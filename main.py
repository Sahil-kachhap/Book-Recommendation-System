import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

books = pd.read_csv('data/BX-Books.csv', sep=';', encoding="latin-1", on_bad_lines='skip')
print(books.shape)

# data cleaning
books = books[['ISBN', 'Book-Title', 'Book-Author', 'Year-Of-Publication', 'Publisher', 'Image-URL-L']]
books.rename(columns={
    "Book-Title": "title",
    "Book-Author": "author",
    "Year-Of-Publication": "year",
    "Publisher": "publisher",
    "Image-URL-L": "image_url"
}, inplace=True)
print(books.columns)

users = pd.read_csv('data/BX-Users.csv', sep=';', encoding="latin-1", on_bad_lines='skip')
ratings = pd.read_csv('data/BX-Book-Ratings.csv', sep=';', encoding="latin-1", on_bad_lines='skip')
ratings.rename(columns={
    "User-ID": "user_id",
    "Book-Rating": "rating",
}, inplace=True)
print(ratings.columns)
