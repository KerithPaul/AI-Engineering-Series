import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

prompt = """
Explain what happens when a user sends a prompt
to a large language model.
"""

response = client.chat.completions.create(
    model=os.getenv("GROQ_MODEL"),
    messages=[
        {"role": "user", "content": prompt}
    ],
)

print("PROMPT:")
print(prompt)

print("\nRESPONSE:")
print(response.choices[0].message.content)