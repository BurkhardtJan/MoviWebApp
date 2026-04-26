from models import db, User, Movie
import fetch_from_omdbapi


class DataManager():

    def create_user(self, name):
        new_user = User(name=name)
        db.session.add(new_user)
        db.session.commit()

    def get_user(self):
        return User.query.all()

    def get_movies(self, user_id):
        return Movie.query.filter_by(user_id=user_id).all()

    def add_movie(self, movie):
        movie_info = fetch_from_omdbapi.fetch_movie_info(movie)
        name = movie_info["Title"]
        director = movie_info["Director"]
        year = movie_info["Year"]
        poster_url = movie_info["Poster"]
        new_movie = Movie(name=name, director=director, year=year, poster_url=poster_url)
        db.session.add(new_movie)
        db.session.commit()

    def update_movie(self, movie_id, new_title):
        movie = Movie.query.get(movie_id)
        movie_info = fetch_from_omdbapi.fetch_movie_info(new_title)
        name = movie_info["Title"]
        director = movie_info["Director"]
        year = movie_info["Year"]
        poster_url = movie_info["Poster"]

        movie.title = name
        movie.director = director
        movie.year = year
        movie.poster_url = poster_url
        db.session.commit()

    def delete_movie(self, movie_id):
        movie = Movie.query.get(movie_id)
        db.session.delete(movie)
        db.session.commit()
