import json
import re
from llama_cpp import Llama
from models_config import get_model_path, MODEL_REGISTRY

# Hard logic tests (Pass/Fail)
TEST_SUITE = [
    {
        "id": 1,
        "task": "Math",
        "prompt": "What is 25 * 4 + 10? Answer with just the number.",
        "expected": "110"
    },
    {
        "id": 2,
        "task": "JSON Extraction",
        "prompt": "Extract the name from this JSON: {\"user\": \"Alice\", \"id\": 99}. Return JSON only.",
        "check": lambda x: "Alice" in x
    },
    {
        "id": 3,
        "task": "Coding",
        "prompt": "Write a Python function `def add(a, b):` that returns their sum. Return code only.",
        "check": lambda x: "return a + b" in x or "return a+b" in x
    },
    {
        "id": 4,
        "task": "Reasoning",
        "prompt": "If A is faster than B, and B is faster than C, who is the slowest?",
        "check": lambda x: "C" in x
    },
    {
        "id": 5,
        "task": "Format",
        "prompt": "Convert 'Hello' to uppercase. Return just the word.",
        "expected": "HELLO"
    }
]

def evaluate_accuracy(model_key):
    path = get_model_path(model_key)
    meta = MODEL_REGISTRY[model_key]
    print(f"   🧠 IQ Testing: {meta['name']}...")
    
    try:
        llm = Llama(model_path=path, n_ctx=2048, n_threads=4, verbose=False)
        score = 0
        
        for test in TEST_SUITE:
            # Format prompt with model's specific template (Crucial for small models)
            full_prompt = meta["prompt_template"].format(prompt=test["prompt"])
            
            output = llm(
                full_prompt, 
                max_tokens=100, 
                stop=["<|end|>", "```", "\n\n"], 
                echo=False
            )
            response = output['choices'][0]['text'].strip()
            
            # Check correctness
            passed = False
            if "expected" in test:
                if test["expected"] in response: passed = True
            elif "check" in test:
                if test["check"](response): passed = True
                
            if passed: score += 1
            
        del llm
        
        # Return percentage (e.g., 80.0)
        return (score / len(TEST_SUITE)) * 100

    except Exception as e:
        print(f"   ❌ Test Failed: {e}")
        return 0.0
