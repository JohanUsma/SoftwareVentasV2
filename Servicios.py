import flask;
import jwt
from Aplicaciones.cl_Cliente_Aplicacion import cl_Cliente_Aplicacion;
from Aplicaciones.cl_Descuento_Aplicacion import cl_Descuento_Aplicacion;
from Aplicaciones.cl_DetalleVenta_Aplicacion import cl_DetalleVenta_Aplicacion
from Aplicaciones.cl_Empleado_Aplicacion import cl_Empleado_Aplicacion
from Aplicaciones.cl_MetodoPago_Aplicacion import cl_MetodoPago_Aplicacion
from Aplicaciones.cl_Pago_Aplicacion import cl_Pago_Aplicacion
from Aplicaciones.cl_ProductoDescuento_Aplicacion import cl_ProductoDescuento_Aplicacion

key = "KJhisdy8787798udfsd56f4s5d4fsdf";
dicCredenciales = {"Usuario": "Prueba", "Contrasena": "1234568"}

print(__name__);
app = flask.Flask(__name__);

#######################################
##       SERVICIOS API - CLIENTE     ##
#######################################

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

#######################################
##     SERVICIOS API - DESCUENTOS    ##
#######################################

@app.route('/Servicios/Descuento/Listar/<id>', methods=["GET"])
def Listar_Descuento_By_Id(id: str) -> str:
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
        
        aplicacion: cl_Descuento_Aplicacion = cl_Descuento_Aplicacion();
        respuesta["Response"] = "Ok";
        respuesta["Entidades"] = aplicacion.Listar(id);
        return flask.jsonify(respuesta);

    except Exception as ex:
        respuesta["Error"] = str(ex)
        return flask.jsonify(respuesta), 500

@app.route('/Servicios/Descuento/Listar', methods=["POST"])
def Listar_Descuento() -> str:
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

        aplicacion: cl_Descuento_Aplicacion = cl_Descuento_Aplicacion();
        respuesta["Response"] = "Ok";
        respuesta["Entidades"] = aplicacion.Listar(None);
        return flask.jsonify(respuesta);

    except Exception as ex:
        respuesta["Error"] = str(ex)
        return flask.jsonify(respuesta), 500

@app.route('/Servicios/Descuento/Insertar', methods=["POST"])
def Insertar_Descuento() -> str:
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
        
        aplicacion: cl_Descuento_Aplicacion = cl_Descuento_Aplicacion();
        return flask.jsonify(aplicacion.Insertar(datos));

    except Exception as ex:
        respuesta["Error"] = str(ex)
        return flask.jsonify(respuesta), 500

@app.route('/Servicios/Descuento/Actualizar/<id>', methods=["PUT"])
def Actualizar_Descuento(id: str) -> str:
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
        
        datos["DescuentoID"] = id
        
        aplicacion: cl_Descuento_Aplicacion = cl_Descuento_Aplicacion();
        return flask.jsonify(aplicacion.Actualizar(datos));

    except Exception as ex:
        respuesta["Error"] = str(ex)
        return flask.jsonify(respuesta), 500

@app.route('/Servicios/Descuento/Eliminar/<id>', methods=["DELETE"])
def Eliminar_Descuento(id: str) -> str:
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
        
        aplicacion: cl_Descuento_Aplicacion = cl_Descuento_Aplicacion();

        return flask.jsonify(aplicacion.Eliminar(id));

    except Exception as ex:
        respuesta["Error"] = str(ex)
        return flask.jsonify(respuesta), 500

#######################################
##   SERVICIOS API - DETALLE VENTAS  ##
#######################################

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

#######################################
##      SERVICIOS API - EMPLEADO     ##
#######################################

@app.route('/Servicios/Empleado/Listar/<id>', methods=["GET"])
def Listar_Empleado_By_Id(id: str) -> str:
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
        
        aplicacion: cl_Empleado_Aplicacion = cl_Empleado_Aplicacion();
        respuesta["Response"] = "Ok";
        respuesta["Entidades"] = aplicacion.Listar(id);
        return flask.jsonify(respuesta);

    except Exception as ex:
        respuesta["Error"] = str(ex)
        return flask.jsonify(respuesta), 500

@app.route('/Servicios/Empleado/Listar', methods=["POST"])
def Listar_Empleado() -> str:
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

        aplicacion: cl_Empleado_Aplicacion = cl_Empleado_Aplicacion();
        respuesta["Response"] = "Ok";
        respuesta["Entidades"] = aplicacion.Listar(None);
        return flask.jsonify(respuesta);

    except Exception as ex:
        respuesta["Error"] = str(ex)
        return flask.jsonify(respuesta), 500

@app.route('/Servicios/Empleado/Insertar', methods=["POST"])
def Insertar_Empleado() -> str:
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
        
        aplicacion: cl_Empleado_Aplicacion = cl_Empleado_Aplicacion();
        return flask.jsonify(aplicacion.Insertar(datos));

    except Exception as ex:
        respuesta["Error"] = str(ex)
        return flask.jsonify(respuesta), 500

@app.route('/Servicios/Empleado/Actualizar/<id>', methods=["PUT"])
def Actualizar_Empleado(id: str) -> str:
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
        
        datos["EmpleadoID"] = id
        
        aplicacion: cl_Empleado_Aplicacion = cl_Empleado_Aplicacion();
        return flask.jsonify(aplicacion.Actualizar(datos));

    except Exception as ex:
        respuesta["Error"] = str(ex)
        return flask.jsonify(respuesta), 500

@app.route('/Servicios/Empleado/Eliminar/<id>', methods=["DELETE"])
def Eliminar_Empleado(id: str) -> str:
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
        
        aplicacion: cl_Empleado_Aplicacion = cl_Empleado_Aplicacion();

        return flask.jsonify(aplicacion.Eliminar(id));

    except Exception as ex:
        respuesta["Error"] = str(ex)
        return flask.jsonify(respuesta), 500

#######################################
##    SERVICIOS API - METODO PAGO    ##
#######################################

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

#######################################
##        SERVICIOS API - PAGO       ##
#######################################

@app.route('/Servicios/Pago/Listar/<id>', methods=["GET"])
def Listar_Pago_By_Id(id: str) -> str:
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
        
        aplicacion: cl_Pago_Aplicacion = cl_Pago_Aplicacion();
        respuesta["Response"] = "Ok";
        respuesta["Entidades"] = aplicacion.Listar(id);
        return flask.jsonify(respuesta);

    except Exception as ex:
        respuesta["Error"] = str(ex)
        return flask.jsonify(respuesta), 500

@app.route('/Servicios/Pago/Listar', methods=["POST"])
def Listar_Pagos() -> str:
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

        aplicacion: cl_Pago_Aplicacion = cl_Pago_Aplicacion();
        respuesta["Response"] = "Ok";
        respuesta["Entidades"] = aplicacion.Listar(None);
        return flask.jsonify(respuesta);

    except Exception as ex:
        respuesta["Error"] = str(ex)
        return flask.jsonify(respuesta), 500

@app.route('/Servicios/Pago/Insertar', methods=["POST"])
def Insertar_Pago() -> str:
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
        
        aplicacion: cl_Pago_Aplicacion = cl_Pago_Aplicacion();
        return flask.jsonify(aplicacion.Insertar(datos));

    except Exception as ex:
        respuesta["Error"] = str(ex)
        return flask.jsonify(respuesta), 500
    
@app.route('/Servicios/Pago/Actualizar/<id>', methods=["PUT"])
def Actualizar_Pago(id: str) -> str:
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
        
        datos["PagoID"] = id
        
        aplicacion: cl_Pago_Aplicacion = cl_Pago_Aplicacion();
        return flask.jsonify(aplicacion.Actualizar(datos));

    except Exception as ex:
        respuesta["Error"] = str(ex)
        return flask.jsonify(respuesta), 500

@app.route('/Servicios/Pago/Eliminar/<id>', methods=["DELETE"])
def Eliminar_Pago(id: str) -> str:
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
        
        aplicacion: cl_Pago_Aplicacion = cl_Pago_Aplicacion();

        return flask.jsonify(aplicacion.Eliminar(id));

    except Exception as ex:
        respuesta["Error"] = str(ex)
        return flask.jsonify(respuesta), 500

#######################################
##      SERVICIOS API - PRODUCTO     ##
#######################################



#######################################
##   SERVICIOS API - PRODUCTO DESC   ##
#######################################

@app.route('/Servicios/ProductoDescuento/Listar/<id>', methods=["GET"])
def Listar_ProductoDescuento_By_Id(id: str) -> str:
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
        
        aplicacion: cl_ProductoDescuento_Aplicacion = cl_ProductoDescuento_Aplicacion();
        respuesta["Response"] = "Ok";
        respuesta["Entidades"] = aplicacion.Listar(id);
        return flask.jsonify(respuesta);

    except Exception as ex:
        respuesta["Error"] = str(ex)
        return flask.jsonify(respuesta), 500

@app.route('/Servicios/ProductoDescuento/Listar', methods=["POST"])
def Listar_ProductosDescuentos() -> str:
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

        aplicacion: cl_ProductoDescuento_Aplicacion = cl_ProductoDescuento_Aplicacion();
        respuesta["Response"] = "Ok";
        respuesta["Entidades"] = aplicacion.Listar(None);
        return flask.jsonify(respuesta);

    except Exception as ex:
        respuesta["Error"] = str(ex)
        return flask.jsonify(respuesta), 500

@app.route('/Servicios/ProductoDescuento/Insertar', methods=["POST"])
def Insertar_ProductoDescuento() -> str:
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
        
        aplicacion: cl_ProductoDescuento_Aplicacion = cl_ProductoDescuento_Aplicacion();
        return flask.jsonify(aplicacion.Insertar(datos));

    except Exception as ex:
        respuesta["Error"] = str(ex)
        return flask.jsonify(respuesta), 500
    
@app.route('/Servicios/ProductoDescuento/Actualizar/<id>', methods=["PUT"])
def Actualizar_ProductoDescuento(id: str) -> str:
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
        
        datos["ProductoDescuentoID"] = id
        
        aplicacion: cl_ProductoDescuento_Aplicacion = cl_ProductoDescuento_Aplicacion();
        return flask.jsonify(aplicacion.Actualizar(datos));

    except Exception as ex:
        respuesta["Error"] = str(ex)
        return flask.jsonify(respuesta), 500

@app.route('/Servicios/ProductoDescuento/Eliminar/<id>', methods=["DELETE"])
def Eliminar_ProductoDescuento(id: str) -> str:
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
        
        aplicacion: cl_ProductoDescuento_Aplicacion = cl_ProductoDescuento_Aplicacion();

        return flask.jsonify(aplicacion.Eliminar(id));

    except Exception as ex:
        respuesta["Error"] = str(ex)
        return flask.jsonify(respuesta), 500


#######################################
##      SERVICIOS API - PROVEEDOR    ##
#######################################



#######################################
##       SERVICIOS API - VENTA       ##
#######################################


app.run('localhost', 4040);