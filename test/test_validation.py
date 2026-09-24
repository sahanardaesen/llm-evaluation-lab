from src.main import validate_dataset

def test_valid_dataset():
    dataset = [
        {
            "id": 1,
            "category": "factual",
            "question": "HTTP 404 nedir?",
            "reference_answer": "Kaynak bulunamadı."
        }
    ]

    assert validate_dataset(dataset) is True