import json

from src.reporter import save_results


def test_save_results(tmp_path):
    results = [
        {
            "id": 1,
            "category": "factual",
            "score": 0.85
        }
    ]

    file_path = tmp_path / "results.json"

    save_results(results, file_path)

    with open(file_path, "r", encoding="utf-8") as file:
        saved_results = json.load(file)

    assert saved_results == results