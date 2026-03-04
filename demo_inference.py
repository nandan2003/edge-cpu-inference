import sys
import time
from llama_cpp import Llama
from models_config import get_model_path, MODEL_REGISTRY


def run_chat():
    # 1. Configuration
    MODEL_KEY = "tinyllama_15m"

    # 2. Check Registry
    if MODEL_KEY not in MODEL_REGISTRY:
        print(f"Error: Model '{MODEL_KEY}' not found.")
        return

    print(f"=== Chatting with: {MODEL_REGISTRY[MODEL_KEY]['name']} ===")

    # 3. Load Model
    try:
        path = get_model_path(MODEL_KEY)
        print(f"Loading from: {path}")
        # n_ctx=2048 to allow some history
        llm = Llama(model_path=path, n_ctx=2048, n_threads=4, verbose=False)
    except Exception as e:
        print(f"Error loading model: {e}")
        return

    print("\nModel Loaded! Type 'exit' or 'quit' to stop.\n")

    # 4. Chat Loop
    history = ""

    while True:
        try:
            user_input = input("\nUser: ")
            if user_input.lower() in ["exit", "quit"]:
                break
        except EOFError:
            break

        # Simple prompt format for raw completion models
        # (This model is tiny, so expect random-ish output, but the format helps)
        prompt = f"{history}User: {user_input}\nAI:"

        print("AI: ", end="", flush=True)

        # Stream response
        stream = llm(
            prompt, max_tokens=128, stop=["User:", "\nUser"], echo=False, stream=True
        )

        response_text = ""
        for output in stream:
            token = output["choices"][0]["text"]
            print(token, end="", flush=True)
            response_text += token

        # Update history (keep it short-ish effectively)
        history += f"User: {user_input}\nAI:{response_text}\n"

    print("\nBye!")


if __name__ == "__main__":
    run_chat()
