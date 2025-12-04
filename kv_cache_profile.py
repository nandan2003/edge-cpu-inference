import os
import time
import psutil
from llama_cpp import Llama

from models_config import get_model_path

PROMPT_KV = (
    "You are profiling long-context behavior. Continue this discussion in depth "
    "about the trade-offs between key-value cache size, context length, and "
    "latency in autoregressive transformers."
)


def profile_kv_growth(llm: Llama, target_tokens: int = 256) -> float:
    """
    Estimate KV-cache growth in MB per 1000 generated tokens.

    Approach:
      - Measure RSS before generation
      - Generate target_tokens
      - Measure RSS after generation
      - Compute growth per 1k tokens
    """
    proc = psutil.Process(os.getpid())
    before = proc.memory_info().rss

    out = llm(
        PROMPT_KV,
        max_tokens=target_tokens,
        temperature=0.2,
        stop=["<|end|>"],
    )

    after = proc.memory_info().rss
    delta_bytes = max(after - before, 0)
    delta_mb = delta_bytes / (1024 ** 2)

    text = out["choices"][0]["text"]
    tokens = max(len(text.split()), 1)

    mb_per_1k = delta_mb * (1000.0 / tokens)
    return round(mb_per_1k, 2)
