from flask import Flask, request, render_template
import requests

app = Flask(__name__)

# Enter your movie database API key here
API_KEY = "e93c3350ce19973913e4baf37a49a213"


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/watchlist')
def watchlist():
    return render_template('watchlist.html')


@app.route('/liked')
def liked():
    return render_template('liked.html')


@app.route('/movies')
def search_movies():
    # Get the search query from the URL query string
    query = request.args.get('q')

    # Make a request to the movie database API to search for movies
    response = requests.get(f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={query}")

    # Get the list of movies from the API response
    movies = response.json()['results']

    # Build a response to display the list of movies
    response_html = "<h1>Movies</h1>"
    for movie in movies:
        response_html += "<p>" + movie['title'] + "</p>"

    return response_html


if __name__ == '__main__':
    app.run()
