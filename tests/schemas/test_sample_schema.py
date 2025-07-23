from schemas.sample_schema import sample_serial, list_sample_serial


def test_sample_serial():
    sample = {
        "created_by": "d3f48a42-0d1e-4270-8e8e-549251cd823d",
        "_id": "12345",
        "name": "Sample Name",
        "description": "This is a sample description.",
        "price": 10.99,
        "quantity": 2,
        "number_of_persons": 4,
        "origin_country": "France",
        "attributes": ["vegan", "gluten-free"],
        "utensils": ["pan", "knife"],
        "ingredients": [
            {"created_by": "d3f48a42-0d1e-4270-8e8e-549251cd823d", "name": "Sugar", "quantity": 100, "unit": "grams"},
            {"created_by": "d3f48a42-0d1e-4270-8e8e-549251cd823d", "name": "Salt"}
        ],
        "steps": [
            {"created_by": "d3f48a42-0d1e-4270-8e8e-549251cd823d", "step_number": 1, "description": "First step", "duration": 10},
            {"created_by": "d3f48a42-0d1e-4270-8e8e-549251cd823d", "step_number": 2, "description": "Second step"}
        ],
        "thumbnail_url": "http://example.com/thumbnail.jpg",
        "large_image_url": "http://example.com/large_image.jpg",
        "source_reference": "Source Reference"
    }
    expected_output = {
        "created_by": "d3f48a42-0d1e-4270-8e8e-549251cd823d",
        "uuid": "12345",
        "name": "Sample Name",
        "description": "This is a sample description.",
        "price": 10.99,
        "quantity": 2,
        "number_of_persons": 4,
        "origin_country": "France",
        "attributes": ["vegan", "gluten-free"],
        "utensils": ["pan", "knife"],
        "ingredients": [
            {"created_by": "d3f48a42-0d1e-4270-8e8e-549251cd823d", "name": "Sugar", "quantity": 100, "unit": "grams"},
            {"created_by": "d3f48a42-0d1e-4270-8e8e-549251cd823d", "name": "Salt", "quantity": None, "unit": None}
        ],
        "steps": [
            {"created_by": "d3f48a42-0d1e-4270-8e8e-549251cd823d", "step_number": 1, "description": "First step", "duration": 10},
            {"created_by": "d3f48a42-0d1e-4270-8e8e-549251cd823d", "step_number": 2, "description": "Second step", "duration": None}
        ],
        "thumbnail_url": "http://example.com/thumbnail.jpg",
        "large_image_url": "http://example.com/large_image.jpg",
        "source_reference": "Source Reference"
    }
    assert sample_serial(sample) == expected_output

    sample_minimal = {
        "created_by": "d3f48a42-0d1e-4270-8e8e-549251cd823d",
        "_id": "67890",
        "name": "Minimal Sample"
    }
    expected_output_minimal = {
        "created_by": "d3f48a42-0d1e-4270-8e8e-549251cd823d",
        "uuid": "67890",
        "name": "Minimal Sample",
        "description": None,
        "price": None,
        "quantity": None,
        "number_of_persons": None,
        "origin_country": None,
        "attributes": [],
        "utensils": [],
        "ingredients": [],
        "steps": [],
        "thumbnail_url": None,
        "large_image_url": None,
        "source_reference": None
    }
    assert sample_serial(sample_minimal) == expected_output_minimal


def test_list_sample_serial():
    samples = [
        {
            "created_by": "d3f48a42-0d1e-4270-8e8e-549251cd823d",
            "_id": "12345",
            "name": "Sample Name",
            "description": "This is a sample description.",
            "price": 10.99,
            "quantity": 2,
            "number_of_persons": 4,
            "origin_country": "France",
            "attributes": ["vegan", "gluten-free"],
            "utensils": ["pan", "knife"],
            "ingredients": [
                {"created_by": "d3f48a42-0d1e-4270-8e8e-549251cd823d", "name": "Sugar", "quantity": 100, "unit": "grams"},
                {"created_by": "d3f48a42-0d1e-4270-8e8e-549251cd823d", "name": "Salt"}
            ],
            "steps": [
                {"created_by": "d3f48a42-0d1e-4270-8e8e-549251cd823d", "step_number": 1, "description": "First step", "duration": 10},
                {"created_by": "d3f48a42-0d1e-4270-8e8e-549251cd823d", "step_number": 2, "description": "Second step"}
            ],
            "thumbnail_url": "http://example.com/thumbnail.jpg",
            "large_image_url": "http://example.com/large_image.jpg",
            "source_reference": "Source Reference"
        },
        {
            "created_by": "d3f48a42-0d1e-4270-8e8e-549251cd823d",
            "_id": "67890",
            "name": "Minimal Sample"
        }
    ]
    expected_output = [
        {
            "created_by": "d3f48a42-0d1e-4270-8e8e-549251cd823d",
            "uuid": "12345",
            "name": "Sample Name",
            "description": "This is a sample description.",
            "price": 10.99,
            "quantity": 2,
            "number_of_persons": 4,
            "origin_country": "France",
            "attributes": ["vegan", "gluten-free"],
            "utensils": ["pan", "knife"],
            "ingredients": [
                {"created_by": "d3f48a42-0d1e-4270-8e8e-549251cd823d", "name": "Sugar", "quantity": 100, "unit": "grams"},
                {"created_by": "d3f48a42-0d1e-4270-8e8e-549251cd823d", "name": "Salt", "quantity": None, "unit": None}
            ],
            "steps": [
                {"created_by": "d3f48a42-0d1e-4270-8e8e-549251cd823d", "step_number": 1, "description": "First step", "duration": 10},
                {"created_by": "d3f48a42-0d1e-4270-8e8e-549251cd823d", "step_number": 2, "description": "Second step", "duration": None}
            ],
            "thumbnail_url": "http://example.com/thumbnail.jpg",
            "large_image_url": "http://example.com/large_image.jpg",
            "source_reference": "Source Reference"
        },
        {
            "created_by": "d3f48a42-0d1e-4270-8e8e-549251cd823d",
            "uuid": "67890",
            "name": "Minimal Sample",
            "description": None,
            "price": None,
            "quantity": None,
            "number_of_persons": None,
            "origin_country": None,
            "attributes": [],
            "utensils": [],
            "ingredients": [],
            "steps": [],
            "thumbnail_url": None,
            "large_image_url": None,
            "source_reference": None
        }
    ]
    assert list_sample_serial(samples) == expected_output

    empty_samples = []
    expected_output_empty = []
    assert list_sample_serial(empty_samples) == expected_output_empty