# AI Engineering Series #02 — Tokens

> Tokens: The hidden unit behind LLM cost and context.

This repository contains the hands-on code for Post #02 of the AI Engineering Series.

## What you will learn

- What tokens are
- How text is tokenized
- What token IDs are
- Why words and tokens are different
- How token count affects context usage
- How token-based chunking works
- Why tokens matter in RAG systems

## Project Structure

```text
post-02-tokens/
├── README.md
├── requirements.txt
├── 01_tokenization/
│   └── tokenizer_demo.py
├── 02_token_ids/
│   └── token_ids_demo.py
├── 03_token_comparison/
│   └── token_comparison.py
├── 04_context_window/
│   └── context_window.py
└── 05_token_chunking/
    └── chunking_demo.py
```

## Installation

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Experiments

### 01 — Tokenization

```bash
python 01_tokenization/tokenizer_demo.py
```

Learn:

```text
Text
 ↓
Tokenizer
 ↓
Tokens
```

### 02 — Token IDs

```bash
python 02_token_ids/token_ids_demo.py
```

Learn:

```text
Token
 ↓
Token ID
```

Models operate on numerical representations rather than raw text.

### 03 — Token Comparison

```bash
python 03_token_comparison/token_comparison.py
```

Compare characters, words, and tokens.

Important: a word is not necessarily one token.

### 04 — Context Window

```bash
python 04_context_window/context_window.py
```

Understand how token count relates to the available context window.

A request can contain:
- System instructions
- User prompt
- Conversation history
- Retrieved context
- Model output

All of these consume tokens.

### 05 — Token Chunking

```bash
python 05_token_chunking/chunking_demo.py
```

This demonstrates simple token-based chunking, which becomes important for RAG and long-document processing.

## Key Takeaways

1. LLMs process tokens rather than raw text.
2. Tokens can be words, subwords, punctuation, or other pieces of text.
3. Tokens are mapped to token IDs.
4. Token count affects how much information fits into a model's context.
5. Token count can affect LLM usage cost.
6. Long documents often need chunking and retrieval strategies.
7. Tokenization is tokenizer/model dependent.

## Important

This project uses `cl100k_base` as an educational example.

Different models can use different tokenizers, so token counts are not universal.

Pricing and context limits are also model/provider specific.
