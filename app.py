from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

print("Loading model...")

model = SentenceTransformer('all-MiniLM-L6-v2')

documents = [
    "Machine learning helps prediction systems",
    "Solar energy is renewable",
    "Pollution affects human health",
    "Artificial Intelligence is transforming industries"
]

query = "How does AI help prediction?"

print("Creating embeddings...")

doc_embeddings = model.encode(documents)
query_embedding = model.encode([query])

similarity = cosine_similarity(query_embedding, doc_embeddings)

print("\nQuestion:")
print(query)

print("\nSimilarity Scores:")
print(similarity)

best_match = similarity.argmax()

print("\nBest Matching Document:")
print(documents[best_match])