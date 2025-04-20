# from flask import Flask

# app = Flask(__name__)
# app.config['SECRET_KEY']='837ff881ff74c5fc48e9a3e5b177960ca1db7488c6edf91a9b38f9f29250e5a0'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
from app import app

if __name__ == '__main__':
    app.run(debug=True)