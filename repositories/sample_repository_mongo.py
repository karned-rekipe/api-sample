import re
from typing import List
from urllib.parse import urlparse
from uuid import uuid4

from pymongo import MongoClient

from interfaces.sample_interface import SampleRepository
from models.sample_model import SampleCreateDatabase, SampleUpdate
from schemas.sample_schema import list_sample_serial, sample_serial

def check_uri(uri):
    if not re.match(r"^mongodb://", uri):
        raise ValueError("Invalid URI: URI must start with 'mongodb://'")


def extract_database(uri: str) -> str:
    parsed_uri = urlparse(uri)
    db_name = parsed_uri.path.lstrip("/")

    if not db_name:
        raise ValueError("L'URI MongoDB ne contient pas de nom de base de données.")

    return db_name


class SampleRepositoryMongo(SampleRepository):

    def __init__(self, uri):
        check_uri(uri)
        database = extract_database(uri)

        self.uri = uri
        self.client = MongoClient(self.uri)
        self.db = self.client[database]
        self.collection = "samples"

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()

    def create_sample(self, sample_create: SampleCreateDatabase) -> str:
        sample_data = sample_create.model_dump()
        sample_id = str(uuid4())
        sample_data["_id"] = sample_id
        try:
            new_uuid = self.db[self.collection].insert_one(sample_data)
            return new_uuid.inserted_id
        except Exception as e:
            raise ValueError(f"Failed to create sample in database: {str(e)}")

    def get_sample(self, uuid: str) -> dict:
        result = self.db[self.collection].find_one({"_id": uuid})
        if result is None:
            return None
        sample = sample_serial(result)
        return sample

    def list_samples(self) -> List[dict]:
        result = self.db[self.collection].find()
        samples = list_sample_serial(result)
        return samples

    def update_sample(self, uuid: str, sample_update: SampleUpdate) -> None:
        update_fields = sample_update.model_dump()
        update_fields.pop('created_by', None)
        update_data = {"$set": update_fields}
        self.db[self.collection].find_one_and_update({"_id": uuid}, update_data)


    def delete_sample(self, uuid: str) -> None:
        self.db[self.collection].delete_one({"_id": uuid})

    def close(self):
        self.client.close()
