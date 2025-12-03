import psutil
import os
import gc
from llama_cpp import Llama
from models_config import get_model_path, MODEL_REGISTRY

def get_process_memory_mb():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / (1024 * 1024)

def profile_kv_growth(model_key):
    path = get_model_path(model_key)
    print(f"   Profiling KV Cache: {MODEL_REGISTRY[model_key]['name']}...")
    
    try:
        gc.collect()
        # Load with 4096 context to allow growth testing
        llm = Llama(model_path=path, n_ctx=4096, n_threads=4, verbose=False)
        
        # Baseline Memory (Model Loaded, Empty Context)
        base_mem = get_process_memory_mb()
        
        results = []
        # We test at 256, 1024, and 2048 tokens
        context_steps = [256, 1024, 2048]
        
        for tokens in context_steps:
            # Generate dummy tokens to fill context (Token ID 1 is usually safe)
            dummy_input = [1] * tokens 
            
            # Force evaluation (filling the KV cache)
            llm.eval(dummy_input)
            
            curr_mem = get_process_memory_mb()
            growth = curr_mem - base_mem
            results.append(growth)
            
        del llm
        
        # Calculate growth rate (MB per 1024 tokens)
        # Using the delta between 1024 and 2048 for stability
        if len(results) >= 3:
            delta_mb = results[2] - results[1]
            return round(delta_mb, 2)
        return 0.0

    except Exception as e:
        print(f"   ❌ Error: {e}")
        return 0.0
