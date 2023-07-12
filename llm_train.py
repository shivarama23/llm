import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig


model_name = "EleutherAI/gpt-neox-20b"
#Tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)
