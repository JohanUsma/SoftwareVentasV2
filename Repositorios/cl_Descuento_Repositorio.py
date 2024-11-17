import json
import pyodbc;
import datetime;
import jsonpickle;
from Utilidades.cl_Database import cl_Database; 
from Nucleo.cl_Descuento import cl_Descuento;


class cl_Descuento_Repositorio:
    
    def Listar(self, id: str) -> dict:  
        respuesta = { };
        try:
            
            conexion = pyodbc.connect(cl_Database.strConnection);
            
            if(not id):
                consulta: str = f"CALL SP_Descuentos_Listar(NULL, @p_resultado);";
            else: 
                consulta: str = f"CALL SP_Descuentos_Listar({id}, @p_resultado);";
            
            cursor = conexion.cursor();
            cursor.execute(consulta);

            respuesta: dict = { };
            contador = 0;
            for elemento in cursor:
                #LLENAR LISTA DE CLIENTES
                desccuento: cl_Descuento = cl_Descuento();
                desccuento.SetDescuentoID(elemento[0]);
                desccuento.SetNombre(elemento[1]);
                desccuento.SetDescripcion(elemento[2]);
                desccuento.SetPorcentaje(elemento[3]);               
                respuesta[str(contador)] = desccuento.__dict__;
                contador = contador + 1;
                
            cursor.close();
            conexion.close();
            return respuesta;
        except Exception as ex:
            respuesta["Error"] = str(ex);
            return respuesta;
    
    