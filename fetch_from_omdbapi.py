import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def fetch_movie_info(movie_name):
    REQUEST_URL = "http://www.omdbapi.com/"
    data = {
        "t": movie_name,
        "apikey": API_KEY
    }
    try:
        response = requests.get(REQUEST_URL, params=data)
        # print(response.status_code)
        # print(response.json())
        return response.json()
    except requests.exceptions.ConnectionError:
        # print("Connection Error")
        return {'Response': 'False', 'Error': 'Connection Error'}
