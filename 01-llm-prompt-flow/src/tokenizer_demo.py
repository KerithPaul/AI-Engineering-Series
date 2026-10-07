import tiktoken

text = "Explain how a large language model processes a prompt."

encoding = tiktoken.get_encoding("cl100k_base")
tokens = encoding.encode(text)

print("Text:")
print(text)

print("\nApproximate token IDs:")
print(tokens)

print("\nApproximate token count:")
print(len(tokens))