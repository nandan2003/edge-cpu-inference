import os

MODELS_DIR = "models"

# Exact filenames from your 'ls' output mapped to their specific templates
MODEL_REGISTRY = {
    "deepseek-r1-1.5b": {
        "name": "DeepSeek R1 Distill (1.5B)",
        "filename": "DeepSeek-R1-Distill-Qwen-1.5B-Q4_K_M.gguf",
        "url": "https://huggingface.co/unsloth/DeepSeek-R1-Distill-Qwen-1.5B-GGUF/resolve/main/DeepSeek-R1-Distill-Qwen-1.5B-Q4_K_M.gguf",
        "prompt_template": "<|im_start|>user\n{prompt}<|im_end|>\n<|im_start|>assistant\n", # ChatML
        "context_window": 32768
    },
    "phi-3-mini": {
        "name": "Phi-3 Mini (3.8B)",
        "filename": "Phi-3-mini-4k-instruct-q4.gguf", 
        "url": "https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-gguf/resolve/main/Phi-3-mini-4k-instruct-q4.gguf",
        "prompt_template": "<|user|>\n{prompt}<|end|>\n<|assistant|>",
        "context_window": 4096
    },
    "mistral-7b": {
        "name": "Mistral 7B (v0.2)",
        "filename": "mistral-7b-instruct-v0.2.Q4_K_M.gguf",
        "url": "https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF/resolve/main/mistral-7b-instruct-v0.2.Q4_K_M.gguf",
        "prompt_template": "[INST] {prompt} [/INST]",
        "context_window": 32768
    },
    "qwen-2.5-3b": {
        "name": "Qwen 2.5 (3B)",
        "filename": "qwen2.5-3b-instruct-q4_k_m.gguf",
        "url": "https://huggingface.co/Qwen/Qwen2.5-3B-Instruct-GGUF/resolve/main/qwen2.5-3b-instruct-q4_k_m.gguf",
        "prompt_template": "<|im_start|>user\n{prompt}<|im_end|>\n<|im_start|>assistant\n",
        "context_window": 32768
    },
    "llama-2-chat": {
        "name": "Llama 2 Chat (7B)",
        "filename": "llama-2-7b-chat.Q4_K_M.gguf",
        "url": "https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/resolve/main/llama-2-7b-chat.Q4_K_M.gguf",
        "prompt_template": "[INST] {prompt} [/INST]",
        "context_window": 4096
    },
    "llama-2-guanaco": {
        "name": "Llama 2 Guanaco (7B)",
        "filename": "llama-2-7b-guanaco-qlora.Q4_K_M.gguf",
        "url": "https://huggingface.co/TheBloke/llama-2-7B-Guanaco-QLoRA-GGUF/resolve/main/llama-2-7b-guanaco-qlora.Q4_K_M.gguf",
        "prompt_template": "### Human: {prompt}\n### Assistant:",
        "context_window": 4096
    },
    "stablelm-zephyr": {
        "name": "StableLM Zephyr (3B)",
        "filename": "stablelm-zephyr-3b.Q4_K_M.gguf",
        "url": "https://huggingface.co/TheBloke/stablelm-zephyr-3b-GGUF/resolve/main/stablelm-zephyr-3b.Q4_K_M.gguf",
        "prompt_template": "<|user|>\n{prompt}<|endoftext|>\n<|assistant|>",
        "context_window": 4096
    },
    "tinyllama-1b": {
        "name": "TinyLlama (1.1B)",
        "filename": "tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf",
        "url": "https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf",
        "prompt_template": "<|user|>\n{prompt}</s>\n<|assistant|>",
        "context_window": 2048
    }
}

def get_model_path(key):
    return os.path.join(MODELS_DIR, MODEL_REGISTRY[key]["filename"])

def list_available_models():
    """Returns list of model keys that actually exist on disk."""
    available = []
    if not os.path.exists(MODELS_DIR):
        return []
        
    for key, meta in MODEL_REGISTRY.items():
        path = os.path.join(MODELS_DIR, meta["filename"])
        if os.path.exists(path):
            available.append(key)
    return available
