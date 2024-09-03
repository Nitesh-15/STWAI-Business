# My Flask App

This is a simple Flask web application with an SQLite database.

## Features

- User model with username and email
- Home page displaying a list of users
- Form to add new users

## Installation

1. Clone the repository.
2. Create a virtual environment and install dependencies.
3. Run the application.

```bash
git clone https://github.com/your-repo/my_flask_app.git
cd my_flask_app
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
python run.py
