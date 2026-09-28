from src.evaluator import semantic_similarity
from src.pipeline import evaluate_dataset
import pytest

@pytest.mark.integration
def test_similar_texts_have_higher_similarity():
    similar_score = semantic_similarity(
        "Python'da liste değiştirilebilir.",
        "Python listeleri üzerinde değişiklik yapılabilir."
    )

    different_score = semantic_similarity(
        "Python'da liste değiştirilebilir.",
        "Bugün Ankara'da hava yağmurlu."
    )

    assert similar_score > different_score

@pytest.mark.integration
def test_evaluate_dataset():
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