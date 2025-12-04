import time
import psutil
import os
import gc
from tabulate import tabulate
from llama_cpp import Llama
from models_config import list_available_models, get_model_path, MODEL_REGISTRY
from benchmark_suite import run_throughput_test
from kv_cache_profile import profile_kv_growth
from memory_test import measure_static_footprint
from accuracy_test import evaluate_accuracy
from plot_benchmark import plot_benchmark_results  # <--- Imported

def get_ram_gb():
    return psutil.Process(os.getpid()).memory_info().rss / (1024**3)

def main():
    models = list_available_models()
    if not models:
        print("No models available. Run 'python download_manager.py' first.")
        return

    raw_data = []
    print("\nSTARTING MULTI-DIMENSIONAL BENCHMARK\n")

    for key in models:
        name = MODEL_REGISTRY[key]['name']
        print(f"Processing: {name}")

        gc.collect()
        base_ram = get_ram_gb()

        try:
            path = get_model_path(key)

            llm = Llama(
                model_path=path,
                n_ctx=4096,
                n_threads=4,
                verbose=False
            )

            static_ram = round(get_ram_gb() - base_ram, 2)

            speed = run_throughput_test(llm, key)

            acc_metrics = evaluate_accuracy(llm, key)

            kv_growth = profile_kv_growth(llm)

            total_ram_4k = static_ram + ((kv_growth * 4) / 1024)

            del llm
            gc.collect()

            raw_data.append({
                "model": name,
                "speed": speed,
                "ram_cost": round(total_ram_4k, 2),
                "acc_total": acc_metrics["Total"],
                "acc_code": acc_metrics["Coding"],
                "acc_reason": acc_metrics["Reasoning"],
                "acc_chat": acc_metrics["Chat"]
            })

        except Exception as e:
            print(f"Failure: {e}")

    # --- REPORTING ---

    print("\n" + "="*80)
    print("FINAL RECOMMENDATION MATRIX")
    print("="*80)

    code_rank = sorted(raw_data, key=lambda x: (x['acc_code'], x['speed']), reverse=True)
    print("\nCODING USE-CASE")
    table = [[m['model'], f"{m['acc_code']}%", f"{m['speed']} t/s"] for m in code_rank]
    print(tabulate(table, headers=["Model", "Coding Score", "Speed"], tablefmt="github"))

    logic_rank = sorted(raw_data, key=lambda x: (x['acc_reason'], x['speed']), reverse=True)
    print("\nREASONING USE-CASE")
    table = [[m['model'], f"{m['acc_reason']}%", f"{m['speed']} t/s"] for m in logic_rank]
    print(tabulate(table, headers=["Model", "Reasoning Score", "Speed"], tablefmt="github"))

    budget_rank = sorted(raw_data, key=lambda x: x['ram_cost'])
    print("\nLOW HARDWARE USE-CASE")
    table = [[m['model'], f"{m['ram_cost']} GB", f"{m['acc_total']}%"] for m in budget_rank]
    print(tabulate(table, headers=["Model", "Total RAM (4k)", "Overall Acc"], tablefmt="github"))

    speed_rank = sorted(raw_data, key=lambda x: x['speed'], reverse=True)
    print("\nREAL-TIME USE-CASE")
    table = [[m['model'], f"{m['speed']} t/s", f"{m['acc_total']}%"] for m in speed_rank]
    print(tabulate(table, headers=["Model", "Speed", "Overall Acc"], tablefmt="github"))

    print("\n" + "="*80)
    print("FULL METRIC TABLE")
    print("="*80)

    rows = [
        [
            m["model"],
            f"{m['speed']} t/s",
            f"{m['acc_total']}%",
            f"{m['acc_code']}%",
            f"{m['acc_reason']}%",
            f"{m['acc_chat']}%",
            f"{m['ram_cost']} GB"
        ]
        for m in raw_data
    ]

    print(tabulate(
        rows,
        headers=[
            "Model", "Speed", "Acc(Total)",
            "Acc(Coding)", "Acc(Reason)",
            "Acc(Chat)", "RAM(4k)"
        ],
        tablefmt="github"
    ))

    # --- PLOTTING ---
    try:
        plot_benchmark_results(raw_data)
    except Exception as e:
        print(f"\n⚠️ Plotting failed: {e}")
        print("Ensure matplotlib and pandas are installed.")

if __name__ == "__main__":
    main()
