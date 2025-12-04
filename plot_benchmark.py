import matplotlib.pyplot as plt
import pandas as pd
import os

def plot_benchmark_results(results_data):
    """
    Generates a scatter plot from the benchmark results.
    
    Args:
        results_data (list): List of dicts containing:
                             - model (str)
                             - speed (float)
                             - acc_total (float)
                             - ram_cost (float)
    """
    if not results_data:
        print("No data to plot.")
        return

    # Convert to DataFrame for easier handling
    df = pd.DataFrame(results_data)
    
    # Check if we have enough data
    if df.empty:
        print("Empty dataset, skipping plot.")
        return

    plt.figure(figsize=(12, 8))
    
    # Scatter plot: X=Speed, Y=Accuracy, Size=RAM
    # We multiply RAM by 100 to make the bubbles visible
    scatter = plt.scatter(
        df["speed"], 
        df["acc_total"], 
        s=df["ram_cost"] * 100, 
        alpha=0.6, 
        c=df["acc_total"], 
        cmap="viridis", 
        edgecolors="w", 
        linewidth=2
    )

    # Add labels
    for i, row in df.iterrows():
        plt.text(
            row["speed"], 
            row["acc_total"] + 1.5, # Offset label slightly up
            row["model"], 
            fontsize=9, 
            ha='center'
        )

    # Add "Pareto Frontier" reference lines
    plt.axhline(y=50, color='r', linestyle='--', alpha=0.3, label="Min Viable Accuracy (50%)")
    plt.axvline(x=10, color='g', linestyle='--', alpha=0.3, label="Real-Time Threshold (10 t/s)")

    # Styling
    plt.title("Edge LLM Frontier: Speed vs. Accuracy\n(Bubble Size = Total RAM Cost @ 4k Context)", fontsize=14)
    plt.xlabel("Throughput (Tokens / Sec)", fontsize=12)
    plt.ylabel("Overall Accuracy (%)", fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()
    plt.colorbar(scatter, label="Accuracy Score")

    # Save
    output_file = "benchmark_plot.png"
    plt.savefig(output_file, dpi=300, bbox_inches="tight")
    print(f"\n📊 Graph saved to '{output_file}'")
    plt.close()

if __name__ == "__main__":
    # Test with dummy data if run directly
    dummy_data = [
        {"model": "Test-7B", "speed": 5.0, "acc_total": 75.0, "ram_cost": 8.0},
        {"model": "Test-1B", "speed": 25.0, "acc_total": 40.0, "ram_cost": 1.5},
    ]
    plot_benchmark_results(dummy_data)
