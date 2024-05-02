<<<<<<< HEAD
<<<<<<< HEAD

# Movie-Recommender-System-with-sentiment-analysis-using-AJAX

![Python](https://img.shields.io/badge/Python-3.8-blueviolet)
![Framework](https://img.shields.io/badge/Framework-Flask-red)
![Frontend](https://img.shields.io/badge/Frontend-HTML/CSS/JS-green)
![API](https://img.shields.io/badge/API-TMDB-fcba03)

Content Based Recommender System recommends movies similar to the movie user likes and analyses the sentiments on the reviews given by the user for that movie.

The details of the movies(title, genre, runtime, rating, poster, etc) are fetched using an API by TMDB, https://www.themoviedb.org/documentation/api, and using the IMDB id of the movie in the API, I did web scraping to get the reviews given by the user in the IMDB site using `beautifulsoup4` and performed sentiment analysis on those reviews.

## How to get the API key?

Create an account in https://www.themoviedb.org/, click on the `API` link from the left hand sidebar in your account settings and fill all the details to apply for API key. If you are asked for the website URL, just give "NA" if you don't have one. You will see the API key in your `API` sidebar once your request is approved.

## How to run the project?

1. Clone or download this repository to your local machine.
2. Install all the libraries mentioned in the [requirements.txt] file with the command `pip install -r requirements.txt`
3. Get your API key from https://www.themoviedb.org/. (Refer the above section on how to get the API key)
4. Replace YOUR_API_KEY in **both** the places (line no. 15 and 29) of `static/recommend.js` file and hit save.
5. Open your terminal/command prompt from your project directory and run the file `main.py` by executing the command `python main.py`.
6. Go to your browser and type `http://127.0.0.1:5000/` in the address bar.
7. There you go! That's it.

## Architecture

![Recommendation App](https://user-images.githubusercontent.com/36665975/168742738-5435cf76-1a42-4d87-94b4-999e5bfc48d3.png)

## Similarity Score :

How does it decide which item is most similar to the item user likes? Here come the similarity scores.

It is a numerical value ranges between zero to one which helps to determine how much two items are similar to each other on a scale of zero to one. This similarity score is obtained measuring the similarity between the text details of both of the items. So, similarity score is the measure of similarity between given text details of two items. This can be done by cosine-similarity.

## How Cosine Similarity works?

Cosine similarity is a metric used to measure how similar the documents are irrespective of their size. Mathematically, it measures the cosine of the angle between two vectors projected in a multi-dimensional space. The cosine similarity is advantageous because even if the two similar documents are far apart by the Euclidean distance (due to the size of the document), chances are they may still be oriented closer together. The smaller the angle, higher the cosine similarity.

![image](https://user-images.githubusercontent.com/36665975/70401457-a7530680-1a55-11ea-9158-97d4e8515ca4.png)

### Sources of the datasets

1. [IMDB 5000 Movie Dataset](https://www.kaggle.com/carolzhangdc/imdb-5000-movie-dataset)
2. [The Movies Dataset](https://www.kaggle.com/rounakbanik/the-movies-dataset)
3. [List of movies in 2018](https://en.wikipedia.org/wiki/List_of_American_films_of_2018)
4. [List of movies in 2019](https://en.wikipedia.org/wiki/List_of_American_films_of_2019)
5. # [List of movies in 2020](https://en.wikipedia.org/wiki/List_of_American_films_of_2020)

# Movie-Application

> > > > > > > 17e8e6f62d4e500a70e836ba8e2bd7f4c5d6cb7f

### ML System Architecture for Movie Recommendation System

# Overview:

The ML system architecture for the movie recommendation system involves several components working together to provide personalized movie recommendations to users based on their preferences and behavior.

### Components:

# Data Collection:

Collects user interaction data such as movie ratings, searches, and views.
Data sources include user profiles, movie databases, and streaming platforms.

# Data Preprocessing:

Cleans and preprocesses the raw data to remove noise and inconsistencies.
Includes tasks like data cleaning, feature engineering, and normalization.

# Model Training:

Trains machine learning models using preprocessed data.
Models include collaborative filtering, content-based filtering, and hybrid models.
Training may involve techniques like matrix factorization, deep learning, or ensemble methods.

# Model Evaluation:

Evaluates the performance of trained models using metrics like precision, recall, and accuracy.
Conducts offline evaluation using historical data and online evaluation with A/B testing.

# Model Deployment:

Deploys the trained models into a production environment for real-time inference.
May involve containerization using Docker and deployment on cloud platforms like AWS, GCP, or Azure.

# User Interface:

Provides an interface for users to interact with the recommendation system.
Includes web or mobile applications where users can input preferences and receive recommendations.

### System Diagram:

# Key Technologies:

Python for data preprocessing, model training, and deployment.
Libraries like Pandas, NumPy, and Scikit-learn for data manipulation and machine learning.
Frameworks like TensorFlow or PyTorch for deep learning models.
Streamlit or Flask for building user interfaces.
Cloud platforms like AWS, GCP, or Azure for model deployment and scalability.

## Architecture:

+---------------------------------------------------------+
| ARCHITECTURE |
+----------------------+ +----------------------+ |
| | | | |
| Data Collection +-------->+ Data Preprocessing +--+->+
| (Tweets & Articles) | | (ZenML Pipeline) | | |
| Storage : Local/HDFS| | | | |
+-----------+----------+ +-----------+----------+ | |
^ | | |
| | | |
| v | |
| +----------------------+ | |
| | | | |
+----------> Model Training , <------------+ |
| Validation & Testing | |
| (Hugging Face | |
| Transformers, ZenML, | |
| Pytest) | |
| | |
+----------------------+ |
| |
v |
+---------------------+---------------------+ |
| | | |
| Model Serving | Docker Container <--------+
| (FastAPI, Flask) | (Deployment & Run) |
| | |
+----------+----------+---------------------+
|
v
+-----------+---------+
| |
| Frontend |
| Interaction |
| (User inputs, |
| Display results) |
| |
+---------------------+

+---------------+  
| | Storage |  
| | (Local Machine)|  
| +---------------+

## Conclusion:

The ML system architecture described above outlines the key components and technologies involved in building a movie recommendation system. By leveraging machine learning techniques and data-driven approaches, the system can deliver personalized recommendations to users, enhancing their movie-watching experience.
