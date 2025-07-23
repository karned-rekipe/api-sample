from pydantic import BaseModel, Field, HttpUrl
from typing import Optional, List, Dict, Any

class SampleRead(BaseModel):
    uuid: str
    name: str
    description: Optional[str] = None
    price: Optional[float] = None
    quantity: Optional[int] = None
    number_of_persons: Optional[int] = Field(None, gt=0, description="Number of persons the sample serves")
    origin_country: Optional[str] = None
    attributes: List[str] = Field(default_factory=list, description="Attributes like vegetarian, gluten-free, etc.")
    utensils: List[str] = Field(default_factory=list, description="List of utensils needed for the sample")
    ingredients: List[Dict[str, Any]] = Field(default_factory=list, description="List of ingredients with their quantities")
    steps: List[Dict[str, Any]] = Field(default_factory=list, description="List of steps to prepare the sample")
    thumbnail_url: Optional[HttpUrl] = Field(None, description="URL for the sample thumbnail image")
    large_image_url: Optional[HttpUrl] = Field(None, description="URL for a larger image of the sample")
    source_reference: Optional[str] = Field(None, description="Reference for the source of the sample (e.g., book, website)")
    created_by: Optional[str] = Field(None, description="User who created the sample")

class SampleWrite(BaseModel):
    name: str
    description: Optional[str] = None
    price: Optional[float] = None
    quantity: Optional[int] = None
    number_of_persons: Optional[int] = Field(None, gt=0, description="Number of persons the sample serves")
    origin_country: Optional[str] = None
    attributes: List[str] = Field(default_factory=list, description="Attributes like vegetarian, gluten-free, etc.")
    utensils: List[str] = Field(default_factory=list, description="List of utensils needed for the sample")
    ingredients: List[Dict[str, Any]] = Field(default_factory=list, description="List of ingredients with their quantities")
    steps: List[Dict[str, Any]] = Field(default_factory=list, description="List of steps to prepare the sample")
    thumbnail_url: Optional[HttpUrl] = Field(None, description="URL for the sample thumbnail image")
    large_image_url: Optional[HttpUrl] = Field(None, description="URL for a larger image of the sample")
    source_reference: Optional[str] = Field(None, description="Reference for the source of the sample (e.g., book, website)")
    created_by: Optional[str] = Field(None, description="User who created the sample")
