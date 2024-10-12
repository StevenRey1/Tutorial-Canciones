from flaskr import create_app
from .modelos import db, Cancion, Album, Usuario, Medio
from .modelos import AlbumSchema
from flask_restful import Api
from .vistas import VistaCanciones, VistaCancion, VistaSignIn, VistaLogIn, VistaAlbum, VistaAlbumsUsuario, VistaCancionesAlbum
from flask_jwt_extended import JWTManager
from flask_cors import CORS

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()
cors=CORS(app)

api = Api(app)
api.add_resource(VistaCanciones, '/canciones')
api.add_resource(VistaCancion, '/cancion/<int:id_cancion>')
api.add_resource(VistaSignIn, '/signin')
api.add_resource(VistaLogIn, '/login')
api.add_resource(VistaAlbumsUsuario, '/usuario/<int:id_usuario>/albumes')
api.add_resource(VistaAlbum, '/album/<int:id_album>')
api.add_resource(VistaCancionesAlbum, '/album/<int:id_album>/canciones')

jwt = JWTManager(app)

#PRUEBA
""" with app.app_context():
    album_schema = AlbumSchema()
    A = Album(titulo='Prueba', anio = 1999, descripcion = 'Texto', medio = Medio.CD)
    db.session.add(A)
    db.session.commit()
    print([album_schema.dumps(album) for album in Album.query.all()]) """
    


""" with app.app_context():
    c= Cancion(titulo= 'Prueba', minutos = 2,segundos = 2,interprete = 'SS')
    db.session.add(c)
    db.session.commit()
    print(Cancion.query.all())
with app.app_context():
    u = Usuario(nombre = 'Juan', contrasena = '12345')
    a = Album(titulo='prueba', anio=1999, descripcion = 'texto', medio = Medio.CD)
    c = Cancion(titulo = 'mi cancion', minutos = 2, segundos = 25, interprete = 'Yo')
    u.albumes.append(a)
    a.canciones.append(c)
    db.session.add(u)
    db.session.add(c)
    db.session.commit()
    print(Usuario.query.all())
    print(Usuario.query.all()[0].albumes)
    print(Album.query.all())
    print(Album.query.all()[0].canciones)
    print(Cancion.query.all())
    db.session.delete(a)
    print(Usuario.query.all())
    print(Album.query.all())
    print(Album.query.all())
    print(Cancion.query.all()) """
    
    
    