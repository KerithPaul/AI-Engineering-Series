import tiktoken


def main():
    encoding = tiktoken.get_encoding("cl100k_base")

    text = "Build a RAG system for legal documents."
    token_ids = encoding.encode(text)

    print("=" * 60)
    print("TEXT TO TOKENS")
    print("=" * 60)

    print(f"\nOriginal text:\n{text}")
    print("\nNumber of tokens:")
    print(len(token_ids))
    print("\nToken IDs:")
    print(token_ids)

    print("\nToken pieces:")
    for token_id in token_ids:
        token_bytes = encoding.decode_single_token_bytes(token_id)
        token = token_bytes.decode("utf-8", errors="replace")
        print(f"{token_id:>6} -> {repr(token)}")


if __name__ == "__main__":
    main()
