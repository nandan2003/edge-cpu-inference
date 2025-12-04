import os

MODELS_DIR = "models"

# Single source of truth for models and their filenames
MODEL_REGISTRY = {
    "deepseek_r1": {
        "name": "DeepSeek R1 Distill (1.5B)",
        "filename": "DeepSeek-R1-Distill-Qwen-1.5B-Q4_K_M.gguf",
        "prompt_template": "{prompt}",
    },
    "phi3_mini": {
        "name": "Phi-3 Mini (3.8B)",
        "filename": "Phi-3-mini-4k-instruct-q4.gguf",
        "prompt_template": "{prompt}",
    },
    "mistral_7b": {
        "name": "Mistral 7B (v0.2)",
        "filename": "mistral-7b-instruct-v0.2.Q4_K_M.gguf",
        "prompt_template": "{prompt}",
    },
    "qwen_2_5": {
        "name": "Qwen 2.5 (3B)",
        "filename": "qwen2.5-3b-instruct-q4_k_m.gguf",
        "prompt_template": "{prompt}",
    },
    "llama2_chat": {
        "name": "Llama 2 Chat (7B)",
        "filename": "llama-2-7b-chat.Q4_K_M.gguf",
        "prompt_template": "{prompt}",
    },
    "llama2_guanaco": {
        "name": "Llama 2 Guanaco (7B)",
        "filename": "llama-2-7b-guanaco-qlora.Q4_K_M.gguf",
        "prompt_template": "{prompt}",
    },
    "stablelm_zephyr": {
        "name": "StableLM Zephyr (3B)",
        "filename": "stablelm-zephyr-3b.Q4_K_M.gguf",
        "prompt_template": "{prompt}",
    },
    "tinyllama": {
        "name": "TinyLlama (1.1B)",
        "filename": "tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf",
        "prompt_template": "{prompt}",
    },
}


def get_model_path(key: str) -> str:
    entry = MODEL_REGISTRY[key]
    return os.path.join(MODELS_DIR, entry["filename"])


def list_available_models():
    """Return list of keys for models that actually exist on disk."""
    available = []
    for key, meta in MODEL_REGISTRY.items():
        path = os.path.join(MODELS_DIR, meta["filename"])
        if os.path.exists(path):
            available.append(key)
    return available
