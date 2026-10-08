import tiktoken


def main():
    encoding = tiktoken.get_encoding("cl100k_base")
    text = "Build a RAG system"
    token_ids = encoding.encode(text)

    print("=" * 60)
    print("TOKEN IDs")
    print("=" * 60)

    print(f"\nText:\n{text}")
    print("\nToken → Token ID")
    print("-" * 40)

    for token_id in token_ids:
        token_bytes = encoding.decode_single_token_bytes(token_id)
        token = token_bytes.decode("utf-8", errors="replace")
        print(f"{repr(token):<15} → {token_id}")

    print("\nImportant:")
    print("Models operate on numerical token IDs,")
    print("not directly on human-readable text.")


if __name__ == "__main__":
    main()
