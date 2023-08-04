import numpy as np
import pickle
import streamlit as st

st.header('Book Recommendation System')
model = pickle.load(open('artifacts/model.pkl', 'rb'))
books = pickle.load(open('artifacts/book_names.pkl', 'rb'))
final_rating = pickle.load(open('artifacts/final_rating.pkl', 'rb'))
book_pivot = pickle.load(open('artifacts/book_pivot.pkl', 'rb'))

def fetch_poster(suggestion):
    book_names = []
    poster_url = []
    ids_index = []

    for book_id in suggestion:
        book_names.append(book_pivot.index[book_id])
    
    for book_name in book_names[0]:
        ids = np.where(final_rating['title'] == book_name)[0][0]
        ids_index.append(ids)

    for index in ids_index:
        url = final_rating.iloc[index]['image_url']
        poster_url.append(url)

    return poster_url

def recommend_books(book_name):
    book_list = []
    book_id = np.where(book_pivot.index == book_name)[0][0]
    distance, suggestion = model.kneighbors(book_pivot.iloc[book_id, :].values.reshape(1, -1), n_neighbors=6)

    poster_url = fetch_poster(suggestion)
    for i in range(len(suggestion)):
        books = book_pivot.index[suggestion[i]]
        for j in books:
            book_list.append(j)
    
    return book_list, poster_url


selected_books = st.selectbox('Type or Select a book', books)

if st.button('Show Recommendation'):
   recommendations_books, poster_url = recommend_books(selected_books)

   col1, col2, col3, col4, col5 = st.columns(5)
   with col1:
       st.text(recommendations_books[1])
       st.image(poster_url[1])
    
   with col2:
       st.text(recommendations_books[2])
       st.image(poster_url[2])

   with col3:
       st.text(recommendations_books[3])
       st.image(poster_url[3])

   with col4:
       st.text(recommendations_books[4])
       st.image(poster_url[4])

   with col5:
       st.text(recommendations_books[5])
       st.image(poster_url[5]) 
       
