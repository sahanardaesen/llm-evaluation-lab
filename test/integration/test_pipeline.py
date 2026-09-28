from src.pipeline import evaluate_question
import pytest

@pytest.mark.integration
def test_real_llm_pipeline():
    question = "Python'da liste ile tuple arasındaki fark nedir?"

    reference_answer = (
        "Liste değiştirilebilir, tuple ise değiştirilemez."
    )

    model_answer, score = evaluate_question(
        question,
        reference_answer
    )

    assert model_answer
    assert 0 <= score <= 1