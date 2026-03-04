import os

MODELS_DIR = "/mnt/models"

# Single source of truth for models and their filenames
MODEL_REGISTRY = {
    # Tiny Models (< 1B)
    "tinyllama_15m": {
        "name": "TinyLlama (15M)",
        "filename": "tinyllama-15M.Q4_K_M.gguf",
        "url": "https://huggingface.co/mradermacher/tinyllama-15M-GGUF/resolve/main/tinyllama-15M.Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 0.015,
        "filesize": 0.01
    },
    "stablelm_2_tiny": {
        "name": "StableLM-2 Tiny (0.13B)",
        "filename": "tiny-random-stablelm-2.Q4_K_M.gguf",
        "url": "https://huggingface.co/mradermacher/tiny-random-stablelm-2-GGUF/resolve/main/tiny-random-stablelm-2.Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 0.127,
        "filesize": 0.08
    },
    "gptneox_160m": {
        "name": "GPTNeoX (160M)",
        "filename": "GPTNeoX-160m-final.Q4_K_M.gguf",
        "url": "https://huggingface.co/mradermacher/GPTNeoX-160m-final-GGUF/resolve/main/GPTNeoX-160m-final.Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 0.16,
        "filesize": 0.10
    },
    "openelm_270m": {
        "name": "OpenELM (270M)",
        "filename": "OpenELM-270M.Q4_K_M.gguf",
        "url": "https://huggingface.co/mradermacher/OpenELM-270M-GGUF/resolve/main/OpenELM-270M.Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 0.27,
        "filesize": 0.16
    },
    "smollm_360m": {
        "name": "SmolLM (0.35B)",
        "filename": "SmolLM-360M-Instruct.Q4_K_M.gguf",
        "url": "https://huggingface.co/mradermacher/SmolLM-360M-Instruct-GGUF/resolve/main/SmolLM-360M-Instruct.Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 0.35,
        "filesize": 0.25
    },
    "gptneox_410m": {
        "name": "GPTNeoX (410M)",
        "filename": "GPTNeoX-spanish_poet-410m.Q4_K_M.gguf",
        "url": "https://huggingface.co/mradermacher/GPTNeoX-spanish_poet-410m-GGUF/resolve/main/GPTNeoX-spanish_poet-410m.Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 0.41,
        "filesize": 0.25
    },
    "openelm_450m": {
        "name": "OpenELM (450M)",
        "filename": "OpenELM-450M.Q4_K_M.gguf",
        "url": "https://huggingface.co/mradermacher/OpenELM-450M-GGUF/resolve/main/OpenELM-450M.Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 0.45,
        "filesize": 0.27
    },
    "falcon_0_5b": {
        "name": "Falcon (0.5B)",
        "filename": "Falcon-H1-0.5B-Base.Q4_K_M.gguf",
        "url": "https://huggingface.co/mradermacher/Falcon-H1-0.5B-Base-GGUF/resolve/main/Falcon-H1-0.5B-Base.Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 0.5,
        "filesize": 0.29
    },
    "qwen_0_5b": {
        "name": "Qwen 2.5 (0.5B)",
        "filename": "qwen2.5-0.5b-instruct-q4_k_m.gguf",
        "url": "https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF/resolve/main/qwen2.5-0.5b-instruct-q4_k_m.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 0.63,
        "filesize": 0.46
    },
    "kiwi_0_7b": {
        "name": "Kiwi (0.7B)",
        "filename": "Kiwi-1.0-0.7B-32k.Q4_K_M.gguf",
        "url": "https://huggingface.co/mradermacher/Kiwi-1.0-0.7B-32k-GGUF/resolve/main/Kiwi-1.0-0.7B-32k.Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 0.7,
        "filesize": 0.50
    },

    # Small Models (1B - 2B)
    "gemma_1b": {
        "name": "Gemma (1B)",
        "filename": "gemma-3-1b-it-Q4_K_M.gguf",
        "url": "https://huggingface.co/unsloth/gemma-3-1b-it-GGUF/resolve/main/gemma-3-1b-it-Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 1.0,
        "filesize": 0.75
    },
    "phi_1_5": {
        "name": "Phi-1.5 (1B)",
        "filename": "phi-1_5.Q4_K_M.gguf",
        "url": "https://huggingface.co/mradermacher/phi-1_5-GGUF/resolve/main/phi-1_5.Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 1.0,
        "filesize": 0.83
    },
    "falcon3_1b": {
        "name": "Falcon3 (1B)",
        "filename": "Falcon3-1B-Instruct-Heretic.i1-Q4_K_M.gguf",
        "url": "https://huggingface.co/mradermacher/Falcon3-1B-Instruct-Heretic-i1-GGUF/resolve/main/Falcon3-1B-Instruct-Heretic.i1-Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 1.0,
        "filesize": 0.98
    },
    "openllama_3_2_1b": {
        "name": "OpenLLaMA 3.2 (1B)",
        "filename": "open-llama-3.2-1B-Instruct.Q4_K_M.gguf",
        "url": "https://huggingface.co/mradermacher/open-llama-3.2-1B-Instruct-GGUF/resolve/main/open-llama-3.2-1B-Instruct.Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 1.0,
        "filesize": 0.89
    },
    "openelm_1_1b": {
        "name": "OpenELM (1.1B)",
        "filename": "OpenELM-1_1B-Instruct.Q4_K_M.gguf",
        "url": "https://huggingface.co/mradermacher/OpenELM-1_1B-Instruct-GGUF/resolve/main/OpenELM-1_1B-Instruct.Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 1.1,
        "filesize": 0.63
    },
    "tinyllama_1_1b": {
        "name": "TinyLlama (1.1B)",
        "filename": "tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf",
        "url": "https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 1.1,
        "filesize": 0.62
    },
    "cerebras_1_3b": {
        "name": "Cerebras-GPT (1.3B)",
        "filename": "Cerebras-GPT-1.3B-Alpaca-SP.Q4_K_M.gguf",
        "url": "https://huggingface.co/mradermacher/Cerebras-GPT-1.3B-Alpaca-SP-GGUF/resolve/main/Cerebras-GPT-1.3B-Alpaca-SP.Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 1.3,
        "filesize": 0.81
    },
    "gptneox_1_3b": {
        "name": "GPT-NeoX (1.3B)",
        "filename": "gpt-neox-1.3b-viet-final.q4_k_m.gguf",
        "url": "https://huggingface.co/afrideva/GPT-NeoX-1.3B-viet-final-GGUF/resolve/main/gpt-neox-1.3b-viet-final.q4_k_m.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 1.3,
        "filesize": 0.88
    },
    "olmo_2_1b": {
        "name": "OLMo-2 (1B)",
        "filename": "OLMo-2-0425-1B-Q4_K_M.gguf",
        "url": "https://huggingface.co/allenai/OLMo-2-0425-1B-GGUF/resolve/main/OLMo-2-0425-1B-Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 1.5,
        "filesize": 0.87
    },
    "deepseek_r1_1_5b": {
        "name": "DeepSeek R1 Distill (1.5B)",
        "filename": "DeepSeek-R1-Distill-Qwen-1.5B-Q4_K_M.gguf",
        "url": "https://huggingface.co/unsloth/DeepSeek-R1-Distill-Qwen-1.5B-GGUF/resolve/main/DeepSeek-R1-Distill-Qwen-1.5B-Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 1.5,
        "filesize": 1.04
    },
    "phi_3_mini_1_5b": {
        "name": "Phi-3 Mini (1.5B)",
        "filename": "phi-3-mini-1.5B-s-soft-distill.Q4_K_M.gguf",
        "url": "https://huggingface.co/mradermacher/phi-3-mini-1.5B-s-soft-distill-GGUF/resolve/main/phi-3-mini-1.5B-s-soft-distill.Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 1.5,
        "filesize": 0.93
    },
    "stablelm_1_6b": {
        "name": "StableLM-2 (1.6B)",
        "filename": "stablelm-2-zephyr-1_6b-Q4_K_M.gguf",
        "url": "https://huggingface.co/second-state/stablelm-2-zephyr-1.6b-GGUF/resolve/main/stablelm-2-zephyr-1_6b-Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 1.6,
        "filesize": 0.96
    },
    "qwen_1_5b": {
        "name": "Qwen 2.5 (1.5B)",
        "filename": "qwen2.5-1.5b-instruct-q4_k_m.gguf",
        "url": "https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct-GGUF/resolve/main/qwen2.5-1.5b-instruct-q4_k_m.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 1.8,
        "filesize": 1.04
    },

    # Medium Models (2B - 5B)
    "gemma_2b": {
        "name": "Gemma (2B)",
        "filename": "gemma-2b.Q4_K_M.gguf",
        "url": "https://huggingface.co/mradermacher/gemma-2b-GGUF/resolve/main/gemma-2b.Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 2.0,
        "filesize": 1.52
    },
    "phi_2": {
        "name": "Phi-2 (2.7B)",
        "filename": "phi-2.Q4_K_M.gguf",
        "url": "https://huggingface.co/TheBloke/phi-2-GGUF/resolve/main/phi-2.Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 2.7,
        "filesize": 1.67
    },
    "qwen_coder_3b": {
        "name": "Qwen 2.5 Coder (3B)",
        "filename": "qwen2.5-coder-3b-instruct-q4_k_m.gguf",
        "url": "https://huggingface.co/Qwen/Qwen2.5-Coder-3B-Instruct-GGUF/resolve/main/qwen2.5-coder-3b-instruct-q4_k_m.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 3.0,
        "filesize": 1.96
    },
    "ministral_3b": {
        "name": "Ministral (3B)",
        "filename": "Ministral-3-3B-Instruct-2512-Q4_K_M.gguf",
        "url": "https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512-GGUF/resolve/main/Ministral-3-3B-Instruct-2512-Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 3.0,
        "filesize": 2.00
    },
    "stablelm_3b": {
        "name": "StableLM (3B)",
        "filename": "stablelm-tuned-alpha-3b-16bit.Q4_K_M.gguf",
        "url": "https://huggingface.co/mradermacher/stablelm-tuned-alpha-3b-16bit-GGUF/resolve/main/stablelm-tuned-alpha-3b-16bit.Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 3.0,
        "filesize": 2.18
    },
    "falcon3_3b": {
        "name": "Falcon3 (3B)",
        "filename": "Falcon3-3B-Base.i1-Q4_K_M.gguf",
        "url": "https://huggingface.co/mradermacher/Falcon3-3B-Base-i1-GGUF/resolve/main/Falcon3-3B-Base.i1-Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 3.0,
        "filesize": 1.87
    },
    "openelm_3b": {
        "name": "OpenELM (3B)",
        "filename": "OpenELM-3B.Q4_K_M.gguf",
        "url": "https://huggingface.co/mradermacher/OpenELM-3B-GGUF/resolve/main/OpenELM-3B.Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 3.0,
        "filesize": 1.76
    },
    "openllama_3b": {
        "name": "OpenLLaMA (3B)",
        "filename": "open-llama-3b-v2-chat.Q4_K_M.gguf",
        "url": "https://huggingface.co/mradermacher/open-llama-3b-v2-chat-GGUF/resolve/main/open-llama-3b-v2-chat.Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 3.0,
        "filesize": 2.40
    },
    "gpt_5_distill_3b": {
        "name": "GPT-5 Distill (3B)",
        "filename": "GPT-5-Distill-llama3.2-3B-Instruct.Q4_K_M.gguf",
        "url": "https://huggingface.co/mradermacher/GPT-5-Distill-llama3.2-3B-Instruct-GGUF/resolve/main/GPT-5-Distill-llama3.2-3B-Instruct.Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 3.0,
        "filesize": 1.88
    },
    "pythia_3_8b": {
        "name": "Pythia (3.8B)",
        "filename": "boomerang-pythia-3.8B.Q4_K_M.gguf",
        "url": "https://huggingface.co/mradermacher/boomerang-pythia-3.8B-GGUF/resolve/main/boomerang-pythia-3.8B.Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 3.8,
        "filesize": 2.31
    },
    "qwen_4b": {
        "name": "Qwen3 (4B)",
        "filename": "Qwen3-4B-Thinking-2507-DeepSeek-v3.2-Speciale-Math-Distill.q4_k_m.gguf",
        "url": "https://huggingface.co/TeichAI/Qwen3-4B-Thinking-2507-DeepSeek-v3.2-Speciale-Math-Distill-GGUF/resolve/main/Qwen3-4B-Thinking-2507-DeepSeek-v3.2-Speciale-Math-Distill.q4_k_m.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 4.0,
        "filesize": 2.33
    },
    "gpt_oss_4b": {
        "name": "GPT-OSS (4B)",
        "filename": "gpt-oss-4B.Q4_K_M.gguf",
        "url": "https://huggingface.co/mradermacher/gpt-oss-4B-GGUF/resolve/main/gpt-oss-4B.Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 4.0,
        "filesize": 3.01
    },
    "gemma_3_4b": {
        "name": "Gemma 3 (4B)",
        "filename": "QiMing-Gemma-3-Socratic-4b.Q4_K_M.gguf",
        "url": "https://huggingface.co/mradermacher/QiMing-Gemma-3-Socratic-4b-GGUF/resolve/main/QiMing-Gemma-3-Socratic-4b.Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 4.0,
        "filesize": 2.32
    },
    "olmoe_1b_5b": {
        "name": "OLMoE (1B/5B)",
        "filename": "OLMoE-1B-5B.Q4_K_M.gguf",
        "url": "https://huggingface.co/mradermacher/OLMoE-1B-5B-GGUF/resolve/main/OLMoE-1B-5B.Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 5.0,
        "filesize": 2.56
    },

    # Large Models (6B - 8B)
    "gpt_oss_6b": {
        "name": "GPT-OSS (6B)",
        "filename": "gpt-oss-6.0b-specialized-all-pruned-moe-only-7-experts.Q4_K_M.gguf",
        "url": "https://huggingface.co/mradermacher/gpt-oss-6.0b-specialized-all-pruned-moe-only-7-experts-GGUF/resolve/main/gpt-oss-6.0b-specialized-all-pruned-moe-only-7-experts.Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 6.0,
        "filesize": 4.27
    },
    "phi_3_6b": {
        "name": "Phi-3 (6B)",
        "filename": "Phi-3-6b-4k-instruct.Q4_K_M.gguf",
        "url": "https://huggingface.co/mradermacher/Phi-3-6b-4k-instruct-GGUF/resolve/main/Phi-3-6b-4k-instruct.Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 6.0,
        "filesize": 4.63
    },
    "cerebras_opt_6_7b": {
        "name": "Cerebras-OPT (6.7B)",
        "filename": "Cerebras-OPT-Fusion.Q4_K_M.gguf",
        "url": "https://huggingface.co/mradermacher/Cerebras-OPT-Fusion-GGUF/resolve/main/Cerebras-OPT-Fusion.Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 6.7,
        "filesize": 4.63
    },
    "pythia_6_9b": {
        "name": "Pythia (6.9B)",
        "filename": "pythia-6.9b.Q4_K_M.gguf",
        "url": "https://huggingface.co/mradermacher/pythia-6.9b-GGUF/resolve/main/pythia-6.9b.Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 6.9,
        "filesize": 4.63
    },
    "llama_2_7b": {
        "name": "Llama 2 (7B)",
        "filename": "llama-2-7b.Q4_K_M.gguf",
        "url": "https://huggingface.co/TheBloke/Llama-2-7B-GGUF/resolve/main/llama-2-7b.Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 7.0,
        "filesize": 3.80
    },
    "gemma_7b": {
        "name": "Gemma (7B)",
        "filename": "gemma-7b-it.Q4_K_M.gguf",
        "url": "https://huggingface.co/mradermacher/gemma-7b-it-GGUF/resolve/main/gemma-7b-it.Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 7.0,
        "filesize": 4.96
    },
    "openllama_7b": {
        "name": "OpenLLaMA (7B)",
        "filename": "open-llama-7b-open-instruct.Q4_K_M.gguf",
        "url": "https://huggingface.co/mradermacher/open-llama-7b-open-instruct-GGUF/resolve/main/open-llama-7b-open-instruct.Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 7.0,    "ministral_3b": {
        "name": "Ministral (3B)",
        "filename": "Ministral-3-3B-Instruct-2512-Q4_K_M.gguf",
        "url": "https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512-GGUF/resolve/main/Ministral-3-3B-Instruct-2512-Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 3.0,
        "filesize": 2.00
    },
    "openllama_3b": {
        "name": "OpenLLaMA (3B)",
        "filename": "open-llama-3b-v2-chat.Q4_K_M.gguf",
        "url": "https://huggingface.co/mradermacher/open-llama-3b-v2-chat-GGUF/resolve/main/open-llama-3b-v2-chat.Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 3.0,
        "filesize": 2.40
    },
    "gpt_oss_6b": {
        "name": "GPT-OSS (6B)",
        "filename": "gpt-oss-6.0b-specialized-all-pruned-moe-only-7-experts.Q4_K_M.gguf",
        "url": "https://huggingface.co/mradermacher/gpt-oss-6.0b-specialized-all-pruned-moe-only-7-experts-GGUF/resolve/main/gpt-oss-6.0b-specialized-all-pruned-moe-only-7-experts.Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 6.0,
        "filesize": 4.27
    },
    "phi_3_6b": {
        "name": "Phi-3 (6B)",
        "filename": "Phi-3-6b-4k-instruct.Q4_K_M.gguf",
        "url": "https://huggingface.co/mradermacher/Phi-3-6b-4k-instruct-GGUF/resolve/main/Phi-3-6b-4k-instruct.Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 6.0,
        "filesize": 4.63
    }
        "filesize": 3.80
    },
    "olmo_3_7b": {
        "name": "OLMo-3 (7B)",
        "filename": "Olmo-3-7B-Instruct-Q4_K_M.gguf",
        "url": "https://huggingface.co/unsloth/Olmo-3-7B-Instruct-GGUF/resolve/main/Olmo-3-7B-Instruct-Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 7.0,
        "filesize": 4.16
    },
    "stablelm_7b": {
        "name": "StableLM (7B)",
        "filename": "stablelm-base-alpha-7b-sharded.Q4_K_M.gguf",
        "url": "https://huggingface.co/mradermacher/stablelm-base-alpha-7b-sharded-GGUF/resolve/main/stablelm-base-alpha-7b-sharded.Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 7.0,
        "filesize": 4.70
    },
    "redpajama_7b": {
        "name": "RedPajama (7B)",
        "filename": "redpajama-incite-7b-base.Q4_K_M.gguf",
        "url": "https://huggingface.co/mav23/RedPajama-INCITE-7B-Base-GGUF/resolve/main/redpajama-incite-7b-base.Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 7.0,
        "filesize": 4.09
    },
    "falcon_7b": {
        "name": "Falcon (7B)",
        "filename": "falcon-7b-instruct.Q4_K_M.gguf",
        "url": "https://huggingface.co/mradermacher/falcon-7b-instruct-GGUF/resolve/main/falcon-7b-instruct.Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 7.0,
        "filesize": 4.63
    },
    "deepseek_r1_8b_qwen": {
        "name": "DeepSeek R1 Qwen (8B)",
        "filename": "DeepSeek-R1-0528-Qwen3-8B-Q4_K_M.gguf",
        "url": "https://huggingface.co/unsloth/DeepSeek-R1-0528-Qwen3-8B-GGUF/resolve/main/DeepSeek-R1-0528-Qwen3-8B-Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 8.0,
        "filesize": 3.69
    },
    "ministral_8b": {
        "name": "Ministral (8B)",
        "filename": "Ministral-3-8B-Instruct-2512-Q4_K_M.gguf",
        "url": "https://huggingface.co/mistralai/Ministral-3-8B-Instruct-2512-GGUF/resolve/main/Ministral-3-8B-Instruct-2512-Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 8.0,
        "filesize": 4.84
    },
    "qwen3_8b": {
        "name": "Qwen3 (8B)",
        "filename": "Qwen3-8B-Q4_K_M.gguf",
        "url": "https://huggingface.co/Qwen/Qwen3-8B-GGUF/resolve/main/Qwen3-8B-Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 8.0,
        "filesize": 4.68
    },
    "qwen3_8b_claude": {
        "name": "Qwen3 Claude (8B)",
        "filename": "Qwen3-8B-claude-sonnet-4.5-high-reasoning-distill-Q4_K_M.gguf",
        "url": "https://huggingface.co/TeichAI/Qwen3-8B-Claude-Sonnet-4.5-Reasoning-Distill-GGUF/resolve/main/Qwen3-8B-claude-sonnet-4.5-high-reasoning-distill-Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 8.0,
        "filesize": 4.68
    },

    # Stress Models (> 9B)
    "gemma_2_9b": {
        "name": "Gemma 2 (9B)",
        "filename": "gemma-2-9b.Q4_K_M.gguf",
        "url": "https://huggingface.co/mradermacher/gemma-2-9b-GGUF/resolve/main/gemma-2-9b.Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 9.0,
        "filesize": 5.37
    },
    "deepseek_math_10b": {
        "name": "DeepSeek Math (10.8B)",
        "filename": "deepseek-math-10.8b-rl.Q4_K_M.gguf",
        "url": "https://huggingface.co/mradermacher/deepseek-math-10.8b-rl-GGUF/resolve/main/deepseek-math-10.8b-rl.Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 10.8,
        "filesize": 6.11
    },
    "falcon_11b": {
        "name": "Falcon (11B)",
        "filename": "Q4_K_M-00001-of-00001.gguf",
        "url": "https://huggingface.co/LiteLLMs/falcon-11B-GGUF/resolve/main/Q4_K_M/Q4_K_M-00001-of-00001.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 11.0,
        "filesize": 6.38
    },
    "pythia_12b": {
        "name": "Pythia (12B)",
        "filename": "pythia-12b.Q4_K_M.gguf",
        "url": "https://huggingface.co/mradermacher/pythia-12b-GGUF/resolve/main/pythia-12b.Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 12.0,
        "filesize": 7.06
    },
    "stablelm_12b": {
        "name": "StableLM-2 (12B)",
        "filename": "stablelm-2-12b.Q4_K_M.gguf",
        "url": "https://huggingface.co/mradermacher/stablelm-2-12b-GGUF/resolve/main/stablelm-2-12b.Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 12.0,
        "filesize": 6.86
    },
    "openllama_13b": {
        "name": "OpenLLaMA (13B)",
        "filename": "open-llama-13b-open-instruct.Q4_K_M.gguf",
        "url": "https://huggingface.co/mradermacher/open-llama-13b-open-instruct-GGUF/resolve/main/open-llama-13b-open-instruct.Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 13.0,
        "filesize": 7.33
    },
    "llama_2_13b": {
        "name": "Llama 2 (13B)",
        "filename": "llama-2-13b.Q4_K_M.gguf",
        "url": "https://huggingface.co/TheBloke/Llama-2-13B-GGUF/resolve/main/llama-2-13b.Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 13.0,
        "filesize": 7.33
    },
    "phi_3_medium": {
        "name": "Phi-3 Medium (14B)",
        "filename": "phi-3-medium-128k-instruct.Q4_K_M.gguf",
        "url": "https://huggingface.co/ssmits/Phi-3-medium-128k-instruct-Q4_K_M-GGUF/resolve/main/phi-3-medium-128k-instruct.Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 14.0,
        "filesize": 7.98
    },
    "qwen_14b": {
        "name": "Qwen 2.5 (14B)",
        "filename": "Qwen2.5-14B-Instruct-Q4_K_M.gguf",
        "url": "https://huggingface.co/bartowski/Qwen2.5-14B-Instruct-GGUF/resolve/main/Qwen2.5-14B-Instruct-Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 14.0,
        "filesize": 8.37
    },
    "starcoder2_15b": {
        "name": "StarCoder2 (16B)",
        "filename": "Q4_K_M-00001-of-00001.gguf",
        "url": "https://huggingface.co/LiteLLMs/starcoder2-15b-instruct-v0.1-GGUF/resolve/main/Q4_K_M/Q4_K_M-00001-of-00001.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 16.0,
        "filesize": 9.18
    },
    "lambda_17b": {
        "name": "Lambda (17B)",
        "filename": "Lambda-17b.Q4_K_M.gguf",
        "url": "https://huggingface.co/mradermacher/Lambda-17b-GGUF/resolve/main/Lambda-17b.Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 17.0,
        "filesize": 9.57
    },
    "mistral_18b": {
        "name": "Mistral (18B)",
        "filename": "mistral_18B_v0.1.Q4_K_M.gguf",
        "url": "https://huggingface.co/mradermacher/mistral_18B_v0.1-GGUF/resolve/main/mistral_18B_v0.1.Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 18.0,
        "filesize": 10.08
    },
    "cothuginn_19b": {
        "name": "COTHuginn (19B)",
        "filename": "cothuginn-4.5-19b.Q4_K_M.gguf",
        "url": "https://huggingface.co/TheBloke/COTHuginn-4.5-19B-GGUF/resolve/main/cothuginn-4.5-19b.Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 19.0,
        "filesize": 10.88
    },
    "rose_20b": {
        "name": "Rose (20B)",
        "filename": "rose-20b.Q4_K_M.gguf",
        "url": "https://huggingface.co/TheBloke/Rose-20B-GGUF/resolve/main/rose-20b.Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 20.0,
        "filesize": 11.22
    },
    "ms_darker_sun_22b": {
        "name": "MS Darker Sun (22B)",
        "filename": "MS-Darker_Sun_v1b_22B.Q4_K_M.gguf",
        "url": "https://huggingface.co/mradermacher/MS-Darker_Sun_v1b_22B-GGUF/resolve/main/MS-Darker_Sun_v1b_22B.Q4_K_M.gguf?download=true",
        "prompt_template": "{prompt}",
        "size": 22.0,
        "filesize": 12.43
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
