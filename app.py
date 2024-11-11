import re
import os
import time
from flask import Flask, render_template, request
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

app = Flask(__name__)

# Load the content from the provided file
def load_content(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: The file {filepath} was not found.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

# Function to extract questions and answers from the content
def extract_questions_and_answers(content):
    questions = []
    answers = {}
    qa_pairs = re.split(r'\n#', content)
    for pair in qa_pairs:
        pair = pair.strip()
        if pair:
            lines = pair.split('\n')
            question = lines[0].replace('#', '').strip()
            answer = '\n'.join(lines[1:]).strip()
            questions.append(question)
            answers[question] = answer
    return questions, answers

# Main function to process user queries and return matching answers
def process_query(user_query, questions, answers):
    keywords = ['java', 'cpp', 'php', 'C++', 'javascript', 'ruby', 'flutter', 'kotlin', 'swift', 'dart', 'c#', 'c', 'html', 'css', 'sql', 'mysql', 'mongodb', 'firebase', 'postgresql', 'oracle', 'sqlite', 'microsoft', 'linux', 'windows', 'macos', 'android', 'ios', 'web', 'mobile', 'desktop', 'cloud', 'aws', 'azure', 'gcp', 'firebase', 'heroku', 'netlify', 'vercel', 'digitalocean', 'linode', 'vultr', 'hostinger', 'bluehost', 'godaddy', 'namecheap', 'cloudflare', 'github', 'gitlab', 'bitbucket', 'jira', 'trello', 'slack', 'discord', 'zoom', 'microsoftteams', 'skype', 'whatsapp', 'telegram', 'signal', 'instagram', 'facebook', 'twitter', 'linkedin', 'youtube', 'tiktok', 'snapchat', 'pinterest', 'reddit', 'quora', 'stackoverflow', 'medium', 'dev', 'hackernoon', 'freecodecamp', 'geeksforgeeks', 'w3schools', 'tutorialspoint', 'javatpoint', 'programiz', 'geektrust', 'leetcode', 'hackerrank', 'codechef', 'codeforces', 'topcoder', 'spoj', 'atcoder', 'kickstart', 'hackerearth', 'interviewbit']
    
    # Check if the user query contains any of the predefined keywords
    if any(keyword in user_query.lower() for keyword in keywords):
        return "Sorry, we aren't trained on this yet!"
    
    # Perform fuzzy matching to find the best answer
    best_match, score = process.extractOne(user_query, questions, scorer=fuzz.token_set_ratio)

    # Adjust threshold to allow more flexibility in matching
    if score > 50:  # Threshold can be adjusted based on need
        return answers[best_match]
    else:
        return "Sorry, we aren't trained on this yet!"

# Flask route to handle user input and render the response
@app.route('/', methods=['GET', 'POST'])
def home():
    dataset_path = 'dataset.txt'
    content = load_content(dataset_path)
    
    if content:
        questions, answers = extract_questions_and_answers(content)
    else:
        questions, answers = [], {}

    result = ""
    if request.method == 'POST':
        user_query = request.form['user_input'].strip()

        # Add a 4-second delay before processing the query
        time.sleep(4)

        result = process_query(user_query, questions, answers)
    
    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
