from transformers import pipeline

spin_model = pipeline("text-generation", model="distilgpt2")
review_model = pipeline("text-generation", model="distilgpt2")

def ai_spin(text: str) -> str:
    snippet = text[:1000]
    return spin_model(snippet, max_length=800, do_sample=True)[0]["generated_text"]

def ai_review(text: str) -> str:
    prompt = f"Improve clarity and flow:\n{text}"
    return review_model(prompt, max_length=800)[0]["generated_text"]
