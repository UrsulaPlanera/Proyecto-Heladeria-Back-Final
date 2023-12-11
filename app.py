
'''
Este código importa diferentes módulos y clases necesarios para el desarrollo de una aplicación Flask.

Flask: Es la clase principal de Flask, que se utiliza para crear instancias de la aplicación Flask.
jsonify: Es una función que convierte los datos en formato JSON para ser enviados como respuesta desde la API.
request: Es un objeto que representa la solicitud HTTP realizada por el cliente.
CORS: Es una extensión de Flask que permite el acceso cruzado entre dominios (Cross-Origin Resource Sharing), lo cual es útil cuando se desarrollan aplicaciones web con frontend y backend separados.
SQLAlchemy: Es una biblioteca de Python que proporciona una abstracción de alto nivel para interactuar con bases de datos relacionales.
Marshmallow: Es una biblioteca de serialización/deserialización de objetos Python a/desde formatos como JSON.
Al importar estos módulos y clases, estamos preparando nuestro entorno de desarrollo para utilizar las funcionalidades que ofrecen.

'''
# Importa las clases Flask, jsonify y request del módulo flask
from flask import Flask, jsonify, request
# Importa la clase CORS del módulo flask_cors
from flask_cors import CORS
# Importa la clase SQLAlchemy del módulo flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy
# Importa la clase Marshmallow del módulo flask_marshmallow
from flask_marshmallow import Marshmallow
#horario
from sqlalchemy.sql import func

'''
En este código, se está creando una instancia de la clase Flask y se está configurando para permitir el acceso cruzado entre dominios utilizando el módulo CORS.

app = Flask(__name__): Se crea una instancia de la clase Flask y se asigna a la variable app. El parámetro __name__ es una variable que representa el nombre del módulo o paquete en el que se encuentra este código. Flask utiliza este parámetro para determinar la ubicación de los recursos de la aplicación.

CORS(app): Se utiliza el módulo CORS para habilitar el acceso cruzado entre dominios en la aplicación Flask. Esto significa que el backend permitirá solicitudes provenientes de dominios diferentes al dominio en el que se encuentra alojado el backend. Esto es útil cuando se desarrollan aplicaciones web con frontend y backend separados, ya que permite que el frontend acceda a los recursos del backend sin restricciones de seguridad del navegador. Al pasar app como argumento a CORS(), se configura CORS para aplicar las políticas de acceso cruzado a la aplicación Flask representada por app.

'''
# Crea una instancia de la clase Flask con el nombre de la aplicación
app = Flask(__name__)
# Configura CORS para permitir el acceso desde el frontend al backend
CORS(app)

'''
En este código, se están configurando la base de datos y se están creando objetos para interactuar con ella utilizando SQLAlchemy y Marshmallow.

app.config["SQLALCHEMY_DATABASE_URI"]: Se configura la URI (Uniform Resource Identifier) de la base de datos. En este caso, se está utilizando MySQL como el motor de base de datos, el usuario y la contraseña son "root", y la base de datos se llama "proyecto". Esta configuración permite establecer la conexión con la base de datos.

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]: Se configura el seguimiento de modificaciones de SQLAlchemy. Al establecerlo en False, se desactiva el seguimiento automático de modificaciones en los objetos SQLAlchemy, lo cual mejora el rendimiento.

db = SQLAlchemy(app): Se crea un objeto db de la clase SQLAlchemy, que se utilizará para interactuar con la base de datos. Este objeto proporciona métodos y funcionalidades para realizar consultas y operaciones en la base de datos.

ma = Marshmallow(app): Se crea un objeto ma de la clase Marshmallow, que se utilizará para serializar y deserializar objetos Python a JSON y viceversa. Marshmallow proporciona una forma sencilla de definir esquemas de datos y validar la entrada y salida de datos en la aplicación. Este objeto se utilizará para definir los esquemas de los modelos de datos en la aplicación.

'''
# Configura la URI de la base de datos con el driver de MySQL, usuario, contraseña y nombre de la base de datos
# URI de la BD == Driver de la BD://user:password@UrlBD/nombreBD
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@localhost/proyecto"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@localhost/proyecto"
# Configura el seguimiento de modificaciones de SQLAlchemy a False para mejorar el rendimiento
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# Crea una instancia de la clase SQLAlchemy y la asigna al objeto db para interactuar con la base de datos
db = SQLAlchemy(app)
# Crea una instancia de la clase Marshmallow y la asigna al objeto ma para trabajar con serialización y deserialización de datos
ma = Marshmallow(app)


#tabla productos


class Producto(db.Model):  # Producto hereda de db.Model
    id_producto = db.Column(db.Integer, primary_key=True)
    nombre_producto = db.Column(db.String(100))
    descripcion_producto = db.Column(db.String(100))
    precio_producto = db.Column(db.Integer)
    stock_producto = db.Column(db.Integer)
    imagen_producto = db.Column(db.String(400))

    def __init__(self, nombre_producto, descripcion_producto, precio_producto, stock_producto, imagen_producto):
        self.nombre_producto = nombre_producto
        self.descripcion_producto = descripcion_producto
        self.precio_producto = precio_producto
        self.stock_producto = stock_producto
        self.imagen_producto = imagen_producto


#final tabla productos



#Tabla de registros


class Registro(db.Model):  # Registro hereda de db.Model

    id_registro = db.Column(db.Integer, primary_key=True)
    fecha_registro = db.Column(db.DateTime, nullable=False, server_default=func.current_timestamp())
    local_registro = db.Column(db.String(100))
    monto_registro = db.Column(db.Integer)

    def __init__(self, local_registro, monto_registro):
        self.local_registro = local_registro
        self.monto_registro = monto_registro


#final tabla registro



#tabla local



class Local(db.Model):  # Registro hereda de db.Model

    id_local = db.Column(db.Integer, primary_key=True)
    id_unico_local = db.Column(db.String(255), unique=True)
    municipio_local = db.Column(db.String(100))
    nombre_local = db.Column(db.String(100))

    def __init__(self, id_unico_local, municipio_local, nombre_local):
        self.municipio_local = municipio_local
        self.nombre_local = nombre_local
        self.id_unico_local = id_unico_local



#final tabla local



#tabla sabores

class Sabor(db.Model):  # Registro hereda de db.Model

    id_sabor = db.Column(db.Integer, primary_key=True)
    categoria_sabor = db.Column(db.String(100))
    nombre_sabor = db.Column(db.String(100))

    def __init__(self, categoria_sabor, nombre_sabor):
        self.categoria_sabor = categoria_sabor
        self.nombre_sabor = nombre_sabor


with app.app_context():
    db.create_all()  # Crea todas las tablas en la base de datos



#para tabla producto


class ProductoSchema(ma.Schema):
    """
    Esquema de la clase Producto.

    Este esquema define los campos que serán serializados/deserializados
    para la clase Producto.
    """
    class Meta:
        fields = ("id_producto", "nombre_producto", "descripcion_producto", "precio_producto", "stock_producto", "imagen_producto")

producto_schema = ProductoSchema()  # Objeto para serializar/deserializar un producto
productos_schema = ProductoSchema(many=True)  # Objeto para serializar/deserializar múltiples productos


@app.route("/productos", methods=["GET"])
def get_Productos():
    """
    Endpoint para obtener todos los productos de la base de datos.

    Retorna un JSON con todos los registros de la tabla de productos.
    """
    all_productos = Producto.query.all()  # Obtiene todos los registros de la tabla de productos
    result = productos_schema.dump(all_productos)  # Serializa los registros en formato JSON
    return jsonify(result)  # Retorna el JSON de todos los registros de la tabla


@app.route("/productos/<id_producto>", methods=["GET"])
def get_producto(id_producto):
    """
    Endpoint para obtener un producto específico de la base de datos.

    Retorna un JSON con la información del producto correspondiente al ID proporcionado.
    """
    producto = Producto.query.get(id_producto)  # Obtiene el producto correspondiente al ID recibido
    return producto_schema.jsonify(producto)  # Retorna el JSON del producto

@app.route("/productos/<id_producto>", methods=["DELETE"])
def delete_producto(id_producto):
    """
    Endpoint para eliminar un producto de la base de datos.

    Elimina el producto correspondiente al ID proporcionado y retorna un JSON con el registro eliminado.
    """
    producto = Producto.query.get(id_producto)  # Obtiene el producto correspondiente al ID recibido
    db.session.delete(producto)  # Elimina el producto de la sesión de la base de datos
    db.session.commit()  # Guarda los cambios en la base de datos
    return producto_schema.jsonify(producto)  # Retorna el JSON del producto eliminado

@app.route("/productos", methods=["POST"])  # Endpoint para crear un producto
def create_producto():

    # Obtiene lo solicitado del producto del JSON proporcionado
    nombre_producto = request.json["nombre_producto"]
    descripcion_producto = request.json["descripcion_producto"]
    precio_producto = request.json["precio_producto"]
    stock_producto = request.json["stock_producto"]
    imagen_producto = request.json["imagen_producto"]
    new_producto = Producto(nombre_producto, descripcion_producto, precio_producto, stock_producto, imagen_producto)
    db.session.add(new_producto)  # Agrega el nuevo producto a la sesión de la base de datos
    db.session.commit()  # Guarda los cambios en la base de datos
    return producto_schema.jsonify(new_producto)  # Retorna el JSON del nuevo producto creado

@app.route("/productos/<id_producto>", methods=["PUT"])  # Endpoint para actualizar un producto
def update_producto(id_producto):

    producto = Producto.query.get(id_producto)  # Obtiene el producto existente con el ID especificado

    # Actualiza los atributos del producto con los datos proporcionados en el JSON
    producto.nombre_producto = request.json["nombre_producto"]
    producto.descripcion_producto = request.json["descripcion_producto"]
    producto.precio_producto = request.json["precio_producto"]
    producto.stock_producto = request.json["stock_producto"]
    producto.imagen_producto = request.json["imagen_producto"]

    db.session.commit()  # Guarda los cambios en la base de datos
    return producto_schema.jsonify(producto)  # Retorna el JSON del producto actualizado



#finaliza para tabla producto



#para tabla registro


class RegistroSchema(ma.Schema):
    class Meta:
        fields = ("id_registro", "fecha_registro", "local_registro", "monto_registro")

registro_schema = RegistroSchema()  # Objeto para serializar/deserializar un registro
registros_schema = RegistroSchema(many=True)  # Objeto para serializar/deserializar múltiples registros



@app.route("/registros", methods=["GET"])
def get_Registros():

    all_registros = Registro.query.all()  # Obtiene todos los registros de la tabla de registros
    result = registros_schema.dump(all_registros)  # Serializa los registros en formato JSON
    return jsonify(result)  # Retorna el JSON de todos los registros de la tabla


@app.route("/registros/<id_registro>", methods=["GET"])
def get_registro(id_registro):

    registro = Registro.query.get(id_registro)  # Obtiene el registro correspondiente al ID recibido
    return registro_schema.jsonify(registro)  # Retorna el JSON del registro

@app.route("/registros/<id_registro>", methods=["DELETE"])
def delete_registro(id_registro):

    registro = Registro.query.get(id_registro)  # Obtiene el registro correspondiente al ID recibido
    db.session.delete(registro)  # Elimina el registro de la sesión de la base de datos
    db.session.commit()  # Guarda los cambios en la base de datos
    return registro_schema.jsonify(registro)  # Retorna el JSON del registro eliminado

@app.route("/registros", methods=["POST"])  # Endpoint para crear un registro
def create_registro():

    # Obtiene el nombre del registro del JSON proporcionado
    local_registro = request.json["local_registro"]
    monto_registro = request.json["monto_registro"]


    new_registro = Registro(local_registro, monto_registro)  # Crea un nuevo objeto registro con los datos proporcionados
    db.session.add(new_registro)  # Agrega el nuevo registro a la sesión de la base de datos
    db.session.commit()  # Guarda los cambios en la base de datos
    return registro_schema.jsonify(new_registro)  # Retorna el JSON del nuevo registro creado

@app.route("/registros/<id_registro>", methods=["PUT"])  # Endpoint para actualizar un registro
def update_registro(id_registro):

    registro = Registro.query.get(id_registro)  # Obtiene el registro existente con el ID especificado

    # Actualiza los atributos del registro con los datos proporcionados en el JSON
    registro.local_registro = request.json["local_registro"]
    registro.monto_registro = request.json["monto_registro"]

    db.session.commit()  # Guarda los cambios en la base de datos
    return registro_schema.jsonify(registro)  # Retorna el JSON del registro actualizado


#finaliza la tabla de registros



#para tabla locales


class LocalSchema(ma.Schema):

    class Meta:
        fields = ("id_local", "id_unico_local", "municipio_local", "nombre_local")

local_schema = LocalSchema()  # Objeto para serializar/deserializar un registro
locales_schema = LocalSchema(many=True)  # Objeto para serializar/deserializar múltiples registros

@app.route("/locales", methods=["GET"])
def get_Locales():

    all_locales = Local.query.all()  # Obtiene todos los registros de la tabla de registros
    result = locales_schema.dump(all_locales)  # Serializa los registros en formato JSON
    return jsonify(result)  # Retorna el JSON de todos los registros de la tabla

@app.route("/locales/<id_local>", methods=["GET"])
def get_local(id_local):

    local = Local.query.get(id_local)  # Obtiene el registro correspondiente al ID recibido
    return local_schema.jsonify(local)  # Retorna el JSON del registro

@app.route("/locales/<id_local>", methods=["DELETE"])
def delete_local(id_local):

    local = Local.query.get(id_local)  # Obtiene el registro correspondiente al ID recibido
    db.session.delete(local)  # Elimina el registro de la sesión de la base de datos
    db.session.commit()  # Guarda los cambios en la base de datos
    return local_schema.jsonify(local)  # Retorna el JSON del registro eliminado

@app.route("/locales", methods=["POST"])  # Endpoint para crear un registro
def create_local():

    id_unico_local = request.json["id_unico_local"]  # Obtiene el nombre del registro del JSON proporcionado
    municipio_local = request.json["municipio_local"]
    nombre_local = request.json["nombre_local"]

    new_local = Local(id_unico_local,municipio_local,nombre_local)  # Crea un nuevo objeto registro con los datos proporcionados
    db.session.add(new_local)  # Agrega el nuevo registro a la sesión de la base de datos
    db.session.commit()  # Guarda los cambios en la base de datos
    return local_schema.jsonify(new_local)  # Retorna el JSON del nuevo registro creado

@app.route("/locales/<id_local>", methods=["PUT"])  # Endpoint para actualizar un registro
def update_local(id_local):

    local = Local.query.get(id_local)  # Obtiene el registro existente con el ID especificado

    # Actualiza los atributos del registro con los datos proporcionados en el JSON
    local.id_unico_local = request.json["id_unico_local"]
    local.municipio_local = request.json["municipio_local"]
    local.nombre_local = request.json["nombre_local"]

    db.session.commit()  # Guarda los cambios en la base de datos
    return local_schema.jsonify(local)  # Retorna el JSON del registro actualizado


#finaliza tabla locales


"""                                        """


#para tabla sabores

class SaborSchema(ma.Schema):

    class Meta:
        fields = ("id_sabor", "categoria_sabor", "nombre_sabor")

sabor_schema = SaborSchema()  # Objeto para serializar/deserializar un registro
sabores_schema = SaborSchema(many=True)  # Objeto para serializar/deserializar múltiples registros

@app.route("/sabores", methods=["GET"])
def get_Sabores():

    all_sabores = Sabor.query.all()  # Obtiene todos los registros de la tabla de registros
    result = sabores_schema.dump(all_sabores)  # Serializa los registros en formato JSON
    return jsonify(result)  # Retorna el JSON de todos los registros de la tabla

@app.route("/sabores/<id_sabor>", methods=["GET"])
def get_sabor(id_sabor):

    sabor = Sabor.query.get(id_sabor)  # Obtiene el registro correspondiente al ID recibido
    return sabor_schema.jsonify(sabor)  # Retorna el JSON del registro

@app.route("/sabores/<id_sabor>", methods=["DELETE"])
def delete_sabor(id_sabor):

    sabor = Sabor.query.get(id_sabor)  # Obtiene el registro correspondiente al ID recibido
    db.session.delete(sabor)  # Elimina el registro de la sesión de la base de datos
    db.session.commit()  # Guarda los cambios en la base de datos
    return sabor_schema.jsonify(sabor)  # Retorna el JSON del registro eliminado

@app.route("/sabores", methods=["POST"])  # Endpoint para crear un registro
def create_sabor():

    # Obtiene el nombre del registro del JSON proporcionado
    categoria_sabor = request.json["categoria_sabor"]
    nombre_sabor = request.json["nombre_sabor"]

    new_sabor = Sabor(categoria_sabor,nombre_sabor)  # Crea un nuevo objeto registro con los datos proporcionados
    db.session.add(new_sabor)  # Agrega el nuevo registro a la sesión de la base de datos
    db.session.commit()  # Guarda los cambios en la base de datos
    return sabor_schema.jsonify(new_sabor)  # Retorna el JSON del nuevo registro creado

@app.route("/sabores/<id_sabor>", methods=["PUT"])  # Endpoint para actualizar un registro
def update_sabor(id_sabor):

    sabor = Sabor.query.get(id_sabor)  # Obtiene el registro existente con el ID especificado

    # Actualiza los atributos del registro con los datos proporcionados en el JSON
    sabor.categoria_sabor = request.json["categoria_sabor"]
    sabor.nombre_sabor = request.json["nombre_sabor"]

    db.session.commit()  # Guarda los cambios en la base de datos
    return sabor_schema.jsonify(sabor)  # Retorna el JSON del registro actualizado

@app.route('/')
def hello_world():
    return 'Hola desde ElArte Helados!'



# Programa Principal
if __name__ == "__main__":
    # Ejecuta el servidor Flask en el puerto 5000 en modo de depuración
    app.run(debug=True, port=5000)
