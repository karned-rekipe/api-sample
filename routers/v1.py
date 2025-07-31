from fastapi import APIRouter, HTTPException, status, Request
from config.config import API_TAG_NAME
from common_api.decorators.v0.check_permission import check_permissions
from models.sample_model import SampleCreate, SampleRead, SampleUpdate
from common_api.services.v0 import Logger
from services.samples_service import create_sample, get_samples, get_sample, update_sample, delete_sample

logger = Logger()

VERSION = "v1"
api_group_name = f"/{API_TAG_NAME}/{VERSION}/"

router = APIRouter(
    tags=[api_group_name],
    prefix=f"/sample/{VERSION}"
)


@router.post("/", status_code=status.HTTP_201_CREATED)
@check_permissions(['create'])
async def create_new_sample(request: Request, sample: SampleCreate) -> dict:
    logger.api("POST /sample/v1/")
    new_uuid = create_sample(request, sample)
    return {"uuid": new_uuid}


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[SampleRead])
@check_permissions(['read', 'read_own'])
async def read_samples(request: Request):
    logger.api("GET /sample/v1/")
    return get_samples(request)


@router.get("/{uuid}", status_code=status.HTTP_200_OK, response_model=SampleRead)
@check_permissions(['read', 'read_own'])
async def read_sample(request: Request, uuid: str):
    logger.api("GET /sample/v1/{uuid}")
    sample = get_sample(request, uuid)
    if sample is None:
        raise HTTPException(status_code=404, detail="Sample not found")
    return sample


@router.put("/{uuid}", status_code=status.HTTP_204_NO_CONTENT)
@check_permissions(['update', 'update_own'])
async def update_existing_sample(request: Request, uuid: str, sample_update: SampleUpdate):
    logger.api("PUT /sample/v1/{uuid}")
    update_sample(request, uuid, sample_update)


@router.delete("/{uuid}", status_code=status.HTTP_204_NO_CONTENT)
@check_permissions(['delete', 'delete_own'])
async def delete_existing_sample(request: Request, uuid: str):
    logger.api("DELETE /sample/v1/{uuid}")
    delete_sample(request, uuid)
