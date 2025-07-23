import pytest
from typing import List, Dict, Any

from interfaces.sample_interface import SampleRepository
from models.sample_model import SampleWrite


class TestSampleRepository(SampleRepository):
    """
    A concrete implementation of the SampleRepository interface for testing.
    """
    def __init__(self):
        self.samples = {}
        self.is_closed = False

    def create_sample(self, sample_create: SampleWrite) -> str:
        sample_id = "test-uuid"
        self.samples[sample_id] = sample_create
        return sample_id

    def get_sample(self, sample_id: str) -> Dict[str, Any]:
        if sample_id in self.samples:
            return {"uuid": sample_id, "name": self.samples[sample_id].name}
        return None

    def list_samples(self) -> List[Dict[str, Any]]:
        return [{"uuid": sample_id, "name": sample.name} for sample_id, sample in self.samples.items()]

    def update_sample(self, sample_id: str, sample_update: SampleWrite) -> None:
        if sample_id in self.samples:
            self.samples[sample_id] = sample_update

    def delete_sample(self, sample_id: str) -> None:
        if sample_id in self.samples:
            del self.samples[sample_id]

    def close(self) -> None:
        self.is_closed = True


def test_sample_repository_interface():
    """
    Test that a concrete implementation of SampleRepository can be created
    and that it implements all the required methods.
    """
    # Create a concrete implementation
    repo = TestSampleRepository()

    # Test create_sample
    sample = SampleWrite(name="Test Sample")
    sample_id = repo.create_sample(sample)
    assert sample_id == "test-uuid"

    # Test get_sample
    retrieved_sample = repo.get_sample(sample_id)
    assert retrieved_sample["uuid"] == sample_id
    assert retrieved_sample["name"] == "Test Sample"

    # Test list_samples
    samples = repo.list_samples()
    assert len(samples) == 1
    assert samples[0]["uuid"] == sample_id
    assert samples[0]["name"] == "Test Sample"

    # Test update_sample
    updated_sample = SampleWrite(name="Updated Sample")
    repo.update_sample(sample_id, updated_sample)
    retrieved_sample = repo.get_sample(sample_id)
    assert retrieved_sample["name"] == "Updated Sample"

    # Test delete_sample
    repo.delete_sample(sample_id)
    assert repo.get_sample(sample_id) is None

    # Test close
    repo.close()
    assert repo.is_closed


def test_sample_repository_abstract_methods():
    """
    Test that SampleRepository cannot be instantiated directly
    because it has abstract methods.
    """
    with pytest.raises(TypeError) as exc:
        SampleRepository()

    assert "Can't instantiate abstract class SampleRepository" in str(exc.value)
    assert "abstract methods" in str(exc.value)