import time
import sys
import os
from llama_cpp import Llama
from models_config import get_model_path, MODEL_REGISTRY

# --- CONFIGURATION ---
# We use Qwen 2.5 because it won the "Efficiency Score" (Fast + Smart)
SELECTED_MODEL = "qwen-2.5-3b" 

if SELECTED_MODEL not in MODEL_REGISTRY:
    print(f"Error: Model config for '{SELECTED_MODEL}' not found.")
    sys.exit(1)

META = MODEL_REGISTRY[SELECTED_MODEL]
MODEL_PATH = get_model_path(SELECTED_MODEL)

if not os.path.exists(MODEL_PATH):
    print(f"Error: Model file not found at {MODEL_PATH}")
    print("Run 'python download_manager.py' first.")
    sys.exit(1)

# --- VISUALS ---
def type_print(text, delay=0.005):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

os.system('clear')
print("="*60)
print(f" 🚀 EDGE INFERENCE ENGINE | ARCHITECTURE: {META['name']}")
print(f" 🔧 HARDWARE: Azure Standard_D4s_v3 (4 vCPU / 16GB RAM)")
print(f" ⚡ QUANTIZATION: 4-bit (Q4_K_M) | ENGINE: llama.cpp (AVX2)")
print("="*60)
print("\nINITIALIZING...", end="", flush=True)

# Load Model
try:
    llm = Llama(
        model_path=MODEL_PATH,
        n_ctx=META["context_window"],
        n_threads=4, 
        verbose=False
    )
    print(" READY.\n")
except Exception as e:
    print(f" FAILED: {e}")
    sys.exit(1)

# --- INTERACTIVE LOOP ---
while True:
    try:
        print("-" * 60)
        user_input = input("\n👤 USER: ")
        if user_input.lower() in ['exit', 'quit']:
            break
            
        # Format Prompt
        prompt = META["prompt_template"].format(prompt=user_input)
        
        print("\n🤖 AI: ", end="", flush=True)
        
        start = time.time()
        stream = llm(
            prompt,
            max_tokens=512,
            stop=["<|end|>", "<|im_end|>", "</s>"],
            stream=True 
        )
        
        token_count = 0
        for output in stream:
            text = output['choices'][0]['text']
            sys.stdout.write(text)
            sys.stdout.flush()
            token_count += 1
            
        duration = time.time() - start
        speed = token_count / duration if duration > 0 else 0
        
        print(f"\n\n[⚡ {speed:.2f} tokens/sec]")
        
    except KeyboardInterrupt:
        print("\nShutting down.")
        break
