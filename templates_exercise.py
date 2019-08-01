from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('template_ex_home.html')


@app.route('/template_ex_result')
def template_ex_result():
    # Assign username variable from forms input
    username = request.args.get('username')

    # Set flags for each requirement
    upflag = (any(letter.isupper() for letter in username))
    lowflag = (any(letter.islower() for letter in username))
    numflag = username[-1].isdigit()

    # Set clear variable to true if all requirements met
    clear = upflag and lowflag and numflag

    return render_template('template_ex_result.html', upflag=upflag, lowflag=lowflag, numflag=numflag, clear=clear)


if __name__ == '__main__':
    app.run(debug=True)
