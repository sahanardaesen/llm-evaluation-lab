import json


def validate_dataset(dataset):
    required_fields = [
        "id",
        "category",
        "question",
        "reference_answer"
    ]

    for item in dataset:
        for field in required_fields:
            if field not in item:
                print(f"Eksik alan: {field}, kayıt id: {item.get('id')}")
                return False

    return True


def get_category_counts(dataset):
    category_counts = {}

    for item in dataset:
        category = item["category"]

        if category not in category_counts:
            category_counts[category] = 0

        category_counts[category] += 1

    return category_counts


with open("data/questions.json", "r", encoding="utf-8") as file:
    dataset = json.load(file)


is_valid = validate_dataset(dataset)

print("Dataset valid:", is_valid)

category_counts = get_category_counts(dataset)

print("\nCategory counts:")

for category, count in category_counts.items():
    print(f"{category}: {count}")