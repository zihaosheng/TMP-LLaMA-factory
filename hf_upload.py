from huggingface_hub import login, upload_folder

# (optional) Login with your Hugging Face credentials
login()

# Push your model files
upload_folder(folder_path="/data/TMP_LLM/Qwen2.5-7B-Instruct-1M_sft_2025-04-04", 
repo_id="zihaosheng/TMP-Qwen2.5-7B-Instruct-1M_sft_2025-04-04", repo_type="model")
