from flask import Flask, render_template
import sqlite3
import os

app = Flask(__name__)

# connecting the database to the function
def get_db_connection():
    base_dir = os.path.dirname(__file__)  # Folder where this file is saved
    db_path = os.path.join(base_dir, '..', 'database', 'movies.db')  # find the path to the database folder
    db_path = os.path.abspath(db_path)  # Get full path to the file

    conn = sqlite3.connect(db_path)  # Connect to the database
    conn.row_factory = sqlite3.Row  # So we can use column names in HTML
    return conn

# Show homepage
@app.route('/')
def home():
    return render_template("index.html")

# Show list of movies
@app.route('/movie_list')
def show_movies():
    conn = get_db_connection()
    rows = conn.execute("SELECT * FROM movies").fetchall()
    movies = [dict(row) for row in rows]  # Convert sqlite3.Row to dictionary to run the trailer link
    conn.close()
    return render_template("movie_list.html", movies=movies)

# Show movie screening times
@app.route('/screenings')
def show_screenings():
    conn = get_db_connection()
    rows = conn.execute("SELECT * FROM screenings").fetchall()
    screenings = [dict(row) for row in rows] # Convert sqlite3.Row to dictionary to keep the same type of coding
    conn.close()
    return render_template("screenings.html", screenings=screenings)

# Start the app
if __name__ == '__main__':
    app.run(debug=True, port=5001)