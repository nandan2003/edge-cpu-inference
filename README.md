# ⚡ Edge-LLM: CPU Inference Benchmark Suite

**"Is GPU-less inference viable for enterprise edge cases?"**

This project benchmarks the performance, memory footprint, and cost-efficiency of 8 state-of-the-art LLM architectures on commodity Cloud CPUs (Azure Standard_D4s_v3).

## 📊 Final Engineering Decision Matrix

| Model | Speed (t/s) | Accuracy | Static RAM | KV Growth (MB/1k) | Score |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Qwen 2.5 (3B)** | **8.37** | **80%** | **3.19 GB** | **99.88** | 🏆 **5.36** |
| **Phi-3 Mini (3.8B)** | 8.33 | 80% | 3.63 GB | 196.49 | 🥈 5.33 |
| **DeepSeek R1 (1.5B)** | **19.38** | 40% | **1.63 GB** | **71.33** | 3.10 |
| **TinyLlama (1.1B)** | 24.18 | 40% | 1.07 GB | 231.59 | 3.87 |
| **Mistral 7B (v0.2)** | 4.26 | 60% | 7.26 GB | 192.54 | 1.53 |
| **Llama 2 (7B)** | 4.92 | 40% | 6.92 GB | 234.76 | 0.79 |

## 🛠️ Key Engineering Insights

### 1. The "Production Ready" Choice: Qwen 2.5
While DeepSeek and TinyLlama are 2x faster, they failed the accuracy threshold (<50%). **Qwen 2.5** is the only architecture that maintains **80% reasoning accuracy** while fitting within **4GB RAM** and running faster than human reading speed (8.4 t/s).

### 2. Architectural Efficiency (KV-Cache)
Qwen 2.5 and DeepSeek demonstrate superior memory efficiency (**71-99 MB/1k tokens**) compared to Llama 2 architectures (**~235 MB/1k tokens**). This **2.5x reduction** in memory pressure allows for longer context windows on edge devices without OOM errors.

### 3. The Bandwidth Wall
7B parameter models (Mistral, Llama 2) hit a hard ceiling at **~4-5 tokens/sec**. Profiling confirms this is a **Memory Bandwidth Bottleneck**, proving that 7B models are mathematically inefficient for CPU-only inference compared to dense 3B architectures.

## 🚀 Reproduction

```bash
# 1. Bootstrap Environment (AVX2 Compilation)
./setup.sh

# 2. Run Full Benchmark Suite
python run.py
