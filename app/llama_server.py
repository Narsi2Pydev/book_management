from flask import Flask, request, jsonify
import torch
from transformers import LlamaForCausalLM, LlamaTokenizer

app = Flask(__name__)

# Load the Llama model and tokenizer
model_name = "Llama3-model-directory"  # Path to locally stored Llama model
device = "cuda" if torch.cuda.is_available() else "cpu"

print(f"Loading model {model_name} on {device}...")
tokenizer = LlamaTokenizer.from_pretrained(model_name)
model = LlamaForCausalLM.from_pretrained(model_name)
model.to(device)
print(f"Model loaded successfully on {device}.")


def generate_summary(text, max_length=200):
    """Generate a summary for the given text using Llama3."""
    inputs = tokenizer.encode(text, return_tensors="pt").to(device)

    # Generate output from the model
    summary_ids = model.generate(inputs, max_length=max_length, num_beams=4, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary


@app.route('/generate_summary', methods=['POST'])
def generate_summary_api():
    """API route to generate a book summary."""
    data = request.get_json()

    if 'content' not in data:
        return jsonify({"error": "Book content is required"}), 400

    book_content = data['content']

    try:
        # Generate summary using the Llama3 model
        summary = generate_summary(book_content)
        return jsonify({"summary": summary}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
