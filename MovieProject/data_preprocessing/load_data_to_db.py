import os                # for file and folder paths
import pandas as pd      # read CSV files and manage data tables
import sqlite3           # create and work with SQLite database

# access folder where this Python file is saved
script_dir = os.path.dirname(os.path.abspath(__file__))

# Load the movie CSV file from the same folder
movies = pd.read_csv(os.path.join(script_dir, 'movie_data.csv'))

# Load the screenings CSV file from the same folder
screenings = pd.read_csv(os.path.join(script_dir, 'screenings_schedule.csv'))

# Create the path to save the database file in the "database" folder, one level up
db_path = os.path.abspath(os.path.join(script_dir, '..', 'database', 'movies.db'))

# Connect to the SQLite database
conn = sqlite3.connect(db_path)

# Save the movies data to a table named "movies" in the .db file
movies.to_sql('movies', conn, if_exists='replace', index=False)

# Save the screenings data to a table named "screenings" in the .db file
screenings.to_sql('screenings', conn, if_exists='replace', index=False)

# Close the connection
conn.close()