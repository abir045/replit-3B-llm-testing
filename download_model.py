import os
import requests
from huggingface_hub import hf_hub_download


def download_config(config_file: str, destination_folder: str):
    config = requests.get(config_file).text
    with open(f"{destination_folder}/config.json", "w") as f:
        f.write(config)


def download_replit_quant(destination_folder: str, repo_id: str, model_filename: str):
    local_path = os.path.abspath(destination_folder)
    return hf_hub_download(
        repo_id=repo_id,
        filename=model_filename,
        local_dir=local_path,
        local_dir_use_symlinks=True,
    )


if __name__ == "__main__":
    """full url: https://huggingface.co/abacaj/Replit-v2-CodeInstruct-3B-ggml/blob/main/replit-v2-codeinstruct-3b.q4_1.bin"""

    repo_id = "abacaj/Replit-v2-CodeInstruct-3B-ggml"
    model_filename = "replit-v2-codeinstruct-3b.q4_1.bin"
    destination_folder = "models"
    config_file = (
        "https://huggingface.co/teknium/Replit-v2-CodeInstruct-3B/raw/main/config.json"
    )

    download_replit_quant(destination_folder, repo_id, model_filename)
    download_config(config_file, destination_folder)
