import os
from to_do_forms import AddForm, DelForm, PersonForm
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'


# Setup database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)


# Models
class Task(db.Model):

    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    desc = db.Column(db.Text)
    person = db.relationship('Person', backref='task', uselist=False)  # 1:1

    def __init__(self, desc):
        self.desc = desc

    def __repr__(self):
        if self.person:
            return f'{self.id}.  {self.desc} is assigned to {self.person.name}'
        else:
            return f'{self.id}.  {self.desc} currently has nobody assigned to complete'


class Person(db.Model):

    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'))

    def __init__(self, name, task_id):
        self.name = name
        self.task_id = task_id

# View functions
@app.route('/')
def to_do_home():
    return render_template('to_do_home.html')


@app.route('/to_do_add_task', methods=['GET', 'POST'])
def to_do_add_task():

    form = AddForm()

    if form.validate_on_submit():
        desc = form.desc.data
        new_task = Task(desc)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('to_do_list'))

    return render_template('to_do_add_task.html', form=form)


@app.route('/to_do_list')
def to_do_list():

    all_tasks = Task.query.all()
    return render_template('to_do_list.html', all_tasks=all_tasks)


@app.route('/to_do_delete_task', methods=['GET', 'POST'])
def to_do_delete_task():

    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        del_task = Task.query.get(id)
        db.session.delete(del_task)
        db.session.commit()
        return redirect(url_for('to_do_list'))

    return render_template('to_do_delete_task.html', form=form)


@app.route('/to_do_person', methods=['GET', 'POST'])
def to_do_person():

    form = PersonForm()

    if form.validate_on_submit():
        name = form.name.data
        assigned_task = form.assigned_task.data
        task = Task.query.get(assigned_task)
        person = Person(name, task.id)
        db.session.add(person)
        db.session.commit()
        return redirect(url_for('to_do_list'))

    return render_template('to_do_person.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
