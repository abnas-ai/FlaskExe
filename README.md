# Flask Task Manager

A simple task management web application built with Flask, SQLAlchemy, and WTForms. It allows users to create, view, and update tasks stored in a SQLite database.

---

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Usage](#usage)
- [Database Migrations](#database-migrations)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- Create new tasks with a title, description, and completion status.
- View a list of all tasks.
- Form validation with Flask-WTF and WTForms.
- Persistent data storage using SQLAlchemy with SQLite.
- Flash messages for user feedback.

## Prerequisites

- Python 3.7 or higher
- Git (to clone the repository)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/flask-task-manager.git
   cd flask-task-manager
   ```

2. **Create and activate a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Project Structure

```
FlaskExe/
├── app/
│   ├── __init__.py       # Initializes the Flask app and database
│   ├── main.py           # Entry point for the application
│   ├── routes.py         # URL route handlers
│   ├── models.py         # SQLAlchemy data models
│   ├── forms.py          # WTForms form definitions
│   ├── utils.py          # Database setup (SQLAlchemy instance)
│   └── templates/
│       └── forms.html    # Jinja2 template for task form and list
├── venv/                 # Virtual environment
├── requirements.txt      # Python package dependencies
└── README.md             # Project documentation
```

## Configuration

- **SECRET_KEY**: Used by Flask to secure sessions and forms. Set in `app/__init__.py` or via environment variable.
- **SQLALCHEMY_DATABASE_URI**: Database connection string. Defaults to `sqlite:///tasks.db`.

You can override these settings by exporting environment variables before running the app:

```bash
export SECRET_KEY="your-secret-key"
export SQLALCHEMY_DATABASE_URI="sqlite:///your-db-file.db"
```

## Usage

1. **Running the application**
   ```bash
   # From the project root directory:
   python -m app.main
   # Or if you have FLASK_APP configured:
   flask run
   ```

2. **Access in browser**
   - **Home**:  `http://127.0.0.1:5000/` (returns a welcome message)
   - **Create Task**: `http://127.0.0.1:5000/create-task`
   - **View Tasks**:  `http://127.0.0.1:5000/tasks`

3. **Creating a task**
   - Fill out the title, description, and completion checkbox.
   - Click **Submit**.
   - A flash message confirms the creation.

4. **Viewing tasks**
   - The tasks page displays all existing tasks from the database.

## Database Migrations

For a simple SQLite app you may not need Alembic, but for larger projects consider adding Flask-Migrate:

```bash
pip install Flask-Migrate
```

Then in your code:

```python
from flask_migrate import Migrate
migrate = Migrate(app, db)
```

Commands:
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

## Contributing

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/my-feature`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/my-feature`.
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

