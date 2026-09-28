from src.pipeline import evaluate_dataset
from unittest.mock import patch

@patch("src.pipeline.generate_answer")
def test_evaluate_dataset(mock_generate_answer):
    mock_generate_answer.return_value = "kaynak yok"
    dataset = [
        {
            "id": 1,
            "category": "factual",
            "question": "HTTP 404 nedir?",
            "reference_answer": "Kaynak bulunamadı."
        }
    ]

    results = evaluate_dataset(dataset)

    assert len(results) == 1
    assert results[0]["id"] == 1
    assert "model_answer" in results[0]
    assert "score" in results[0]
    assert results[0]["model_answer"] == "kaynak yok"