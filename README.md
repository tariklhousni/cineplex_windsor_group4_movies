# MovieProject — Group 4 Theater App

This is a small website that shows a list of movies and their screening times.  
It was made using Python and Flask.

## Project Structure

MovieProject/
│
├── data_preprocessing/
│   ├── load_data_to_db.py
│   ├── movie_data.csv
│   └── screenings_schedule.csv
│
├── database/
│   └── movies.db
│
├── website/
│   ├── app.py
│   ├── static/
│   │   └── index_style.css
│   └── templates/
│       ├── index.html
│       ├── movie_list.html
│       └── screenings.html
│
├── requirements.txt
└── README.md

## Features

- Shows a welcome page with buttons.
- Shows all movies in a table.
- Shows all screening times in a table.
- Has a button to go back to the home page.
- Uses a clean and simple design with CSS.
- Loads data from a database.

## How to Run

1. Extract the MovieProject.zip into any folder you want.
2. Go to the folder called MovieProject\website on your computer.
2. Run the file app.py
3. Copy the address shown in your terminal and past it in your web browser bar.
You will see the homepage, and navigate using the buttons to view movies or screenings.