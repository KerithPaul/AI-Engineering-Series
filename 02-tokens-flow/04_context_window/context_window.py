import tiktoken


def calculate_context_usage(text, context_window, encoding):
    token_count = len(encoding.encode(text))
    remaining = context_window - token_count
    usage_percentage = (token_count / context_window) * 100
    return token_count, remaining, usage_percentage


def main():
    encoding = tiktoken.get_encoding("cl100k_base")

    text = """
    You are an AI engineer building a Retrieval
    Augmented Generation system for legal documents.

    The system retrieves relevant legal information
    from a knowledge base and provides that information
    to a language model as context.

    The model then generates a grounded response
    using the retrieved information.
    """

    context_window = 8192

    token_count, remaining, usage_percentage = calculate_context_usage(
        text, context_window, encoding
    )

    print("=" * 60)
    print("CONTEXT WINDOW")
    print("=" * 60)

    print(f"\nContext window : {context_window:,} tokens")
    print(f"Used tokens    : {token_count:,}")
    print(f"Remaining      : {remaining:,}")
    print(f"Usage          : {usage_percentage:.2f}%")

    print("\nContext usage:")
    bar_length = 40
    filled = min(int((usage_percentage / 100) * bar_length), bar_length)
    bar = "█" * filled + "░" * (bar_length - filled)
    print(f"[{bar}]")


if __name__ == "__main__":
    main()
