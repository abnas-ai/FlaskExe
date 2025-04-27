from . import app
from .forms import TaskForm, UserForm
from .models import Task, User
from flask import render_template, flash, redirect, url_for
from . import db



@app.route('/')
def home():
    users = User.query.all()
    user_count = User.query.count()
    tasks = Task.query.all()
    task_count = Task.query.count()
    return render_template('index.html', title='Home', users=users, tasks=tasks, user_count=user_count,  task_count=task_count)
    
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
    return render_template('tasks.html', task_form=form)

@app.route('/tasks')
def tasks():
   
    form = TaskForm()
    
    tasks = Task.query.order_by(Task.timestamp.desc()).all()
    return render_template('tasks.html', tasks=tasks, task_form=form, title='Tasks')


@app.route('/users')
def users():
    form = UserForm()
    
    return render_template('users.html', users=users, title='Users', user_form=form)