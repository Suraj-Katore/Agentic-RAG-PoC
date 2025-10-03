from openai import OpenAI

client = OpenAI(api_key="1ICfm7h6TcUzTTZ9hrJGn8hugqYLBzfAgLXHo5fFkLZnnKf3lXKZJQQJ99BHACHYHv6XJ3w3AAABACOGYHE9")

prompt = "Write a short creative sentence about the moon."

# Set temperature = 0
response_deterministic = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    temperature=0  
)
print("Deterministic:", response_deterministic.choices[0].message.content)

for i in range(3):
    response_random = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8
    )

    print(f"Random {i+1}:", response_random.choices[0].message.content)
