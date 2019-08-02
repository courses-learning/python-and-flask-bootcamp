from flask import Flask, render_template, flash, session, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'


class SimpleForm(FlaskForm):

    submit = SubmitField('Submit')
    shark_type = StringField('What is your favourite type of shark?')


@app.route('/', methods=['GET', 'POST'])
def home():
    form = SimpleForm()

    if form.validate_on_submit():
        session['shark_type'] = form.shark_type.data

        if form.shark_type.data.lower() == 'great white' or form.shark_type.data.lower() == 'great white shark':
            flash('WARNING - The Great White Shark is VERY DANGEROUS!')
        elif form.shark_type.data.lower() == 'hammerhead' or form.shark_type.data.lower() == 'hammerhead shark':
            flash('TAKE CARE - The Hammerhead Shark can be dangerous')
        elif form.shark_type.data.lower() == 'tiger' or form.shark_type.data.lower() == 'tiger shark':
            flash('TAKE CARE - The Tiger Shark can be dangerous')
        else:
            flash(f'YOU SHOULD BE OK - The {form.shark_type.data} is not dangerous')

        return redirect(url_for('home'))

    return render_template('forms_ex_home.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
