import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors

books = pd.read_csv('data/BX-Books.csv', sep=';', encoding="latin-1", on_bad_lines='skip')
# print(books.shape)

# data cleaning
books = books[['ISBN', 'Book-Title', 'Book-Author', 'Year-Of-Publication', 'Publisher', 'Image-URL-L']]
books.rename(columns={
    "Book-Title": "title",
    "Book-Author": "author",
    "Year-Of-Publication": "year",
    "Publisher": "publisher",
    "Image-URL-L": "image_url"
}, inplace=True)

users = pd.read_csv('data/BX-Users.csv', sep=';', encoding="latin-1", on_bad_lines='skip')
ratings = pd.read_csv('data/BX-Book-Ratings.csv', sep=';', encoding="latin-1", on_bad_lines='skip')
ratings.rename(columns={
    "User-ID": "user_id",
    "Book-Rating": "rating",
}, inplace=True)
# print(ratings.columns)

filtered_users = ratings['user_id'].value_counts() > 200
# print(filtered_users[filtered_users].shape)
y = filtered_users[filtered_users].index
ratings = ratings[ratings['user_id'].isin(y)]
rated_books = ratings.merge(books, on='ISBN')
#print(rated_books.columns)
num_rating = rated_books.groupby('title')['rating'].count().reset_index()
num_rating.rename(columns={"rating": "rating_count"}, inplace=True)
final_rating = rated_books.merge(num_rating, on='title')
final_rating = final_rating[final_rating['rating_count'] >= 50]
final_rating.drop_duplicates(['user_id', 'title'], inplace=True)
#print(final_rating.shape) # (61853, 8)

# pivot table implementation
book_pivot = final_rating.pivot_table(columns='user_id', index='title', values='rating')
book_pivot.fillna(0, inplace=True)
#print(book_pivot.shape) 
book_sparse = csr_matrix(book_pivot)

# Clustering Algorithm implementation
model = NearestNeighbors(algorithm='brute')
model.fit(book_sparse)
distance, suggestion = model.kneighbors(book_pivot.iloc[237, :].values.reshape(1, -1), n_neighbors=6)
for i in range(len(suggestion)):
    print(book_pivot.index[suggestion[i]])

book_names = book_pivot.index
pickle.dump(model, open('artifacts/model.pkl', 'wb'))
pickle.dump(book_names, open('artifacts/book_names.pkl', 'wb'))
pickle.dump(final_rating, open('artifacts/final_rating.pkl', 'wb'))
pickle.dump(book_pivot, open('artifacts/book_pivot.pkl', 'wb'))

# testing
def recommend_books(book_name):
    book_id = np.where(book_pivot.index == book_name)[0][0]
    distance, suggestion = model.kneighbors(book_pivot.iloc[book_id, :].values.reshape(1, -1), n_neighbors=6)
    for i in range(len(suggestion)):
        books = book_pivot.index[suggestion[i]]
        for j in range(len(books)):
            print(books[j])

recommend_books("Harry Potter and the Sorcerer's Stone (Book 1)")