# AI Engineering Series

A practical, implementation-first journey through modern AI Engineering.

This repository contains the code, experiments, visualizations, and supporting material for my AI Engineering content series.

The goal is simple:

> **Don't just learn AI concepts. Build them, experiment with them, and understand how they work in real systems.**

---

## Why This Repository Exists

A lot of AI learning follows this pattern:

```text
Learn a concept
    ↓
Watch a tutorial
    ↓
Read documentation
    ↓
Move to the next concept
```

This series takes a different approach:

```text
Understand
    ↓
Implement
    ↓
Experiment
    ↓
Measure
    ↓
Explain
    ↓
Document
```

Every topic in the series is therefore accompanied by a small practical implementation.

The objective isn't to build unnecessarily large projects.

The objective is to isolate an important AI Engineering concept and understand it deeply enough to implement and explain it.

---

# Repository Structure

Each topic lives in its own directory.

```text
ai-engineering-series/
│
├── README.md
│
├── 01-llm-prompt-flow/
│   ├── README.md
│   ├── POST-01.md
│   ├── requirements.txt
│   ├── .env.example
│   │
│   ├── src/
│   │   ├── prompt_flow.py
│   │   └── tokenizer_demo.py
│   │
│   └── outputs/
│       ├── post-01-explainer.png
│       └── post-01-hands-on-task.png
│
├── 02-tokenization-context/
│   └── ...
│
├── 03-context-engineering/
│   └── ...
│
└── ...
```

Each project is designed to be as independent as possible.

This makes it possible to explore one topic without having to understand the entire repository first.

---

# Design Philosophy

## 1. One Topic at a Time

Each project should have a clear learning objective.

For example:

```text
01
↓
What happens when a prompt is sent to an LLM?
```

rather than combining:

```text
Prompt Flow
+ RAG
+ Agents
+ Vector DB
+ Streaming
+ Evaluation
```

The projects intentionally avoid unnecessary complexity.

---

## 2. Code Should Demonstrate the Concept

The implementation should answer:

> "Can I prove that I understand this concept by writing code?"

If the answer is no, the topic probably needs a better practical experiment.

---

## 3. Measure Whenever Possible

Where appropriate, experiments should collect real observations.

For example:

```text
Input
↓
Processing
↓
Output
↓
Measurement
```

Measurements may include things such as:

- token counts
- latency
- retrieval scores
- similarity scores
- accuracy
- precision / recall
- context size
- memory usage
- throughput
- evaluation metrics

The exact measurements depend on the topic.

---

## 4. Prefer Small Experiments Over Large Demos

A 50-line experiment that clearly demonstrates one concept is often more valuable than a 1,000-line application that hides the concept behind abstractions.

The goal is:

```text
Small
+
Understandable
+
Reproducible
+
Measurable
```

---

# Technology Approach

The technology used in each project will depend on the concept being demonstrated.

Potential technologies include:

### LLMs

- Groq
- Local LLMs
- Open-source models
- Other inference providers where appropriate

### Python

Python is the primary language for the practical implementations.

### AI / ML

- PyTorch
- Transformers
- Sentence Transformers
- scikit-learn

### LLM Systems

- LangChain
- LangGraph
- RAG pipelines
- Vector databases
- Agent frameworks

### Infrastructure

Where relevant:

- Docker
- Kubernetes
- Redis
- databases
- observability tools
- MLOps tooling

Tools will only be introduced when they are relevant to the concept being demonstrated.

---

# Project Standards

Every project should aim to contain:

```text
README.md
    ↓
What is the concept?
Why does it matter?
How does the implementation work?
How do I run it?

Code
    ↓
Small, readable implementation

Experiment
    ↓
Something measurable or observable

Documentation
    ↓
What did the experiment demonstrate?
```

Not every project needs exactly the same files.

The structure should follow the learning objective rather than forcing every topic into the same template.

---

# Running a Project

Each project contains its own setup instructions.

For example:

```bash
cd 01-llm-prompt-flow
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it.

Windows:

```powershell
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Then install the dependencies specified by that project:

```bash
pip install -r requirements.txt
```

Follow the project's `README.md` for the remaining steps.

---

# Configuration & Secrets

API keys and credentials should **never** be committed to this repository.

Projects that require credentials will generally provide:

```text
.env.example
```

Copy it to:

```text
.env
```

and add your local credentials.

The repository's `.gitignore` should prevent secrets from being committed.

---

# How the Series Connects

The topics are designed to build on each other.

A simplified progression looks like:

```text
LLM Fundamentals
       │
       ▼
Tokenization
       │
       ▼
Context
       │
       ▼
Embeddings
       │
       ▼
Vector Search
       │
       ▼
RAG
       │
       ▼
RAG Evaluation
       │
       ▼
LLM Optimization
       │
       ├── Caching
       ├── KV Cache
       └── Context Optimization
       │
       ▼
Tool Calling
       │
       ▼
Agents
       │
       ▼
Agent Memory
       │
       ▼
Multi-Agent Systems
       │
       ▼
Observability & Evaluation
       │
       ▼
Deployment & MLOps
```

The purpose is not to memorize isolated technologies.

It is to understand how these pieces fit together when building production AI systems.

---

# What I Am Trying to Build Through This Series

The long-term objective is to develop a strong mental model of modern AI systems.

Not just:

> "How do I call an LLM API?"

But:

> "How do I design, build, evaluate, optimize, deploy, and operate reliable AI systems?"

That means progressively understanding the entire stack:

```text
                    AI APPLICATION
                         │
          ┌──────────────┼──────────────┐
          │              │              │
       Prompts         RAG          Agents
          │              │              │
          └──────────────┼──────────────┘
                         │
                    LLM Inference
                         │
              ┌──────────┴──────────┐
              │                     │
          Optimization         Evaluation
              │                     │
              └──────────┬──────────┘
                         │
                   Infrastructure
                         │
                       MLOps
```

---

# Content + Code

This repository is also connected to a public content series.

Each major topic can have:

```text
LinkedIn Post
      │
      ├── Explanation
      │
      ├── Visual
      │
      └── Practical Task
              │
              ▼
         GitHub Project
```

The LinkedIn post explains the concept.

The GitHub project demonstrates it.

The practical experiment provides evidence that the concept was actually implemented.

---

# Current Project

## 01 — LLM Prompt Flow

The first project focuses on the basic interaction between an application and an LLM.

```text
User Input
    ↓
Text
    ↓
Tokenization
    ↓
LLM Request
    ↓
Model Inference
    ↓
Generated Response
```

The implementation uses Python and the Groq API.

It intentionally remains small.

The purpose is to establish the mental model before moving into more complex topics.

See:

```text
01-llm-prompt-flow/
```

for the implementation and experiment.

---

# Learning Principle

The series follows one rule:

```text
Don't just consume AI content.

Build the concept.
Break it.
Measure it.
Understand it.
Explain it.
```

That is the difference between knowing an AI buzzword and being able to engineer an AI system.

---

# Progress

This repository will evolve continuously as new topics are implemented.

### Current

- [x] Repository structure
- [x] Post-01 — LLM Prompt Flow
- [ ] Post-02
- [ ] Post-03
- [ ] Post-04
- [ ] More AI Engineering topics

---

## Follow the Series

This repository accompanies the AI Engineering content series.

New topics, experiments, and implementations will be added progressively.

**Learn → Build → Measure → Explain**