from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim


model = SentenceTransformer("all-MiniLM-L6-v2")


def semantic_similarity(text_a, text_b):
    embeddings = model.encode([text_a, text_b])

    embedding_a = embeddings[0]
    embedding_b = embeddings[1]

    similarity = cos_sim(embedding_a, embedding_b)

    return similarity.item()