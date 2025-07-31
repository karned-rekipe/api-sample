from fastapi import HTTPException
from models.sample_model import SampleRead, SampleUpdate
from common_api.utils.v0 import get_state_repos


def create_sample(request, new_sample) -> str:
    try:
        repos = get_state_repos(request)
        new_uuid = repos.sample_repo.create_sample(new_sample)
        if not isinstance(new_uuid, str):
            raise TypeError("The method create_sample did not return a str.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while creating the sample: {e}")

    return new_uuid

def get_samples(request) -> list[SampleRead]:
    try:
        repos = get_state_repos(request)
        samples = repos.sample_repo.list_samples()
        if not isinstance(samples, list):
            raise TypeError("The method list_samples did not return a list.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while get the list of samples: {e}")

    return samples


def get_sample(request, uuid: str) -> SampleRead:
    try:
        repos = get_state_repos(request)
        sample = repos.sample_repo.get_sample(uuid)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while retrieving the sample: {e}")

    if sample is None:
        raise HTTPException(status_code=404, detail="Sample not found")

    return sample

def update_sample(request, uuid: str, sample_update: SampleUpdate) -> None:
    try:
        repos = get_state_repos(request)
        repos.sample_repo.update_sample(uuid, sample_update)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while updating the sample: {e}")

def delete_sample(request, uuid: str) -> None:
    try:
        repos = get_state_repos(request)
        repos.sample_repo.delete_sample(uuid)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while deleting the sample: {e}")