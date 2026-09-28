import pytest

from src.main import validate_dataset


def test_valid_dataset():
    dataset = [
        {
            "id": 1,
            "category": "factual",
            "question": "HTTP 404 nedir?",
            "reference_answer": "Kaynak bulunamadı.",
        }
    ]

    assert validate_dataset(dataset) is True


@pytest.mark.parametrize(
    "missing_field", ["id", "category", "question", "reference_answer"]
)
def test_missing_required_field(missing_field):
    dataset = [
        {
            "id": 1,
            "category": "factual",
            "question": "HTTP 404 nedir?",
            "reference_answer": "Kaynak bulunamadı.",
        }
    ]

    del dataset[0][missing_field]

    assert validate_dataset(dataset) is False


@pytest.mark.parametrize("empty_field", ["category", "question", "reference_answer"])
def test_empty_required_field(empty_field):
    dataset = [
        {
            "id": 1,
            "category": "factual",
            "question": "HTTP 404 nedir?",
            "reference_answer": "Kaynak bulunamadı.",
        }
    ]

    dataset[0][empty_field] = ""

    assert validate_dataset(dataset) is False
