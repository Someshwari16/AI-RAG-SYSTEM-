# AI-RAG-System

# Retrieval-Augmented Generation (RAG) System using Semantic Search

## Overview

This project demonstrates the basic implementation of a Retrieval-Augmented Generation (RAG) system using semantic search and sentence embeddings.

The main objective of this project is to understand how modern AI systems retrieve relevant information from documents using embeddings and similarity matching techniques.

Instead of performing traditional keyword-based search, this system performs semantic search by understanding the meaning of sentences.

The project converts both documents and user queries into numerical vector representations called embeddings and compares them using cosine similarity to retrieve the most relevant information.



# What is RAG?

RAG stands for:

Retrieval-Augmented Generation
# How Embeddings Work Internally

## Understanding Embeddings

Embeddings are numerical vector representations of words or sentences.

Computers cannot directly understand human language. Therefore, AI models convert text into mathematical values so that machines can process semantic meaning.

Example:


"Artificial Intelligence"
↓
[0.21, -0.44, 0.87, 0.13, ...]


The generated numbers are called vectors or embeddings.



# Why Convert Sentences into Numbers?

Computers only understand numerical operations.

To compare meanings between sentences, the text must first be converted into mathematical form.

For example:

Sentence 1:
"AI helps prediction"

Sentence 2:
"Machine learning improves forecasting"

Even though the words are different, their meanings are similar.

Embedding models convert both sentences into vectors positioned close together in vector space.

# How Embedding Models Work

This project uses:

SentenceTransformer('all-MiniLM-L6-v2')

This is a pre-trained transformer-based neural network model.

The model has already learned language patterns from massive text datasets.

It learns:
- word relationships
- sentence meanings
- contextual understanding
- semantic similarity

# Internal Working of Embedding Generation

## Step 1: Tokenization

The sentence is first broken into smaller units called tokens.

Example:

"Artificial Intelligence is powerful"

becomes:

["Artificial", "Intelligence", "is", "powerful"]

Each token is processed separately.

# Step 2: Token IDs

Each token is mapped to a unique numerical ID from the model vocabulary.

Example:

"Artificial" → 3451
"Intelligence" → 7821
"is" → 2003
"powerful" → 3928


These IDs are not random. They correspond to learned vocabulary entries inside the neural network.
# Step 3: Initial Word Embeddings

Each token ID is converted into an initial embedding vector.

Example:
"Artificial"
↓
[0.12, 0.45, -0.21, ...]
"Intelligence"
↓
[0.67, -0.11, 0.92, ...]

These vectors contain learned semantic information.

Words with similar meanings produce similar vector patterns.

Example:
"King" and "Queen"

will have nearby vector representations.

# Step 4: Contextual Understanding

Transformer neural networks analyze relationships between all words in the sentence using self-attention mechanisms.

The model checks:
- surrounding words
- grammar
- sentence structure
- semantic relationships

Example:

"bank"

can mean:
- river bank
- financial bank

The model understands meaning from context.

# Step 5: Sentence Embedding Creation

After processing all tokens, the model combines their contextual representations into one final sentence embedding.

Example:

"Artificial Intelligence is powerful"
↓
[0.21, -0.44, 0.87, 0.13, ...]

This final vector captures the semantic meaning of the complete sentence.

# Vector Space Representation

All sentence embeddings exist in a high-dimensional mathematical space called vector space.

Similar meanings are placed close together.

Example:

AI prediction systems
Machine learning forecasting

These embeddings appear near each other.

Unrelated sentences appear far apart.

Example:

Solar energy
Cooking recipes
Football match

These vectors are distant from AI-related embeddings.


# Similarity Comparison

The system compares vectors using cosine similarity.

Formula:

Cosine Similarity = (A · B) / (||A|| × ||B||)

Where:
- A = Query embedding
- B = Document embedding

The similarity score determines how semantically related two sentences are.

# Example from This Project

## Query

"How does AI help prediction?"

## Document


"Machine learning helps prediction systems"

The embedding model recognizes:
- AI ↔ Machine Learning
- Prediction ↔ Prediction Systems

Thus their vectors become close in vector space.

Result:

High Similarity Score


# Why Embeddings Are Powerful

Embeddings enable:
- semantic search
- recommendation systems
- chatbots
- AI assistants
- document retrieval
- language translation
- question answering systems

They form the core foundation of modern AI systems.

# Real-World Importance

Embedding systems are used in:
- ChatGPT
- Google Search
- Recommendation engines
- AI assistants
- YouTube recommendations
- Enterprise document search
- RAG systems

Modern AI applications depend heavily on embedding-based semantic understanding.
