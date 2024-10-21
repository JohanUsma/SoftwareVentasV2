import sys
from ClasesT.cl_Database import cl_Database
import flask;
import datetime
from ClasesMN.cl_Cliente import cl_Cliente; 
from ClasesMN.cl_Venta import cl_Venta; 

objDatabase: cl_Database = cl_Database();
objDatabase.OpenConnectionDB();

parametros_cliente: list = ("Juan", "Pérez", "prueba@x.com", "Calle Falsa 123", "1234567890")
"""
parametros_cliente: list = ("Juan", "Pérez", "prueba@x.com", "Calle Falsa 123", "1234567890")
objDatabase.EjecutarSP("SP_Clientes_SIUD", "'INSERT'", "NULL", parametros_cliente)

parametros_cliente: list = ("Juan2", "Pérez2", "prueba@x.com", "Calle Falsa 123", "1234567890")
objDatabase.EjecutarSP("SP_Clientes_SIUD", "'UPDATE'", "14", parametros_cliente)

objDatabase.EjecutarSP("SP_Clientes_SIUD", "'DELETE'", "13", parametros_cliente)
"""

objDatabase.EjecutarSP("SP_Clientes_SIUD", "'SELECT'", "NULL", parametros_cliente)

"""
#OBJETO DE LA CLASE DATABSE
objDatabase: cl_Database = cl_Database.Database();

print("\n------------CONEXION BASE DE DATOS------------\n")

proceso: str = "x";

if(proceso == "marca"):
    print("\n------------PROCESO INSERTAR MARCA------------\n")
    
    #PARAMETROS PARA INSERTAR UNA MARCA
    nombre_m: str = "Marca_Prueba4";

    parametros: list = (nombre_m,);

    #LLAMADO DE LA FUNCION PARA INSERTAR UNA MARCA
    objDatabase.EjecutarSP("proc_insertar_marca", parametros);
    
    print("\n------------PROCESO CONSULTAR MARCAS------------\n")
    
    objDatabase.ConsultarMarcas();
else:
    print("\n------------PROCESO INSERTAR ZAPATO------------\n")
    #PARAMETROS PARA INSERTAR UN NUEVO ZAPATO
    modelo: str = "Prueba2";
    talla: str = 35;
    fecha_fabricacion: str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S");
    disponibilidad: str = 'false';
    id_marca: str = 4;

    parametros: list = (modelo, talla, fecha_fabricacion, disponibilidad, id_marca)
    
    #LLAMADO DE LA FUNCION PARA INSERTAR UN ZAPATO
    objDatabase.EjecutarSP("proc_insertar_zapato", parametros);
    
    print("\n------------PROCESO CONSULTAR ZAPATOS------------\n")
        
    #LLAMADO DE LA FUNCION CONSULTAR ZAPATO
    objDatabase.ConsultarZapatos();


print("\n------------CIERRE BASE DE DATOS------------\n")

#CIERRE DE CONEXIÓN A LA BASE DE DATOS
objDatabase.CloseConnectionDB();

"""