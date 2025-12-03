import psutil
import os
import gc
from llama_cpp import Llama
from models_config import get_model_path

def measure_static_footprint(model_key):
    path = get_model_path(model_key)
    process = psutil.Process(os.getpid())
    
    # Baseline (Python overhead)
    gc.collect()
    start_mem = process.memory_info().rss
    
    try:
        # Load model with minimal context just to measure weight footprint
        llm = Llama(model_path=path, n_threads=4, n_ctx=512, verbose=False)
        
        peak_mem = process.memory_info().rss
        footprint_gb = (peak_mem - start_mem) / (1024**3)
        
        del llm
        return round(footprint_gb, 2)
        
    except Exception:
        return 0.0
