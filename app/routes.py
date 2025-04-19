

from flask import render_template
from app import app
from app.models import User

@app.route('/')
def home():
    users = User.query.all()
    return render_template('index.html', users=users)


from flask import render_template, redirect, url_for, flash
from app.forms import TaskForm
from app.models import Task, db

@app.route('/create-task', methods=['GET', 'POST'])
def create_task():
    form = TaskForm()
    if form.validate_on_submit():
        new_task = Task(
            title=form.title.data,
            description=form.description.data,
            completed=form.completed.data,
            user_id=1  # Replace with actual user ID logic
        )
        db.session.add(new_task)
        db.session.commit()
        flash('Task created successfully!')
        return redirect(url_for('create_task'))
    return render_template('create_task.html', form=form)
@app.route('/tasks')
def tasks():
    tasks = Task.query.all()
    return render_template('tasks.html', tasks=tasks)



