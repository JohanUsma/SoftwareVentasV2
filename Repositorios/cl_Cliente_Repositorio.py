import json
import pyodbc;
import datetime;
import jsonpickle;
from Utilidades.cl_Database import cl_Database; 
from Nucleo.cl_Cliente import cl_Cliente;


class cl_Cliente_Repositorio:
    
    def Listar(self, id: str) -> dict:  
        respuesta = { };
        try:
            
            conexion = pyodbc.connect(cl_Database.strConnection);
            
            if(not id):
                consulta: str = f"CALL SP_Clientes_Listar(NULL, @p_resultado);";
            else: 
                consulta: str = f"CALL SP_Clientes_Listar({id}, @p_resultado);";
            
            cursor = conexion.cursor();
            cursor.execute(consulta);

            respuesta: dict = { };
            contador = 0;
            for elemento in cursor:
                #LLENAR LISTA DE CLIENTES
                cliente: cl_Cliente = cl_Cliente();
                cliente.SetClienteID(elemento[0]);
                cliente.SetNombre(elemento[1]);
                cliente.SetApellido(elemento[2]);
                cliente.SetCorreo(elemento[3]);
                cliente.SetTelefono(elemento[4]);
                cliente.SetDireccion(elemento[5]);
                respuesta[str(contador)] = cliente.__dict__;
                contador = contador + 1;
                
            cursor.close();
            conexion.close();
            return respuesta;
        except Exception as ex:
            respuesta["Error"] = str(ex);
            return respuesta;