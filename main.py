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