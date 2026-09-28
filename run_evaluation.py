from src.main import load_dataset
from src.pipeline import evaluate_dataset
from src.reporter import save_results


dataset = load_dataset()

print(f"Dataset'te {len(dataset)} soru var.")

results = evaluate_dataset(dataset)

total_score = 0

for result in results:
    total_score += result["score"]

print("Total score:", total_score)

average_score = total_score / len(results)

print(f"Average score: {average_score:.4f}")

print(f"{len(results)} soru değerlendirildi.")

save_results(
    results,
    average_score,
    "results/evaluation_results.json"
)

print("Sonuçlar kaydedildi.")