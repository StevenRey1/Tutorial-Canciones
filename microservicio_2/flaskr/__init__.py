from flask import Flask



def create_app(config_name):
    app = Flask(__name__)  
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/tabla'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return app