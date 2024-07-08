from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
import pandas as pd
import joblib
from collections import defaultdict
from sklearn.preprocessing import StandardScaler
from scipy.spatial.distance import cdist
import numpy as np

app = Flask(__name__)
CORS(app)

# Load the dataset
data = pd.read_csv("./data.csv")
song_cluster_pipeline = joblib.load('ml_model.pkl')

# Define the required columns
number_cols = [
    'valence', 'year', 'acousticness', 'danceability', 'duration_ms', 'energy',
    'explicit', 'instrumentalness', 'key', 'liveness', 'loudness', 'mode',
    'popularity', 'speechiness', 'tempo'
]

# Define helper functions
def get_song_data(song, spotify_data):
    try:
        song_data = spotify_data[(spotify_data['name'] == song['name']) & (spotify_data['year'] == song['year'])].iloc[0]
        return song_data
    except IndexError:
        return None

def get_mean_vector(song_list, spotify_data):
    song_vectors = []
    for song in song_list:
        song_data = get_song_data(song, spotify_data)
        if song_data is None:
            print(f"Warning: {song['name']} does not exist in Spotify data")
            continue
        song_vector = song_data[number_cols].values
        song_vectors.append(song_vector)
    if not song_vectors:  # Check if song_vectors is empty
        return None
    song_matrix = np.array(song_vectors)
    return np.mean(song_matrix, axis=0)

def flatten_dict_list(dict_list):
    flattened_dict = defaultdict(list)
    for dictionary in dict_list:
        for key, value in dictionary.items():
            flattened_dict[key].append(value)
    return flattened_dict

def recommend_songs(song_list, spotify_data, song_cluster_pipeline, n_songs=10):
    metadata_cols = ['name', 'year', 'artists']
    song_dict = flatten_dict_list(song_list)
    song_center = get_mean_vector(song_list, spotify_data)
    if song_center is None:
        return []
    scaler = song_cluster_pipeline.steps[0][1]
    scaled_data = scaler.transform(spotify_data[number_cols])
    scaled_song_center = scaler.transform(song_center.reshape(1, -1))
    distances = cdist(scaled_song_center, scaled_data, 'cosine')
    index = list(np.argsort(distances)[:, :n_songs][0])
    rec_songs = spotify_data.iloc[index]
    rec_songs = rec_songs[~rec_songs['name'].isin(song_dict['name'])]
    return rec_songs[metadata_cols].to_dict(orient='records')

CREDENTIALS_FILE = 'credentials.json'

# Function to load existing credentials from the file
def load_credentials():
    if os.path.exists(CREDENTIALS_FILE):
        with open(CREDENTIALS_FILE, 'r') as file:
            return json.load(file)
    return {}

# Function to save credentials to the file
def save_credentials(credentials):
    with open(CREDENTIALS_FILE, 'w') as file:
        json.dump(credentials, file)
        

@app.route('/recommend', methods=['POST'])
def recommend():
    song_list = request.json.get('songs')
    if not song_list:
        return jsonify({"error": "No songs provided"}), 400
    
    print(song_list)
    recommendations = recommend_songs(song_list, data, song_cluster_pipeline)
    return jsonify(recommendations)

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    
    credentials = load_credentials()
    
    if email in credentials and credentials[email] == password:
        return jsonify({'authenticated': True}), 200
    else:
        return jsonify({'authenticated': False}), 401

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'Email and password are required'}), 400

    credentials = load_credentials()

    # Check if the user already exists
    if email in credentials:
        return jsonify({'authenticated': credentials[email] == password}), 200

    # Save new user credentials
    credentials[email] = password
    save_credentials(credentials)

    return jsonify({'authenticated': True}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5001)
