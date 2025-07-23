from typing import Type

from common_api.services.v0 import Logger
from repositories.sample_repository_mongo import SampleRepositoryMongo

logger = Logger()


class Repositories:
    def __init__(self, sample_repo=None):
        self.sample_repo = sample_repo


class BucketRepositories:
    def __init__(self, sample_bucket_repo=None):
        self.sample_bucket_repo = sample_bucket_repo


def get_repositories(uri: str) -> Repositories | Type[Repositories]:
    if uri.startswith("mongodb"):
        logger.info("Using MongoDB repositories")
        return Repositories(
            sample_repo = SampleRepositoryMongo(uri)
        )

    return Repositories


def get_bucket_repositories(credentials) -> BucketRepositories | Type[BucketRepositories]:

    return BucketRepositories
