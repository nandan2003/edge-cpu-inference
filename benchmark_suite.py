import time
from llama_cpp import Llama

from models_config import MODEL_REGISTRY

PROMPT_THROUGHPUT = (
    "You are a language model. Generate a detailed answer about how "
    "to implement an efficient tokenizer and sampling loop for CPU-only "
    "inference in Python. Do not include code, only explanation."
)


def _run_single_throughput(llm: Llama, max_tokens: int = 128) -> float:
    """Run one deterministic throughput pass and return tokens/sec."""
    t0 = time.time()
    out = llm(
        PROMPT_THROUGHPUT,
        max_tokens=max_tokens,
        temperature=0.0,
        stop=["<|end|>"],
    )
    dt = time.time() - t0
    text = out["choices"][0]["text"]
    # Token count proxy: word count is good enough for relative throughput
    tokens = max(len(text.split()), 1)
    return tokens / dt if dt > 0 else 0.0


def run_throughput_test(llm: Llama, model_key: str, runs: int = 5) -> float:
    """
    Average throughput over N runs to reduce variance.

    Returns mean tokens/sec.
    """
    speeds = []
    for _ in range(runs):
        s = _run_single_throughput(llm)
        speeds.append(s)
    return round(sum(speeds) / len(speeds), 2) if speeds else 0.0
