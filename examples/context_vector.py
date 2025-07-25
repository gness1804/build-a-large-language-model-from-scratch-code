import numpy as np

# 1. Example word embeddings for a 3-word sentence
# Let's say our sentence is: "cat sat mat"
embeddings = np.array([
    [1.0, 0.0],  # "cat"
    [0.0, 1.0],  # "sat"
    [1.0, 1.0],  # "mat"
])

# 2. Example attention weights for each word (rows sum to 1)
# Each row: how much the word attends to [cat, sat, mat]
attention_weights = np.array([
    [0.7, 0.2, 0.1],  # "cat" attends mostly to itself
    [0.1, 0.8, 0.1],  # "sat" attends mostly to itself
    [0.2, 0.2, 0.6],  # "mat" attends mostly to itself
])

# 3. Compute context vectors (weighted sum of embeddings)
context_vectors = attention_weights @ embeddings

print("Original embeddings:\n", embeddings)
print("\nAttention weights:\n", attention_weights)
print("\nContext vectors:\n", context_vectors)