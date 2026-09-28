from src.main import load_dataset
from src.pipeline import evaluate_dataset
from src.reporter import save_results


dataset = load_dataset()

print(f"Dataset'te {len(dataset)} soru var.")

results = evaluate_dataset(dataset)

print(f"{len(results)} soru değerlendirildi.")

save_results(
    results,
    "results/evaluation_results.json"
)

print("Sonuçlar kaydedildi.")