# 🎬 Movie Recommender System (Content-Based)

## 📌 Overview
This project implements a content-based movie recommender system that suggests similar movies based on textual features such as genres, overview, and keywords. The system uses TF-IDF vectorization and cosine similarity to find movies that are most similar to a given movie.

## 🚀 Features
- Content-based recommendation approach
- Uses TF-IDF vectorization for text representation
- Computes cosine similarity to measure movie similarity
- Recommends top similar movies based on user input
- Lightweight and fast implementation using Python

## 🛠️ Tech Stack
- Python  
- Pandas  
- Scikit-learn  
- TF-IDF Vectorizer  

## 🔍 How It Works
1. Movie metadata is preprocessed and combined into a single textual feature.
2. TF-IDF vectorization converts text data into numerical vectors.
3. Cosine similarity is calculated between movie vectors.
4. The system returns the top N most similar movies.

## 📈 Use Case
This project demonstrates how recommendation systems work in platforms like Netflix and Amazon by leveraging content similarity rather than user behavior.

## ▶️ How to Run
1. Clone the repository  
   ```bash
   git clone <repository-url>
