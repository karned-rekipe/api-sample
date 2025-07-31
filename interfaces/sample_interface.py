from abc import ABC, abstractmethod
from models.sample_model import SampleCreate, SampleUpdate


class SampleRepository(ABC):

    @abstractmethod
    def create_sample(self, sample_create: SampleCreate):
        pass

    @abstractmethod
    def get_sample(self, sample_id: str):
        pass

    @abstractmethod
    def list_samples(self):
        pass

    @abstractmethod
    def update_sample(self, sample_id: str, sample_update: SampleUpdate):
        pass

    @abstractmethod
    def delete_sample(self, sample_id: str):
        pass

    @abstractmethod
    def close(self):
        pass