setup-python:
	pip install -r requirements.txt

setup-model:
	mkdir models
	cd models
	curl -L https://huggingface.co/cjpais/llava-v1.6-vicuna-7b-gguf/resolve/main/llava-v1.6-vicuna-7b.Q3_K_M.gguf -o llava-v1.6-vicuna-7b.Q3_K_M.gguf