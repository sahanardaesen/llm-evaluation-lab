from src.llm import generate_answer
from src.evaluator import semantic_similarity


def evaluate_question(question, reference_answer):
    model_answer = generate_answer(question)

    score = semantic_similarity(
        reference_answer,
        model_answer
    )

    return model_answer, score