

def sample_serial(sample) -> dict:
    return {
        "uuid": str(sample["_id"]),
        "name": sample["name"],
        "description": sample.get("description"),
        "created_by": sample.get("created_by")
    }


def list_sample_serial(samples) -> list:
    return [sample_serial(sample) for sample in samples]
