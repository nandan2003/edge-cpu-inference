import os
import psutil
from llama_cpp import Llama

from models_config import get_model_path


def measure_static_footprint(model_key: str, n_threads: int = 4, n_ctx: int = 4096) -> float:
    """
    Measure static RAM cost (in GB) to load the model into memory.

    This is load-time memory, no tokens generated.
    """
    proc = psutil.Process(os.getpid())
    before = proc.memory_info().rss

    path = get_model_path(model_key)
    _ = Llama(model_path=path, n_ctx=n_ctx, n_threads=n_threads, verbose=False)

    after = proc.memory_info().rss
    delta_gb = (after - before) / (1024 ** 3)
    return round(delta_gb, 2)
