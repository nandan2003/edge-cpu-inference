import time
from tabulate import tabulate
from models_config import list_available_models, MODEL_REGISTRY
from benchmark_suite import run_throughput_test
from kv_cache_profile import profile_kv_growth  # <--- Re-imported
from memory_test import measure_static_footprint
from accuracy_test import evaluate_accuracy

def main():
    models = list_available_models()
    
    if not models:
        print("❌ No models found! Run 'python download_manager.py' first.")
        return

    report_data = []
    
    print(f"\n🚀 STARTING ULTIMATE BENCHMARK SUITE ({len(models)} Models)\n")

    for key in models:
        name = MODEL_REGISTRY[key]['name']
        print(f"🔹 Benchmarking: {name}")
        
        # 1. Throughput (Speed)
        tps = run_throughput_test(key)
        
        # 2. Accuracy (Quality)
        accuracy = evaluate_accuracy(key)
        
        # 3. Systems Metrics (The Hardware Engineering Flex)
        ram_gb = measure_static_footprint(key)
        kv_growth = profile_kv_growth(key) # <--- Restored
        
        # 4. Efficiency Score
        # We value Accuracy heavily. If Accuracy < 50%, Score is penalized.
        # Score = Speed * (Accuracy/100)^2
        # This prevents "Fast but Dumb" models from winning.
        acc_ratio = accuracy / 100
        efficiency_score = round(tps * (acc_ratio ** 2), 2)
        
        report_data.append([name, tps, f"{accuracy}%", ram_gb, kv_growth, efficiency_score])

    print("\n\n" + "="*90)
    print("FINAL ENGINEERING DECISION MATRIX")
    print("="*90)
    
    headers = ["Model", "Speed (t/s)", "Accuracy", "Static RAM (GB)", "KV Growth (MB/1k)", "Score"]
    print(tabulate(report_data, headers=headers, tablefmt="github"))
    print("\n")

if __name__ == "__main__":
    main()
