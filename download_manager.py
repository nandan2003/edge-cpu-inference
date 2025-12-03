import os
import requests
from tqdm import tqdm
from models_config import MODELS_DIR, MODEL_REGISTRY

def download_file(url, filename):
    path = os.path.join(MODELS_DIR, filename)
    if os.path.exists(path):
        print(f"✅ Found {filename}")
        return

    print(f"⬇️  Downloading {filename}...")
    try:
        response = requests.get(url, stream=True)
        total_size = int(response.headers.get('content-length', 0))
        block_size = 1024 * 1024  # 1MB

        with open(path, 'wb') as file, tqdm(
            desc=filename,
            total=total_size,
            unit='iB',
            unit_scale=True,
            unit_divisor=1024,
        ) as bar:
            for data in response.iter_content(block_size):
                file.write(data)
                bar.update(len(data))
        print("   Success.")
    except Exception as e:
        print(f"❌ Error downloading {filename}: {e}")
        if os.path.exists(path):
            os.remove(path)

if __name__ == "__main__":
    if not os.path.exists(MODELS_DIR):
        os.makedirs(MODELS_DIR)
    
    print(f"=== INITIALIZING MODEL REGISTRY ({len(MODEL_REGISTRY)} Models) ===")
    for key, meta in MODEL_REGISTRY.items():
        download_file(meta["url"], meta["filename"])
