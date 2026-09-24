from src.evaluator import semantic_similarity


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