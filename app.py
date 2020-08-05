# Import required modules && classes
from flask import Flask, Blueprint, render_template, request, redirect


# Create the Flask app
app = Flask(__name__)

# Register blueprints


# Route home
@app.route('/')
def index():
    return render_template('index.html')

# __name__ == __main__
if (__name__ == '__main__'):
    app.run(debug=True)