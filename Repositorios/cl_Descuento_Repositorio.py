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
                descuento: cl_Descuento = cl_Descuento();
                descuento.SetDescuentoID(elemento[0]);
                descuento.SetNombre(elemento[1]);
                descuento.SetDescripcion(elemento[2]);
                descuento.SetPorcentaje(elemento[3]);               
                respuesta[str(contador)] = descuento.__dict__;
                contador = contador + 1;
                
            cursor.close();
            conexion.close();
            return respuesta;
        except Exception as ex:
            respuesta["Error"] = str(ex);
            return respuesta;
    
    def Insertar(self, descuento: cl_Descuento) -> dict:  
        respuesta = { };
        try:
            
            conexion = pyodbc.connect(cl_Database.strConnection);
            cursor = conexion.cursor();
            
            consulta: str = "{CALL SP_Descuentos_Insertar( ";
            consulta += "'" + descuento.GetNombre() + "', '" + descuento.GetDescripcion() + "', " + descuento.GetPorcentaje();
            consulta += ", @Resultado);}";
            cursor.execute(consulta);
            
            consulta: str = "SELECT @Resultado;";
            cursor.execute(consulta);
            respuesta["Resultado"] = str(cursor.fetchone()[0]);
            cursor.execute("commit;");

            cursor.close();
            conexion.close();
            return respuesta;
        except Exception as ex:
            respuesta["Error"] = str(ex);
            return respuesta;