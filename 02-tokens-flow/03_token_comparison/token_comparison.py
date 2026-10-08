import tiktoken


def main():
    encoding = tiktoken.get_encoding("cl100k_base")

    examples = [
        "Hello world!",
        "unbelievable",
        "ChatGPT is amazing.",
        "Build a RAG system.",
        "Machine learning",
        "भारत एक देश है।",
        "🤖",
    ]

    print("=" * 60)
    print("TOKEN COUNT COMPARISON")
    print("=" * 60)

    for text in examples:
        tokens = encoding.encode(text)

        print("\nText:")
        print(text)
        print(f"Characters : {len(text)}")
        print(f"Words      : {len(text.split())}")
        print(f"Tokens     : {len(tokens)}")
        print(f"Token IDs  : {tokens}")


if __name__ == "__main__":
    main()
