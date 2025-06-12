from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load once at module level for reuse
MODEL_NAME = "sshleifer/distilbart-cnn-12-6"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

def summarize_text(text: str, min_length: int = 30, max_length: int = 130) -> str:
    if not text.strip():
        raise ValueError("Input text is empty")
    # Tokenize input text
    inputs = tokenizer.encode(text, return_tensors="pt", truncation=True, max_length=1024)

    # Generate summary
    summary_ids = model.generate(
        inputs,
        num_beams=4,
        min_length=min_length,
        max_length=max_length,
        early_stopiing=True
    )

    # Decode output
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary