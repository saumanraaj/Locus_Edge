import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Path to the locally saved fine-tuned model
local_model_path = "/Users/saumanraaj/models/local_model"  # Replace with your model path

# Check for GPU availability
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load the tokenizer and model
print("Loading model and tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(local_model_path)
model = AutoModelForCausalLM.from_pretrained(local_model_path, torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32)
model = model.to(device)

# Test prompt
test_prompt = "Move forward by 2 meters."

# Tokenize input
print("Tokenizing input...")
inputs = tokenizer(test_prompt, return_tensors="pt").to(device)

# Generate output
print("Generating output...")
with torch.no_grad():  # Ensure faster inference
    output_tokens = model.generate(
        **inputs,
        max_length=50,  # Adjust based on desired output length
        temperature=0.7,  # Adjust for randomness (lower for more focused output)
        top_k=50,  # Top-k sampling for diverse results
        top_p=0.9,  # Nucleus sampling for diverse results
        do_sample=True  # Enable sampling for creative output
    )

# Decode the output
output_text = tokenizer.decode(output_tokens[0], skip_special_tokens=True)
print("Generated Output:", output_text)

