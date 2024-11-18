import sys;
import jsonify;
import flask;
import json;
import datetime;
import decimal;
import jwt;
from Utilidades import Convertir;
from Aplicaciones.cl_Cliente_Aplicacion import cl_Cliente_Aplicacion;
from Aplicaciones.cl_DetalleVenta_Aplicacion import cl_DetalleVenta_Aplicacion;
from Aplicaciones.cl_MetodoPago_Aplicacion import cl_MetodoPago_Aplicacion;
from Aplicaciones.cl_Producto_Aplicacion import cl_Producto_Aplicacion;
from Aplicaciones.cl_Proveedor_Aplicacion import cl_Proveedor_Aplicacion;

key = "KJhisdy8787798udfsd56f4s5d4fsdf";
dicCredenciales = {"Usuario": "Prueba", "Contrasena": "1234568"}

print(__name__);
app = flask.Flask(__name__);


@app.route('/Servicios/Autenticacion', methods=["POST"])
def Autenticacion() -> str :
    respuesta = { };
    try:
        datos = flask.request.get_json();

        #Validar si los datos tienen los campos necesarios
        if(not "Usuario" in datos.keys() or not "Contrasena" in datos.keys()):
            respuesta["Error"] = 'Formato Json Invalido';
            return (flask.jsonify(respuesta), 400);
        
        #Valdiar si el usuario y contraseña son correctos
        if datos["Usuario"] != dicCredenciales["Usuario"] or datos["Contrasena"] != dicCredenciales["Contrasena"]:
            respuesta["Error"] = 'Usuario o Contraseña Incorrectos';
            return (flask.jsonify(respuesta), 401);

        #Generar Token
        encoded = jwt.encode(dicCredenciales, key, algorithm="HS256");

        respuesta["Token"] = encoded;
        respuesta["Response"] = "Ok";
        return flask.jsonify(respuesta);
    except Exception as ex:
        respuesta["Error"] = str(ex);
        return flask.jsonify(respuesta);

@app.route('/Servicios/Cliente/Listar/<id>', methods=["GET"])
def Listar_Cliente_By_Id(id: str) -> str:
    respuesta = {}
    try:
        # Obtener el token desde el encabezado
        token = flask.request.headers.get("Token")

        # Validar que el token esté presente
        if not token:
            respuesta["Error"] = 'lbNoAutenticacion'
            return (flask.jsonify(respuesta), 401)

        #Decodificar Token
        user_deco = jwt.decode(token, key, algorithms=["HS256"])
        
        #Validar Usuario y Constraseña
        if user_deco["Usuario"] != dicCredenciales["Usuario"] or user_deco["Contrasena"] != dicCredenciales["Contrasena"]:
            respuesta["Error"] = 'Token Invalido';
            return (flask.jsonify(respuesta), 401);
        
        aplicacion: cl_Cliente_Aplicacion = cl_Cliente_Aplicacion();
        respuesta["Response"] = "Ok";
        respuesta["Entidades"] = aplicacion.Listar(id);
        return flask.jsonify(respuesta);

    except Exception as ex:
        respuesta["Error"] = str(ex)
        return flask.jsonify(respuesta), 500

@app.route('/Servicios/Cliente/Listar', methods=["POST"])
def Listar_Cliente() -> str:
    respuesta = {}
    try:
        # Obtener el token desde el encabezado
        token = flask.request.headers.get("Token")

        # Validar que el token esté presente
        if not token:
            respuesta["Error"] = 'lbNoAutenticacion'
            return (flask.jsonify(respuesta), 401)

        #Decodificar Token
        user_deco = jwt.decode(token, key, algorithms=["HS256"])
        
        #Validar Usuario y Constraseña
        if user_deco["Usuario"] != dicCredenciales["Usuario"] or user_deco["Contrasena"] != dicCredenciales["Contrasena"]:
            respuesta["Error"] = 'Token Invalido';
            return (flask.jsonify(respuesta), 401);

        aplicacion: cl_Cliente_Aplicacion = cl_Cliente_Aplicacion();
        respuesta["Response"] = "Ok";
        respuesta["Entidades"] = aplicacion.Listar(None);
        return flask.jsonify(respuesta);

    except Exception as ex:
        respuesta["Error"] = str(ex)
        return flask.jsonify(respuesta), 500

@app.route('/Servicios/Cliente/Insertar', methods=["POST"])
def Insertar_Cliente() -> str:
    respuesta = {}
    try:
        # Obtener el token desde el encabezado
        token = flask.request.headers.get("Token")

        # Validar que el token esté presente
        if not token:
            respuesta["Error"] = 'lbNoAutenticacion'
            return (flask.jsonify(respuesta), 401)

        #Decodificar Token
        user_deco = jwt.decode(token, key, algorithms=["HS256"])
        
        #Validar Usuario y Constraseña
        if user_deco["Usuario"] != dicCredenciales["Usuario"] or user_deco["Contrasena"] != dicCredenciales["Contrasena"]:
            respuesta["Error"] = 'Token Invalido';
            return (flask.jsonify(respuesta), 401);

        datos = flask.request.get_json();
        
        aplicacion: cl_Cliente_Aplicacion = cl_Cliente_Aplicacion();
        return flask.jsonify(aplicacion.Insertar(datos));

    except Exception as ex:
        respuesta["Error"] = str(ex)
        return flask.jsonify(respuesta), 500
    
@app.route('/Servicios/Cliente/Actualizar/<id>', methods=["PUT"])
def Actualizar_Cliente(id: str) -> str:
    respuesta = {}
    try:
        # Obtener el token desde el encabezado
        token = flask.request.headers.get("Token")

        # Validar que el token esté presente
        if not token:
            respuesta["Error"] = 'lbNoAutenticacion'
            return (flask.jsonify(respuesta), 401)

        #Decodificar Token
        user_deco = jwt.decode(token, key, algorithms=["HS256"])
        
        #Validar Usuario y Constraseña
        if user_deco["Usuario"] != dicCredenciales["Usuario"] or user_deco["Contrasena"] != dicCredenciales["Contrasena"]:
            respuesta["Error"] = 'Token Invalido';
            return (flask.jsonify(respuesta), 401);

        datos = flask.request.get_json();
        
        datos["ClienteID"] = id
        
        aplicacion: cl_Cliente_Aplicacion = cl_Cliente_Aplicacion();
        return flask.jsonify(aplicacion.Actualizar(datos));

    except Exception as ex:
        respuesta["Error"] = str(ex)
        return flask.jsonify(respuesta), 500

@app.route('/Servicios/Cliente/Eliminar/<id>', methods=["DELETE"])
def Eliminar_Cliente(id: str) -> str:
    respuesta = {}
    try:
        # Obtener el token desde el encabezado
        token = flask.request.headers.get("Token")

        # Validar que el token esté presente
        if not token:
            respuesta["Error"] = 'lbNoAutenticacion'
            return (flask.jsonify(respuesta), 401)

        #Decodificar Token
        user_deco = jwt.decode(token, key, algorithms=["HS256"])
        
        #Validar Usuario y Constraseña
        if user_deco["Usuario"] != dicCredenciales["Usuario"] or user_deco["Contrasena"] != dicCredenciales["Contrasena"]:
            respuesta["Error"] = 'Token Invalido';
            return (flask.jsonify(respuesta), 401);
        
        aplicacion: cl_Cliente_Aplicacion = cl_Cliente_Aplicacion();

        return flask.jsonify(aplicacion.Eliminar(id));

    except Exception as ex:
        respuesta["Error"] = str(ex)
        return flask.jsonify(respuesta), 500

@app.route('/Servicios/DetallesVenta/Listar/<id>', methods=["GET"])
def Listar_DetallesVenta_By_Id(id: str) -> str:
    respuesta = {}
    try:
        # Obtener el token desde el encabezado
        token = flask.request.headers.get("Token")

        # Validar que el token esté presente
        if not token:
            respuesta["Error"] = 'lbNoAutenticacion'
            return (flask.jsonify(respuesta), 401)

        #Decodificar Token
        user_deco = jwt.decode(token, key, algorithms=["HS256"])
        
        #Validar Usuario y Constraseña
        if user_deco["Usuario"] != dicCredenciales["Usuario"] or user_deco["Contrasena"] != dicCredenciales["Contrasena"]:
            respuesta["Error"] = 'Token Invalido';
            return (flask.jsonify(respuesta), 401);
        
        aplicacion: cl_DetalleVenta_Aplicacion = cl_DetalleVenta_Aplicacion();
        respuesta["Response"] = "Ok";
        respuesta["Entidades"] = aplicacion.Listar(id);
        return flask.jsonify(respuesta);

    except Exception as ex:
        respuesta["Error"] = str(ex)
        return flask.jsonify(respuesta), 500
    
@app.route('/Servicios/DetallesVenta/Listar', methods=["POST"])
def Listar_DetallesVenta() -> str:
    respuesta = {}
    try:
        # Obtener el token desde el encabezado
        token = flask.request.headers.get("Token")

        # Validar que el token esté presente
        if not token:
            respuesta["Error"] = 'lbNoAutenticacion'
            return (flask.jsonify(respuesta), 401)

        #Decodificar Token
        user_deco = jwt.decode(token, key, algorithms=["HS256"])
        
        #Validar Usuario y Constraseña
        if user_deco["Usuario"] != dicCredenciales["Usuario"] or user_deco["Contrasena"] != dicCredenciales["Contrasena"]:
            respuesta["Error"] = 'Token Invalido';
            return (flask.jsonify(respuesta), 401);

        aplicacion: cl_DetalleVenta_Aplicacion = cl_DetalleVenta_Aplicacion();
        respuesta["Response"] = "Ok";
        respuesta["Entidades"] = aplicacion.Listar(None);
        return flask.jsonify(respuesta);

    except Exception as ex:
        respuesta["Error"] = str(ex)
        return flask.jsonify(respuesta), 500

@app.route('/Servicios/DetallesVenta/Insertar', methods=["POST"])
def Insertar_DetallesVenta() -> str:
    respuesta = {}
    try:
        # Obtener el token desde el encabezado
        token = flask.request.headers.get("Token")

        # Validar que el token esté presente
        if not token:
            respuesta["Error"] = 'lbNoAutenticacion'
            return (flask.jsonify(respuesta), 401)

        #Decodificar Token
        user_deco = jwt.decode(token, key, algorithms=["HS256"])
        
        #Validar Usuario y Constraseña
        if user_deco["Usuario"] != dicCredenciales["Usuario"] or user_deco["Contrasena"] != dicCredenciales["Contrasena"]:
            respuesta["Error"] = 'Token Invalido';
            return (flask.jsonify(respuesta), 401);

        datos = flask.request.get_json();
        
        aplicacion: cl_DetalleVenta_Aplicacion = cl_DetalleVenta_Aplicacion();
        return flask.jsonify(aplicacion.Insertar(datos));

    except Exception as ex:
        respuesta["Error"] = str(ex)
        return flask.jsonify(respuesta), 500
    
@app.route('/Servicios/DetallesVenta/Actualizar/<id>', methods=["PUT"])
def Actualizar_DetallesVenta(id: str) -> str:
    respuesta = {}
    try:
        # Obtener el token desde el encabezado
        token = flask.request.headers.get("Token")

        # Validar que el token esté presente
        if not token:
            respuesta["Error"] = 'lbNoAutenticacion'
            return (flask.jsonify(respuesta), 401)

        #Decodificar Token
        user_deco = jwt.decode(token, key, algorithms=["HS256"])
        
        #Validar Usuario y Constraseña
        if user_deco["Usuario"] != dicCredenciales["Usuario"] or user_deco["Contrasena"] != dicCredenciales["Contrasena"]:
            respuesta["Error"] = 'Token Invalido';
            return (flask.jsonify(respuesta), 401);

        datos = flask.request.get_json();
        
        datos["DetalleVentaID"] = id
        
        aplicacion: cl_DetalleVenta_Aplicacion = cl_DetalleVenta_Aplicacion();
        return flask.jsonify(aplicacion.Actualizar(datos));

    except Exception as ex:
        respuesta["Error"] = str(ex)
        return flask.jsonify(respuesta), 500

@app.route('/Servicios/DetallesVenta/Eliminar/<id>', methods=["DELETE"])
def Eliminar_DetallesVenta(id: str) -> str:
    respuesta = {}
    try:
        # Obtener el token desde el encabezado
        token = flask.request.headers.get("Token")

        # Validar que el token esté presente
        if not token:
            respuesta["Error"] = 'lbNoAutenticacion'
            return (flask.jsonify(respuesta), 401)

        #Decodificar Token
        user_deco = jwt.decode(token, key, algorithms=["HS256"])
        
        #Validar Usuario y Constraseña
        if user_deco["Usuario"] != dicCredenciales["Usuario"] or user_deco["Contrasena"] != dicCredenciales["Contrasena"]:
            respuesta["Error"] = 'Token Invalido';
            return (flask.jsonify(respuesta), 401);
        
        aplicacion: cl_DetalleVenta_Aplicacion = cl_DetalleVenta_Aplicacion();

        return flask.jsonify(aplicacion.Eliminar(id));

    except Exception as ex:
        respuesta["Error"] = str(ex)
        return flask.jsonify(respuesta), 500

@app.route('/Servicios/MetodoPago/Listar/<id>', methods=["GET"])
def Listar_MetodoPago_By_Id(id: str) -> str:
    respuesta = {}
    try:
        # Obtener el token desde el encabezado
        token = flask.request.headers.get("Token")

        # Validar que el token esté presente
        if not token:
            respuesta["Error"] = 'lbNoAutenticacion'
            return (flask.jsonify(respuesta), 401)

        #Decodificar Token
        user_deco = jwt.decode(token, key, algorithms=["HS256"])
        
        #Validar Usuario y Constraseña
        if user_deco["Usuario"] != dicCredenciales["Usuario"] or user_deco["Contrasena"] != dicCredenciales["Contrasena"]:
            respuesta["Error"] = 'Token Invalido';
            return (flask.jsonify(respuesta), 401);
        
        aplicacion: cl_MetodoPago_Aplicacion = cl_MetodoPago_Aplicacion();
        respuesta["Response"] = "Ok";
        respuesta["Entidades"] = aplicacion.Listar(id);
        return flask.jsonify(respuesta);

    except Exception as ex:
        respuesta["Error"] = str(ex)
        return flask.jsonify(respuesta), 500

@app.route('/Servicios/MetodoPago/Listar', methods=["POST"])
def Listar_MetodosPago() -> str:
    respuesta = {}
    try:
        # Obtener el token desde el encabezado
        token = flask.request.headers.get("Token")

        # Validar que el token esté presente
        if not token:
            respuesta["Error"] = 'lbNoAutenticacion'
            return (flask.jsonify(respuesta), 401)

        #Decodificar Token
        user_deco = jwt.decode(token, key, algorithms=["HS256"])
        
        #Validar Usuario y Constraseña
        if user_deco["Usuario"] != dicCredenciales["Usuario"] or user_deco["Contrasena"] != dicCredenciales["Contrasena"]:
            respuesta["Error"] = 'Token Invalido';
            return (flask.jsonify(respuesta), 401);

        aplicacion: cl_MetodoPago_Aplicacion = cl_MetodoPago_Aplicacion();
        respuesta["Response"] = "Ok";
        respuesta["Entidades"] = aplicacion.Listar(None);
        return flask.jsonify(respuesta);

    except Exception as ex:
        respuesta["Error"] = str(ex)
        return flask.jsonify(respuesta), 500

@app.route('/Servicios/MetodoPago/Insertar', methods=["POST"])
def Insertar_MetodoPago() -> str:
    respuesta = {}
    try:
        # Obtener el token desde el encabezado
        token = flask.request.headers.get("Token")

        # Validar que el token esté presente
        if not token:
            respuesta["Error"] = 'lbNoAutenticacion'
            return (flask.jsonify(respuesta), 401)

        #Decodificar Token
        user_deco = jwt.decode(token, key, algorithms=["HS256"])
        
        #Validar Usuario y Constraseña
        if user_deco["Usuario"] != dicCredenciales["Usuario"] or user_deco["Contrasena"] != dicCredenciales["Contrasena"]:
            respuesta["Error"] = 'Token Invalido';
            return (flask.jsonify(respuesta), 401);

        datos = flask.request.get_json();
        
        aplicacion: cl_MetodoPago_Aplicacion = cl_MetodoPago_Aplicacion();
        return flask.jsonify(aplicacion.Insertar(datos));

    except Exception as ex:
        respuesta["Error"] = str(ex)
        return flask.jsonify(respuesta), 500

@app.route('/Servicios/MetodoPago/Actualizar/<id>', methods=["PUT"])
def Actualizar_MetodoPago(id: str) -> str:
    respuesta = {}
    try:
        # Obtener el token desde el encabezado
        token = flask.request.headers.get("Token")

        # Validar que el token esté presente
        if not token:
            respuesta["Error"] = 'lbNoAutenticacion'
            return (flask.jsonify(respuesta), 401)

        #Decodificar Token
        user_deco = jwt.decode(token, key, algorithms=["HS256"])
        
        #Validar Usuario y Constraseña
        if user_deco["Usuario"] != dicCredenciales["Usuario"] or user_deco["Contrasena"] != dicCredenciales["Contrasena"]:
            respuesta["Error"] = 'Token Invalido';
            return (flask.jsonify(respuesta), 401);

        datos = flask.request.get_json();
        
        datos["MetodoPagoID"] = id
        
        aplicacion: cl_MetodoPago_Aplicacion = cl_MetodoPago_Aplicacion();
        return flask.jsonify(aplicacion.Actualizar(datos));

    except Exception as ex:
        respuesta["Error"] = str(ex)
        return flask.jsonify(respuesta), 500

@app.route('/Servicios/MetodoPago/Eliminar/<id>', methods=["DELETE"])
def Eliminar_MetodoPago(id: str) -> str:
    respuesta = {}
    try:
        # Obtener el token desde el encabezado
        token = flask.request.headers.get("Token")

        # Validar que el token esté presente
        if not token:
            respuesta["Error"] = 'lbNoAutenticacion'
            return (flask.jsonify(respuesta), 401)

        #Decodificar Token
        user_deco = jwt.decode(token, key, algorithms=["HS256"])
        
        #Validar Usuario y Constraseña
        if user_deco["Usuario"] != dicCredenciales["Usuario"] or user_deco["Contrasena"] != dicCredenciales["Contrasena"]:
            respuesta["Error"] = 'Token Invalido';
            return (flask.jsonify(respuesta), 401);
        
        aplicacion: cl_MetodoPago_Aplicacion = cl_MetodoPago_Aplicacion();

        return flask.jsonify(aplicacion.Eliminar(id));

    except Exception as ex:
        respuesta["Error"] = str(ex)
        return flask.jsonify(respuesta), 500

@app.route('/Servicios/Producto/Listar/<id>', methods=["GET"])
def Listar_Producto_By_Id(id: str) -> str:
    respuesta = {}
    try:
        # Obtener el token desde el encabezado
        token = flask.request.headers.get("Token")

        # Validar que el token esté presente
        if not token:
            respuesta["Error"] = 'lbNoAutenticacion'
            return (flask.jsonify(respuesta), 401)

        #Decodificar Token
        user_deco = jwt.decode(token, key, algorithms=["HS256"])
        
        #Validar Usuario y Constraseña
        if user_deco["Usuario"] != dicCredenciales["Usuario"] or user_deco["Contrasena"] != dicCredenciales["Contrasena"]:
            respuesta["Error"] = 'Token Invalido';
            return (flask.jsonify(respuesta), 401);
        
        aplicacion: cl_Producto_Aplicacion = cl_Producto_Aplicacion();
        respuesta["Response"] = "Ok";
        respuesta["Entidades"] = aplicacion.Listar(id);
        return flask.jsonify(respuesta);

    except Exception as ex:
        respuesta["Error"] = str(ex)
        return flask.jsonify(respuesta), 500
    
@app.route('/Servicios/Producto/Listar', methods=["POST"])
def Listar_Producto() -> str:
    respuesta = {}
    try:
        # Obtener el token desde el encabezado
        token = flask.request.headers.get("Token")

        # Validar que el token esté presente
        if not token:
            respuesta["Error"] = 'lbNoAutenticacion'
            return (flask.jsonify(respuesta), 401)

        #Decodificar Token
        user_deco = jwt.decode(token, key, algorithms=["HS256"])
        
        #Validar Usuario y Constraseña
        if user_deco["Usuario"] != dicCredenciales["Usuario"] or user_deco["Contrasena"] != dicCredenciales["Contrasena"]:
            respuesta["Error"] = 'Token Invalido';
            return (flask.jsonify(respuesta), 401);

        aplicacion: cl_Producto_Aplicacion = cl_Producto_Aplicacion();
        respuesta["Response"] = "Ok";
        respuesta["Entidades"] = aplicacion.Listar(None);
        return flask.jsonify(respuesta);

    except Exception as ex:
        respuesta["Error"] = str(ex)
        return flask.jsonify(respuesta), 500

@app.route('/Servicios/Producto/Insertar', methods=["POST"])
def Insertar_Producto() -> str:
    respuesta = {}
    try:
        # Obtener el token desde el encabezado
        token = flask.request.headers.get("Token")

        # Validar que el token esté presente
        if not token:
            respuesta["Error"] = 'lbNoAutenticacion'
            return (flask.jsonify(respuesta), 401)

        #Decodificar Token
        user_deco = jwt.decode(token, key, algorithms=["HS256"])
        
        #Validar Usuario y Constraseña
        if user_deco["Usuario"] != dicCredenciales["Usuario"] or user_deco["Contrasena"] != dicCredenciales["Contrasena"]:
            respuesta["Error"] = 'Token Invalido';
            return (flask.jsonify(respuesta), 401);

        datos = flask.request.get_json();
        
        aplicacion: cl_Producto_Aplicacion = cl_Producto_Aplicacion();
        return flask.jsonify(aplicacion.Insertar(datos));

    except Exception as ex:
        respuesta["Error"] = str(ex)
        return flask.jsonify(respuesta), 500
    
@app.route('/Servicios/Producto/Actualizar/<id>', methods=["PUT"])
def Actualizar_Producto(id: str) -> str:
    respuesta = {}
    try:
        # Obtener el token desde el encabezado
        token = flask.request.headers.get("Token")

        # Validar que el token esté presente
        if not token:
            respuesta["Error"] = 'lbNoAutenticacion'
            return (flask.jsonify(respuesta), 401)

        #Decodificar Token
        user_deco = jwt.decode(token, key, algorithms=["HS256"])
        
        #Validar Usuario y Constraseña
        if user_deco["Usuario"] != dicCredenciales["Usuario"] or user_deco["Contrasena"] != dicCredenciales["Contrasena"]:
            respuesta["Error"] = 'Token Invalido';
            return (flask.jsonify(respuesta), 401);

        datos = flask.request.get_json();
        
        datos["ProductoID"] = id
        
        aplicacion: cl_Producto_Aplicacion = cl_Producto_Aplicacion();
        return flask.jsonify(aplicacion.Actualizar(datos));

    except Exception as ex:
        respuesta["Error"] = str(ex)
        return flask.jsonify(respuesta), 500

@app.route('/Servicios/Producto/Eliminar/<id>', methods=["DELETE"])
def Eliminar_Producto(id: str) -> str:
    respuesta = {}
    try:
        # Obtener el token desde el encabezado
        token = flask.request.headers.get("Token")

        # Validar que el token esté presente
        if not token:
            respuesta["Error"] = 'lbNoAutenticacion'
            return (flask.jsonify(respuesta), 401)

        #Decodificar Token
        user_deco = jwt.decode(token, key, algorithms=["HS256"])
        
        #Validar Usuario y Constraseña
        if user_deco["Usuario"] != dicCredenciales["Usuario"] or user_deco["Contrasena"] != dicCredenciales["Contrasena"]:
            respuesta["Error"] = 'Token Invalido';
            return (flask.jsonify(respuesta), 401);
        
        aplicacion: cl_Producto_Aplicacion = cl_Producto_Aplicacion();

        return flask.jsonify(aplicacion.Eliminar(id));

    except Exception as ex:
        respuesta["Error"] = str(ex)
        return flask.jsonify(respuesta), 500

@app.route('/Servicios/Proveedor/Listar/<id>', methods=["GET"])
def Listar_Proveedor_By_Id(id: str) -> str:
    respuesta = {}
    try:
        # Obtener el token desde el encabezado
        token = flask.request.headers.get("Token")

        # Validar que el token esté presente
        if not token:
            respuesta["Error"] = 'lbNoAutenticacion'
            return (flask.jsonify(respuesta), 401)

        #Decodificar Token
        user_deco = jwt.decode(token, key, algorithms=["HS256"])
        
        #Validar Usuario y Constraseña
        if user_deco["Usuario"] != dicCredenciales["Usuario"] or user_deco["Contrasena"] != dicCredenciales["Contrasena"]:
            respuesta["Error"] = 'Token Invalido';
            return (flask.jsonify(respuesta), 401);
        
        aplicacion: cl_Proveedor_Aplicacion = cl_Proveedor_Aplicacion();
        respuesta["Response"] = "Ok";
        respuesta["Entidades"] = aplicacion.Listar(id);
        return flask.jsonify(respuesta);

    except Exception as ex:
        respuesta["Error"] = str(ex)
        return flask.jsonify(respuesta), 500
    
@app.route('/Servicios/Proveedor/Listar', methods=["POST"])
def Listar_Proveedor() -> str:
    respuesta = {}
    try:
        # Obtener el token desde el encabezado
        token = flask.request.headers.get("Token")

        # Validar que el token esté presente
        if not token:
            respuesta["Error"] = 'lbNoAutenticacion'
            return (flask.jsonify(respuesta), 401)

        #Decodificar Token
        user_deco = jwt.decode(token, key, algorithms=["HS256"])
        
        #Validar Usuario y Constraseña
        if user_deco["Usuario"] != dicCredenciales["Usuario"] or user_deco["Contrasena"] != dicCredenciales["Contrasena"]:
            respuesta["Error"] = 'Token Invalido';
            return (flask.jsonify(respuesta), 401);

        aplicacion: cl_Proveedor_Aplicacion = cl_Proveedor_Aplicacion();
        respuesta["Response"] = "Ok";
        respuesta["Entidades"] = aplicacion.Listar(None);
        return flask.jsonify(respuesta);

    except Exception as ex:
        respuesta["Error"] = str(ex)
        return flask.jsonify(respuesta), 500

@app.route('/Servicios/Proveedor/Insertar', methods=["POST"])
def Insertar_Proveedor() -> str:
    respuesta = {}
    try:
        # Obtener el token desde el encabezado
        token = flask.request.headers.get("Token")

        # Validar que el token esté presente
        if not token:
            respuesta["Error"] = 'lbNoAutenticacion'
            return (flask.jsonify(respuesta), 401)

        #Decodificar Token
        user_deco = jwt.decode(token, key, algorithms=["HS256"])
        
        #Validar Usuario y Constraseña
        if user_deco["Usuario"] != dicCredenciales["Usuario"] or user_deco["Contrasena"] != dicCredenciales["Contrasena"]:
            respuesta["Error"] = 'Token Invalido';
            return (flask.jsonify(respuesta), 401);

        datos = flask.request.get_json();
        
        aplicacion: cl_Proveedor_Aplicacion = cl_Proveedor_Aplicacion();
        return flask.jsonify(aplicacion.Insertar(datos));

    except Exception as ex:
        respuesta["Error"] = str(ex)
        return flask.jsonify(respuesta), 500

@app.route('/Servicios/Proveedor/Actualizar/<id>', methods=["PUT"])
def Actualizar_Proveedor(id: str) -> str:
    respuesta = {}
    try:
        # Obtener el token desde el encabezado
        token = flask.request.headers.get("Token")

        # Validar que el token esté presente
        if not token:
            respuesta["Error"] = 'lbNoAutenticacion'
            return (flask.jsonify(respuesta), 401)

        #Decodificar Token
        user_deco = jwt.decode(token, key, algorithms=["HS256"])
        
        #Validar Usuario y Constraseña
        if user_deco["Usuario"] != dicCredenciales["Usuario"] or user_deco["Contrasena"] != dicCredenciales["Contrasena"]:
            respuesta["Error"] = 'Token Invalido';
            return (flask.jsonify(respuesta), 401);

        datos = flask.request.get_json();
        
        datos["ProveedorID"] = id
        
        aplicacion: cl_Proveedor_Aplicacion = cl_Proveedor_Aplicacion();
        return flask.jsonify(aplicacion.Actualizar(datos));

    except Exception as ex:
        respuesta["Error"] = str(ex)
        return flask.jsonify(respuesta), 500

@app.route('/Servicios/Proveedor/Eliminar/<id>', methods=["DELETE"])
def Eliminar_Proveedor(id: str) -> str:
    respuesta = {}
    try:
        # Obtener el token desde el encabezado
        token = flask.request.headers.get("Token")

        # Validar que el token esté presente
        if not token:
            respuesta["Error"] = 'lbNoAutenticacion'
            return (flask.jsonify(respuesta), 401)

        #Decodificar Token
        user_deco = jwt.decode(token, key, algorithms=["HS256"])
        
        #Validar Usuario y Constraseña
        if user_deco["Usuario"] != dicCredenciales["Usuario"] or user_deco["Contrasena"] != dicCredenciales["Contrasena"]:
            respuesta["Error"] = 'Token Invalido';
            return (flask.jsonify(respuesta), 401);
        
        aplicacion: cl_Proveedor_Aplicacion = cl_Proveedor_Aplicacion();

        return flask.jsonify(aplicacion.Eliminar(id));

    except Exception as ex:
        respuesta["Error"] = str(ex)
        return flask.jsonify(respuesta), 500
               
app.run('localhost', 4040);