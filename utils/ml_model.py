import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.neighbors import NearestNeighbors
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Sample dataset
data = {
    'title': ['Book1', 'Book2', 'Book3', 'Book4', 'Book5'],
    'genre': ['Fantasy', 'Sci-Fi', 'Fantasy', 'Romance', 'Romance'],
    'average_rating': [4.5, 4.7, 4.0, 3.5, 4.1],
    'number_of_ratings': [150, 200, 50, 75, 120]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# One-hot encode the genre
encoder = OneHotEncoder()
genre_encoded = encoder.fit_transform(df[['genre']]).toarray()

# Normalize the average rating (Optional)
ratings = df['average_rating'].values.reshape(-1, 1)

# Combine features
X = np.hstack((genre_encoded, ratings))

# Train the model
knn = NearestNeighbors(metric='cosine', algorithm='brute')
knn.fit(X)


# Function to recommend books
def recommend_books(book_title, n_recommendations=3):
    book_idx = df[df['title'] == book_title].index[0]
    book_vector = X[book_idx].reshape(1, -1)
    distances, indices = knn.kneighbors(book_vector, n_neighbors=n_recommendations + 1)

    recommended_books = []
    for i in range(1, len(distances.flatten())):
        recommended_books.append(df.iloc[indices.flatten()[i]]['title'])

    return recommended_books


# Example usage
book_to_recommend_for = 'Book1'
recommended_books = recommend_books(book_to_recommend_for)
print(f"Books recommended for {book_to_recommend_for}: {recommended_books}")
