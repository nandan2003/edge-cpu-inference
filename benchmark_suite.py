import time
from llama_cpp import Llama
from models_config import get_model_path, MODEL_REGISTRY

def run_throughput_test(model_key, threads=4):
    path = get_model_path(model_key)
    meta = MODEL_REGISTRY[model_key]
    
    print(f"   Testing {meta['name']}...")
    
    try:
        # Load Model
        llm = Llama(
            model_path=path,
            n_threads=threads,
            n_ctx=2048,
            verbose=False
        )

        # Warmup
        llm("Warmup", max_tokens=1)

        # Format Prompt using the specific template for this model
        # We use a coding task to ensure it measures reasoning speed, not just memorization
        raw_prompt = "Write a python function to merge two sorted lists."
        prompt = meta["prompt_template"].format(prompt=raw_prompt)
        
        start_time = time.time()
        output = llm(
            prompt,
            max_tokens=128,
            stop=["<|end|>", "```", "</s>", "<|endoftext|>", "[/INST]"],
            echo=False
        )
        end_time = time.time()

        tokens = output['usage']['completion_tokens']
        duration = end_time - start_time
        tps = tokens / duration if duration > 0 else 0
        
        del llm
        return round(tps, 2)

    except Exception as e:
        print(f"   ❌ Error: {e}")
        return 0.0
