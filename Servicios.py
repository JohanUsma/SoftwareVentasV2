import sys;
import jsonify;
import flask;
import json;
import datetime;
import decimal;
import jwt
from Utilidades import Convertir;
from Aplicaciones.cl_Cliente_Aplicacion import cl_Cliente_Aplicacion;

print(__name__);
app = flask.Flask(__name__);

@app.route('/Servicios/Autenticacion', methods=["POST"])
def Autenticacion() -> str :
    respuesta = { };
    try:
        datos = flask.request.get_json();

        if(not "Usuario" in datos.keys() or not "Contrasena" in datos.keys()):
            respuesta["Error"] = 'Formato Json Invalido';
            return (flask.jsonify(respuesta), 400);
            
        if datos["Usuario"] != "Prueba" or datos["Contrasena"] != "12345678":
            respuesta["Error"] = 'Usuario o Contraseña Incorrectos';
            return (flask.jsonify(respuesta), 401);

        key = "KJhisdy8787798udfsd56f4s5d4fsdf";
        encoded = jwt.encode({"Usuario": "Prueba"}, key, algorithm="HS256");
        
        respuesta["Token"] = encoded;
        respuesta["Response"] = "Ok";
        return flask.jsonify(respuesta);
    except Exception as ex:
        respuesta["Error"] = str(ex);
        return flask.jsonify(respuesta);

@app.route('/Servicios/Cliente/Listar/<id>', methods=["GET"])
def Listar_By_Id(id: str) -> str:
    respuesta = {}
    try:
        # Obtener el token desde el encabezado
        token = flask.request.headers.get("Token")

        # Validar que el token esté presente
        if not token:
            respuesta["Error"] = 'lbNoAutenticacion'
            return (flask.jsonify(respuesta), 401)

        # Decodificar el token
        key = "KJhisdy8787798udfsd56f4s5d4fsdf"
        jwt.decode(token, key, algorithms=["HS256"])

        aplicacion: cl_Cliente_Aplicacion = cl_Cliente_Aplicacion();
        respuesta["Response"] = "Ok";
        respuesta["Entidades"] = aplicacion.Listar(id);
        return flask.jsonify(respuesta);

    except Exception as ex:
        respuesta["Error"] = str(ex)
        return flask.jsonify(respuesta), 500

@app.route('/Servicios/Cliente/Listar', methods=["POST"])
def Listar() -> str:
    respuesta = {}
    try:
        # Obtener el token desde el encabezado
        token = flask.request.headers.get("Token")

        # Validar que el token esté presente
        if not token:
            respuesta["Error"] = 'lbNoAutenticacion'
            return (flask.jsonify(respuesta), 401)

        # Decodificar el token
        key = "KJhisdy8787798udfsd56f4s5d4fsdf"
        jwt.decode(token, key, algorithms=["HS256"])

        aplicacion: cl_Cliente_Aplicacion = cl_Cliente_Aplicacion();
        respuesta["Response"] = "Ok";
        respuesta["Entidades"] = aplicacion.Listar(None);
        return flask.jsonify(respuesta);

    except Exception as ex:
        respuesta["Error"] = str(ex)
        return flask.jsonify(respuesta), 500

app.run('localhost', 4040);