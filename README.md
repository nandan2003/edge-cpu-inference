# Edge CPU Inference

A comprehensive toolkit for profiling, benchmarking, and running Local LLMs (GGUF format) on Edge CPUs. This project is built on top of `llama.cpp` and provides automated scripts for model management, memory footprint analysis, and inference performance testing.

## Features

- **Model Management**: Easily download and manage various GGUF models ranging from tiny 15M parameter models to large 22B parameter ones using a unified configuration (`models_config.py`).
- **CPU-Optimized Inference**: Automated setup builds `llama.cpp` locally with AVX2 and FMA optimizations for peak CPU performance.
- **Memory Profiling**: Tools to measure Static RAM usage and dynamic KV-cache growth per token during inference.
- **Benchmarking**: Automated benchmarking scripts to evaluate decode rate, prefill rate, latency, and parallel efficiency across different thread configurations.
- **Interactive Demo**: A simple CLI chat application to interact with downloaded models in real-time.

## Quick Start

### 1. Setup Environment

Run the setup script to install necessary system dependencies, compile `llama.cpp` with optimization flags, and prepare the Python virtual environment:

```bash
./setup.sh
```

### 2. Activate Virtual Environment

Activate the Python virtual environment created by the setup script:

```bash
python -m venv venv
source venv/bin/activate
```

## Usage

### Downloading Models

The project includes a unified model registry in `models_config.py`. To download all configured models:

```bash
python3 download_manager.py
```

*Note: This script uses `tqdm` to display download progress and saves models directly to the root directory.*

### Interactive Chat Demo

To quickly test a model interactively, run the demo script. By default, it will load the `tinyllama_15m` model:

```bash
python3 demo_inference.py
```

### Benchmarking and Profiling

The primary benchmarking logic is driven by `memory_test.py` and `prompts.py`. The suite records inference statistics across different thread counts and context sizes. 

Metrics collected include:
- Prefill Rate (tokens/sec)
- Decode Rate (tokens/sec)
- Total Latency
- Peak Memory (Static + KV Cache)

Results are automatically appended to `report.csv` for further analysis. 

### Utilities

A simple C program (`list.c`) is provided to parse `report.csv` and extract unique model names tested:

```bash
# Compile
gcc list.c -o list_models
# Run
./list_models
```

## Analysis & Insights

Based on extensive benchmarking across various models and thread configurations (captured in `report.csv`), several key patterns for Edge CPU inference have emerged:

### 1. The "Sweet Spot" for Thread Scaling
- **Observation**: Performance scaling is non-linear. Moving from 1 to 4 threads typically yields a **~2x speedup** in decode rate.
- **Diminishing Returns**: Increasing from 4 to 8 threads often shows negligible gains or even performance regression due to cache contention and synchronization overhead on many consumer/edge CPUs.
- **Recommendation**: For most edge devices, **4 threads** provides the best balance between throughput and power efficiency.

### 2. Model Tier Performance (on 4 Threads)
- **Ultra-Small ( < 500M params)**: Models like `TinyLlama (15M)` and `StableLM-2 Tiny (0.13B)` achieve blistering speeds of **60-100+ TPS**, making them ideal for real-time edge triggers or simple classification.
- **Small (0.5B - 2B params)**: The most versatile tier. `Falcon3 (1B)` and `Qwen 2.5 (0.5B)` consistently hit **20-30 TPS**, providing a smooth conversational experience.
- **Medium (3B - 7B params)**: Higher intelligence models like `Gemma (7B)` or `Phi-3 (6B)` run at **3-6 TPS**. While slower, they are capable of complex reasoning within acceptable human-reading speeds.

### 3. Memory Footprint Analysis
| Model Tier | Parameter Count | Peak RAM (GGUF) |
| :--- | :--- | :--- |
| **Tiny** | 15M - 160M | 0.15GB - 0.4GB |
| **Small** | 0.5B - 1.5B | 0.7GB - 2.5GB |
| **Medium** | 3B - 7B | 3.5GB - 12GB |

### 4. Dynamic Memory (KV Cache) Insights
- **Context Overhead**: KV cache growth is a critical factor for long-context applications. Some models (e.g., `Falcon3 (1B)`) exhibit significantly higher memory growth per 1,000 tokens compared to `Phi-3 Mini (1.5B)`.
- **Constraint**: When running on devices with < 4GB RAM, choosing models with low KV cache growth (like `TinyLlama (15M)`) is essential for maintaining stability during long-running sessions.

### 5. Efficiency Leaders
- **High Throughput**: `Falcon3 (1B)` outperformed many 1B competitors, achieving nearly double the TPS of `Gemma (1B)` in similar tests.
- **Resource Efficiency**: `TinyLlama (15M)` remains the undisputed king of efficiency with the highest "CIES Score" (Performance/Resource ratio), proving that specialized small models are highly viable for edge deployment.

## Project Structure

- `setup.sh`: Environment initialization, dependency installation, and `llama.cpp` source compilation.
- `models_config.py`: Registry containing model details (URL, filename, prompt templates).
- `download_manager.py`: Utility to fetch models defined in the registry.
- `demo_inference.py`: Minimal CLI chat interface for testing models.
- `memory_test.py`: Core profiling script to measure RAM footprint and benchmark inference speeds.
- `prompts.py`: Utility to generate synthetic prompts of specific lengths for standardized benchmarking.
- `report.csv`: Aggregated dataset of inference benchmark results.
- `list.c` / `list_models`: C utility to extract unique model runs from the generated report.
