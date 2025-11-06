# Importing necessary modules from the Flask library
from flask import Flask, render_template

# Creating a Flask application instance
app = Flask(__name__)

# Defining the route for the homepage ("/")
@app.route('/')
def index():
    # When the user visits the root URL, return this simple text
    return "Hello, World!"


if __name__ == '__main__':
    # Start the Flask development server in debug mode
    app.run(debug=True)

# A new route that takes a variable from the URL and displays a greeting page
# Example: Visiting /greet/John will trigger this route
@app.route('/greet/<name>')
def greetpage(name):
    # Render an HTML template called 'index.html', passing the 'name' variable to it
    return render_template('index.html', name=name)
