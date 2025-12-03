import time
import sys
from llama_cpp import Llama

# CONFIGURATION: Use the High-Speed Model
MODEL_PATH = "./Phi-3-mini-4k-instruct-q4.gguf"

print("--- LOADING ENGINE (PHI-3 3.8B) ---")
llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=4096,
    n_threads=4, 
    verbose=False
)

print("\n" + "="*50)
print(" 🚀 HIGH-PERFORMANCE CPU INFERENCE READY")
print(f" Model: Phi-3 Mini | Quant: Q4_0 | Threads: 4")
print("="*50 + "\n")

# Interactive Loop
while True:
    try:
        user_input = input("\nUser: ")
        if user_input.lower() in ['exit', 'quit']:
            break
            
        # Phi-3 Prompt Format
        prompt = f"<|user|>\n{user_input}<|end|>\n<|assistant|>"
        
        print("AI: ", end="", flush=True)
        
        start = time.time()
        stream = llm(
            prompt,
            max_tokens=250,
            stop=["<|end|>"],
            stream=True 
        )
        
        token_count = 0
        for output in stream:
            text = output['choices'][0]['text']
            print(text, end="", flush=True)
            token_count += 1
            
        print("\n")
        
    except KeyboardInterrupt:
        break

print("\nShutting down.")
