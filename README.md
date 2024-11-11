FAQ Chatbot using Flask and Fuzzy Matching
A simple FAQ chatbot web application built with Flask that uses fuzzy matching to find the most relevant answer to a user's question from a predefined dataset. This chatbot is ideal for quick, automated responses to common queries, and is highly customizable for different use cases.

Features
Flask Web Application: Provides a user-friendly web interface where users can type questions and receive answers.
Fuzzy Matching: Uses the fuzzywuzzy library to match user queries with questions in the dataset, allowing flexibility in the phrasing of questions.
Keyword Filtering: Filters out queries that contain specific keywords and provides a default response if the question is outside the scope of training.
4-Second Delay: Adds a slight delay after each query for a more natural experience.
How It Works
Dataset: The bot reads questions and answers from a dataset file (e.g., dataset.txt), which contains FAQ pairs.
Preprocessing: The questions are extracted from the dataset and stored in a list, while answers are stored in a dictionary.
Fuzzy Matching: When a user submits a query, the app uses fuzzy string matching to find the closest question in the dataset and returns the associated answer.
Keyword Filtering: Certain keywords (like programming languages and tools) are filtered to return a default message, ensuring the bot only answers relevant questions.
Getting Started
Prerequisites
Python 3.7+
Flask
fuzzywuzzy library
Jinja2 (used for rendering HTML templates in Flask)
