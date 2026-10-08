import tiktoken


def chunk_text(text, encoding, chunk_size=50, overlap=10):
    """Split text into token-based chunks."""
    token_ids = encoding.encode(text)
    chunks = []
    start = 0

    while start < len(token_ids):
        end = start + chunk_size
        chunk_token_ids = token_ids[start:end]
        chunks.append(encoding.decode(chunk_token_ids))

        if end >= len(token_ids):
            break

        start = end - overlap

    return chunks


def main():
    encoding = tiktoken.get_encoding("cl100k_base")

    document = """
    Retrieval Augmented Generation combines
    information retrieval with language generation.

    A user sends a query to the system.

    The query is converted into an embedding
    and compared with documents stored in a
    vector database.

    The most relevant documents are retrieved.

    Those documents are then added to the
    model context.

    The language model uses the retrieved
    context to generate a grounded response.

    This approach is useful when an application
    needs to answer questions using an external
    knowledge base.
    """

    chunks = chunk_text(document, encoding, chunk_size=30, overlap=5)

    print("=" * 60)
    print("TOKEN-BASED CHUNKING")
    print("=" * 60)

    for index, chunk in enumerate(chunks, start=1):
        token_count = len(encoding.encode(chunk))

        print(f"\nCHUNK {index}")
        print("-" * 40)
        print(chunk.strip())
        print(f"\nToken count: {token_count}")


if __name__ == "__main__":
    main()
