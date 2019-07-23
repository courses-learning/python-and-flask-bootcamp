# Set up your imports here!
from flask import Flask

app = Flask(__name__)


@app.route('/')  # Fill this in!
def index():
    # Welcome Page
    # Create a generic welcome page.
    return "<h2>Welcome, Go to /puppy_latin/name to get your entered name in Puppy Latin</h2>"


@app.route('/puppy_latin/<name>')  # Fill this in!
def puppylatin(name):
    # This function will take in the name passed
    # and then use "puppy-latin" to convert it!
    if name.lower()[-1] == "y":
        new_name = name[:-1] + 'iful'
        return f"<h2>Hi {name.title()} your Puppy Latin name is {new_name.title()}</h2>"
    else:
        return f"<h2>Hi {name.title()} your Puppy Latin name is {name.title()}y</h2>"

    # HINT: Use indexing and concatenation of strings
    # For Example: "hello"+" world" --> "hello world"


if __name__ == '__main__':
    # Fill me in!
    app.run()
