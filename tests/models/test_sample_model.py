import pytest
from pydantic import ValidationError

from models.sample_model import SampleWrite


def test_sample_creation():
    sample_data = {
        "name": "Sample Name",
        "description": "This is a sample description.",
        "price": 10.99,
        "quantity": 2,
        "number_of_persons": 4,
        "origin_country": "France",
        "attributes": ["vegan", "gluten-free"],
        "utensils": ["pan", "knife"],
        "ingredients": [
            {"name": "Sugar", "quantity": 100, "unit": "grams"},
            {"name": "Salt"}
        ],
        "steps": [
            {"step_number": 1, "description": "First step", "duration": "10 min"},
            {"step_number": 2, "description": "Second step"}
        ],
        "thumbnail_url": "http://example.com/thumbnail.jpg",
        "large_image_url": "http://example.com/large_image.jpg",
        "source_reference": "Source Reference"
    }
    sample = SampleWrite(**sample_data)
    assert sample.name == "Sample Name"
    assert sample.description == "This is a sample description."
    assert sample.price == 10.99
    assert sample.quantity == 2
    assert sample.number_of_persons == 4
    assert sample.origin_country == "France"
    assert sample.attributes == ["vegan", "gluten-free"]
    assert sample.utensils == ["pan", "knife"]
    assert len(sample.ingredients) == 2
    assert len(sample.steps) == 2
    assert str(sample.thumbnail_url) == "http://example.com/thumbnail.jpg"
    assert str(sample.large_image_url) == "http://example.com/large_image.jpg"
    assert sample.source_reference == "Source Reference"


def test_sample_creation_with_defaults():
    sample_data = {
        "name": "Minimal Sample"
    }
    sample = SampleWrite(**sample_data)
    assert sample.name == "Minimal Sample"
    assert sample.description is None
    assert sample.price is None
    assert sample.quantity is None
    assert sample.number_of_persons is None
    assert sample.origin_country is None
    assert sample.attributes == []
    assert sample.utensils == []
    assert sample.ingredients == []
    assert sample.steps == []
    assert sample.thumbnail_url is None
    assert sample.large_image_url is None
    assert sample.source_reference is None


def test_sample_validation_error():
    invalid_sample_data = {
        "name": "Invalid Sample",
        "number_of_persons": 0
    }
    with pytest.raises(ValidationError):
        SampleWrite(**invalid_sample_data)


def test_sample_missing_fields():
    incomplete_sample_data = {
        "description": "Incomplete Sample"
    }
    with pytest.raises(ValidationError):
        SampleWrite(**incomplete_sample_data)

def test_sample_invalid_description_type():
    invalid_sample_data = {
        "name": "Invalid Sample",
        "description": 123
    }
    with pytest.raises(ValidationError):
        SampleWrite(**invalid_sample_data)

def test_sample_invalid_price_type():
    invalid_sample_data = {
        "name": "Invalid Sample",
        "price": "ten"
    }
    with pytest.raises(ValidationError):
        SampleWrite(**invalid_sample_data)

def test_sample_invalid_quantity_type():
    invalid_sample_data = {
        "name": "Invalid Sample",
        "quantity": "two"
    }
    with pytest.raises(ValidationError):
        SampleWrite(**invalid_sample_data)

def test_sample_invalid_number_of_persons_type():
    invalid_sample_data = {
        "name": "Invalid Sample",
        "number_of_persons": "four"
    }
    with pytest.raises(ValidationError):
        SampleWrite(**invalid_sample_data)

def test_sample_invalid_origin_country_type():
    invalid_sample_data = {
        "name": "Invalid Sample",
        "origin_country": 42
    }
    with pytest.raises(ValidationError):
        SampleWrite(**invalid_sample_data)

def test_sample_invalid_attributes_type():
    invalid_sample_data = {
        "name": "Invalid Sample",
        "attributes": "vegan"
    }
    with pytest.raises(ValidationError):
        SampleWrite(**invalid_sample_data)

def test_sample_invalid_utensils_type():
    invalid_sample_data = {
        "name": "Invalid Sample",
        "utensils": "pan"
    }
    with pytest.raises(ValidationError):
        SampleWrite(**invalid_sample_data)

def test_sample_invalid_ingredients_type():
    invalid_sample_data = {
        "name": "Invalid Sample",
        "ingredients": "Sugar"
    }
    with pytest.raises(ValidationError):
        SampleWrite(**invalid_sample_data)

def test_sample_invalid_steps_type():
    invalid_sample_data = {
        "name": "Invalid Sample",
        "steps": "First step"
    }
    with pytest.raises(ValidationError):
        SampleWrite(**invalid_sample_data)

def test_sample_invalid_thumbnail_url_type():
    invalid_sample_data = {
        "name": "Invalid Sample",
        "thumbnail_url": 123
    }
    with pytest.raises(ValidationError):
        SampleWrite(**invalid_sample_data)

def test_sample_invalid_large_image_url_type():
    invalid_sample_data = {
        "name": "Invalid Sample",
        "large_image_url": 123
    }
    with pytest.raises(ValidationError):
        SampleWrite(**invalid_sample_data)

def test_sample_invalid_source_reference_type():
    invalid_sample_data = {
        "name": "Invalid Sample",
        "source_reference": 123
    }
    with pytest.raises(ValidationError):
        SampleWrite(**invalid_sample_data)

def test_sample_invalid_url():
    invalid_sample_data = {
        "name": "Invalid Sample",
        "thumbnail_url": "invalid_url",
        "large_image_url": "invalid_url"
    }
    with pytest.raises(ValidationError):
        SampleWrite(**invalid_sample_data)

def test_sample_invalid_list_types():
    invalid_sample_data = {
        "name": "Invalid Sample",
        "attributes": ["vegan", 123],
        "utensils": ["pan", 42]
    }
    with pytest.raises(ValidationError):
        SampleWrite(**invalid_sample_data)