import json

with open("data/questions.json", "r", encoding="utf-8") as file:
    dataset = json.load(file)

required_fields = [
    "id",
    "category",
    "question",
    "reference_answer"
]

for item in dataset:
    for field in required_fields:
        if field not in item:
            print(f"Missing field: {field}")