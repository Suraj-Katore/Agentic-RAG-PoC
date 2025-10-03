from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

prompt = "AI will transform the future because"
result = generator(prompt, max_length=50, num_return_sequences=1)

print("Generated Text:\n", result[0]['generated_text'])