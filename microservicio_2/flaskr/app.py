from flask import Flask
from flask_restful import Api, Resource
from celery import Celery
from modelos import db, Cancion, CancionSchema

cancion_schema = CancionSchema()

app = Flask(__name__)  
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@db:5432/tabla'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

class VistaTablaPuntaje(Resource):

    def get(self):
        print([cancion_schema.dump(ca) for ca in Cancion.query.all()])
        return [cancion_schema.dump(ca) for ca in Cancion.query.all()]

api = Api(app)
api.add_resource(VistaTablaPuntaje, '/tablaPuntajes')