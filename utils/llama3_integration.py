import requests
import aiohttp
from transformers import LlamaForCausalLM, LlamaTokenizer

async def generate_book_summary(title, author, genre):
    async with aiohttp.ClientSession() as session:
        async with session.post('http://localhost:5000/generate-summary', json={
            'title': title,
            'author': author,
            'genre': genre
        }) as response:
            response_json = await response.json()
            return response_json.get('summary')

async def generate_review_summary(reviews_text):
    async with aiohttp.ClientSession() as session:
        async with session.post('http://localhost:5000/generate-review-summary', json={
            'reviews_text': reviews_text
        }) as response:
            response_json = await response.json()
            return response_json.get('summary')


async def generate_summary(book_text):

    # Load the tokenizer and the model
    tokenizer = LlamaTokenizer.from_pretrained("meta-llama/Llama-2-7b")
    model = LlamaForCausalLM.from_pretrained("meta-llama/Llama-2-7b", device_map="auto")
    # Preprocess the text
    inputs = tokenizer(book_text, return_tensors="pt", truncation=True, max_length=512)

    # Generate a summary using the model
    summary_ids = model.generate(inputs["input_ids"], max_length=150, num_beams=5, early_stopping=True)

    # Decode the generated summary into text
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return summary


async def test_summary():
    book_text = """
    In a hole in the ground there lived a hobbit. Not a nasty, dirty, wet hole, filled with the ends of worms and an oozy smell, 
    nor yet a dry, bare, sandy hole with nothing in it to sit down on or to eat: it was a hobbit-hole, and that means comfort.
    """
    # Generate the summary
    summary = generate_summary(book_text)
    print("Summary:", summary)