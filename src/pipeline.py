from src.llm import generate_answer
from src.evaluator import semantic_similarity

def evaluate_question(question, reference_answer):
    model_answer = generate_answer(question)

    score = semantic_similarity(
        reference_answer,
        model_answer
    )

    return model_answer, score


def evaluate_dataset(dataset):
    results = []

    for item in dataset:
        model_answer, score = evaluate_question(
            item["question"],
            item["reference_answer"]
        )

        result = {
            "id": item["id"],
            "category": item["category"],
            "question": item["question"],
            "reference_answer": item["reference_answer"],
            "model_answer": model_answer,
            "score": score
        }

        results.append(result)

    return results