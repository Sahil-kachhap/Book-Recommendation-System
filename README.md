# Book Recommendation System using Collaborative Filtering
![book-recommendation](https://github.com/Sahil-kachhap/Book-Recommendation-System/assets/54017876/a95287ad-f996-4a4b-8ec3-0f73917cbe69)

## Description
The Book Recommendation System is built to assist users in discovering new books that align with their interests. It utilizes collaborative filtering, a user-based approach, to generate book recommendations. By analyzing the ratings and preferences of similar users, the system identifies books that might interest the active user.

The collaborative filtering algorithm follows these steps:

1. Data Preprocessing: The datasets, including books, ratings, and user information, are loaded and preprocessed to ensure consistency and remove any irrelevant data.
2. User Selection: The user can select a book from a dropdown list to indicate their preference.
3. Collaborative Filtering: The system uses collaborative filtering techniques to identify users who have similar preferences to the active user.
4. Recommendation Generation: Based on the collaborative filtering results, a list of book recommendations is generated and presented to the user.
5. Display: The recommended books are displayed to the user, and they can explore more details about each book, such as the book title, author, publication year, and publisher.

The project aims to help users discover new books they might enjoy and foster a sense of community among book enthusiasts by providing personalized recommendations.

## Dataset
The project uses three datasets:

1. Books Dataset:

- "ISBN": International Standard Book Number.
- "Book-Title": Title of the book.
- "Book-Author": Author of the book.
- "Year-Of-Publication": Year of publication of the book.
- "Publisher": Publisher of the book.
- "Image-URL-L": URL of the book cover image.

2. Ratings Dataset:

- "User-ID": Unique identifier for users.
- "ISBN": International Standard Book Number.
- "Book-Rating": User's rating for the book (from 1 to 10).

3. Users Dataset:

- "User-ID": Unique identifier for users.
- "Location": Location of the user.
- "Age": Age of the user.
