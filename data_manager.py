from models import db, User, Movie
import fetch_from_omdbapi


class DataManager():

    def create_user(self, name):
        """Function for creating new user"""
        new_user = User(name=name)
        db.session.add(new_user)
        db.session.commit()

    def get_users(self):
        """Function for getting all users"""
        return User.query.all()

    def get_user_by_id(self, user_id):
        """Function for getting user by id"""
        return db.session.get(User, user_id)

    def get_movies(self, user_id):
        """Function for getting all movies of user"""
        return Movie.query.filter_by(user_id=user_id).all()

    def add_movie(self, movie, user_id):
        """Function for adding new movie form user to database"""
        movie_info = fetch_from_omdbapi.fetch_movie_info(movie)
        if movie_info["Response"] == "False":
            raise Exception(movie_info["Error"])
        name = movie_info["Title"]
        director = movie_info["Director"]
        year = movie_info["Year"]
        poster_url = movie_info["Poster"]
        new_movie = Movie(name=name, director=director, year=year, poster_url=poster_url, user_id=user_id)
        db.session.add(new_movie)
        db.session.commit()

    def update_movie(self, movie_id, new_title):
        """Function for updating movie title"""
        movie = Movie.query.get(movie_id)
        movie.name = new_title
        db.session.commit()

    def delete_movie(self, movie_id):
        """Function for deleting movie from database"""
        movie = Movie.query.get(movie_id)
        db.session.delete(movie)
        db.session.commit()
