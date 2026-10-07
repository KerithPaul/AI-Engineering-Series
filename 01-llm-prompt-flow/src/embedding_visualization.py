# src/embedding_visualization.py

from pathlib import Path

import matplotlib.pyplot as plt
from sentence_transformers import SentenceTransformer
from sklearn.decomposition import PCA


def main() -> None:
    texts = [
        "What is machine learning?",
        "How does artificial intelligence work?",
        "What is deep learning?",
        "How do neural networks learn?",
        "What is a pizza recipe?",
        "How do I make pasta?",
    ]

    # Convert text into embedding vectors.
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(texts)

    # Reduce high-dimensional embeddings to 2 dimensions
    # so that we can visualize them.
    pca = PCA(n_components=2)
    points = pca.fit_transform(embeddings)

    plt.figure(figsize=(10, 7))

    for i, text in enumerate(texts):
        x, y = points[i]

        plt.scatter(x, y)
        plt.annotate(
            text,
            (x, y),
            xytext=(8, 8),
            textcoords="offset points",
            fontsize=9,
        )

    plt.title("Text Embeddings Visualized in 2D")
    plt.xlabel("Principal Component 1")
    plt.ylabel("Principal Component 2")
    plt.grid(alpha=0.2)

    output_path = (
        Path(__file__).resolve().parents[1]
        / "outputs"
        / "embedding-visualization.png"
    )

    plt.tight_layout()
    plt.savefig(output_path, dpi=200)
    plt.show()

    print(f"Saved visualization to: {output_path}")


if __name__ == "__main__":
    main()