from pydantic import BaseModel, Field, HttpUrl
from typing import Optional, List, Dict, Any

class SampleBase(BaseModel):
    name: str
    description: Optional[str] = None

class SampleCreate(SampleBase):
    pass

class SampleCreateDatabase(SampleBase):
    created_by: Optional[str] = Field(None, description="User who created the sample")

class SampleRead(SampleBase):
    uuid: str
    created_by: Optional[str] = Field(None, description="User who created the sample")

class SampleUpdate(BaseModel):
    name: str
    description: Optional[str] = None
