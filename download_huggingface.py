from huggingface_hub import hf_hub_download

hf_hub_download(repo_id="openai/clip-vit-base-patch16", 
                filename="config.json", 
                cache_dir="./clip-model/openai/clip-vit-base-patch16")