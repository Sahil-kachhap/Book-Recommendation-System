import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
print(final_rating.shape) # (61853, 8)
