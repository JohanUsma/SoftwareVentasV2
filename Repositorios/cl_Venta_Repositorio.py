import json
import pyodbc;
import datetime;
import jsonpickle;
from Utilidades.cl_Database import cl_Database; 
from Nucleo.cl_Venta import cl_Venta;


class cl_Venta_Repositorio:
    
    def Listar(self, id: str) -> dict:  
        respuesta = { };
        try:
            
            conexion = pyodbc.connect(cl_Database.strConnection);
            
            if(not id):
                consulta: str = f"CALL SP_Ventas_Listar(NULL, @p_resultado);";
            else: 
                consulta: str = f"CALL SP_Ventas_Listar({id}, @p_resultado);";
            
            cursor = conexion.cursor();
            cursor.execute(consulta);

            respuesta: dict = { };
            contador = 0;
            for elemento in cursor:
                #LLENAR LISTA DE CLIENTES
                venta: cl_Venta = cl_Venta();
                venta.SetVentaID(elemento[0]);
                venta.SetClienteID(elemento[1]);
                venta.SetFecha(elemento[2]);
                venta.SetTotal(elemento[3]);
                respuesta[str(contador)] = venta.__dict__;
                contador = contador + 1;
                
            cursor.close();
            conexion.close();
            return respuesta;
        except Exception as ex:
            respuesta["Error"] = str(ex);
            return respuesta;

    def Insertar(self, venta: cl_Venta) -> dict:  
        respuesta = { };
        try:
            
            conexion = pyodbc.connect(cl_Database.strConnection);
            cursor = conexion.cursor();
            
            consulta: str = "{CALL SP_Ventas_Insertar( ";
            consulta += "" + str(venta.GetClienteID())+ ", '" + str(venta.GetFecha()) + "', ";
            consulta += "" + str(venta.GetTotal())  + ", @Resultado);}";
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

    def Actualizar(self, venta: cl_Venta) -> dict:  
        respuesta = { };
        try:
            
            conexion = pyodbc.connect(cl_Database.strConnection);
            cursor = conexion.cursor();
            
            consulta: str = "{CALL SP_Ventas_Actualizar( ";
            consulta += "" + str(venta.GetVentaID()) + ", " + str(venta.GetClienteID())+ ", '" + str(venta.GetFecha()) + "', ";
            consulta += "" + str(venta.GetTotal())  + ", @Resultado);}";
            #consulta += ", @Resultado);}";
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

    def Eliminar(self, id: str) -> dict:  
        respuesta = { };
        try:
            
            conexion = pyodbc.connect(cl_Database.strConnection);
            cursor = conexion.cursor();
            
            consulta: str = f"CALL SP_Ventas_Eliminar({id}, @Resultado);";
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