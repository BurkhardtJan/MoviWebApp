import os
from flask import Flask, render_template, request, redirect, url_for, abort
from data_manager import DataManager
from models import db, Movie

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
data_dir = os.path.join(basedir, 'data')
if not os.path.exists(data_dir):
    os.makedirs(data_dir)
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(data_dir, 'movies.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)  # Link the database and the app. This is the reason you need to import db from models

data_manager = DataManager()  # Create an object of your DataManager class


@app.route('/')
def index():
    """Starting page. Shows list of users and form to add new user."""
    users = data_manager.get_users()
    return render_template("index.html", users=users), 200


@app.route('/users')
def list_users():
    users = data_manager.get_users()
    return str(users)  # Temporarily returning users as a string


@app.route('/users', methods=['POST'])
def create_user():
    """Adds a new user to the database."""
    new_user = request.form.get("new_user")
    if not new_user:
        return redirect(url_for('index'))
    try:
        data_manager.create_user(new_user)
    except Exception as e:
        print("An error occurred: ", str(e), 500)
        return "An error occurred: " + str(e), 500
    return redirect(url_for('index'))


@app.route('/users/<int:user_id>/movies', methods=['GET'])
def get_movies(user_id):
    """Shows a list of movies for a user."""
    user = data_manager.get_user_by_id(user_id)
    if user is None:
        abort(404)
    return render_template("movies.html", movies=data_manager.get_movies(user_id), user=user)


@app.route('/users/<int:user_id>/movies', methods=['POST'])
def add_movie(user_id):
    """Adds a new movie for user to the database."""
    movie_title = request.form.get("movie_title")
    if not movie_title:
        return redirect(url_for('get_movies', movies=data_manager.get_movies(user_id), user_id=user_id))
    try:
        data_manager.add_movie(movie_title, user_id)
    except Exception as e:
        print("An error occurred: ", str(e), 500)
        return "An error occurred: " + str(e), 500
    return redirect(url_for('get_movies', movies=data_manager.get_movies(user_id), user_id=user_id))


@app.route('/users/<int:user_id>/movies/<int:movie_id>/update', methods=['POST'])
def update_movie(user_id, movie_id):
    """Updates a movie title manually for user to the database."""
    new_title = request.form.get("new_title")
    try:
        data_manager.update_movie(movie_id, new_title)
    except Exception as e:
        print("An error occurred: ", str(e), 500)
        return "An error occurred: " + str(e), 500
    return redirect(url_for('get_movies', movies=data_manager.get_movies(user_id), user_id=user_id))


@app.route('/users/<int:user_id>/movies/<int:movie_id>/delete', methods=['POST'])
def delete_movie(user_id, movie_id):
    """Deletes a movie for user to the database."""
    try:
        data_manager.delete_movie(movie_id)
    except Exception as e:
        print("An error occurred: ", str(e), 500)
        return "An error occurred: " + str(e), 500
    return redirect(url_for('get_movies', movies=data_manager.get_movies(user_id), user_id=user_id))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run()
