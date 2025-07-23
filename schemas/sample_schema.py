

def sample_serial(sample) -> dict:
    return {
        "uuid": str(sample["_id"]),
        "name": sample["name"],
        "description": sample.get("description"),
        "price": sample.get("price"),
        "quantity": sample.get("quantity"),
        "number_of_persons": sample.get("number_of_persons"),
        "origin_country": sample.get("origin_country"),
        "attributes": sample.get("attributes", []),
        "utensils": sample.get("utensils", []),
        "ingredients": [{"name": item.get("name"), "quantity": item.get("quantity"), "unit": item.get("unit"), "created_by": item.get("created_by")} for item in sample.get("ingredients", [])],
        "steps": [{"step_number": item.get("step_number"), "description": item.get("description"), "duration": item.get("duration"), "created_by": item.get("created_by")} for item in sample.get("steps", [])],
        "thumbnail_url": sample.get("thumbnail_url"),
        "large_image_url": sample.get("large_image_url"),
        "source_reference": sample.get("source_reference"),
        "created_by": sample.get("created_by")
    }


def list_sample_serial(samples) -> list:
    return [sample_serial(sample) for sample in samples]
