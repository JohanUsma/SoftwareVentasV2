import pyodbc;
from Utilidades.cl_Database import cl_Database; 
from Nucleo.cl_DetalleVenta import cl_DetalleVenta;

class cl_DetalleVenta_Repositorio:
    
    def Listar(self, id: str) -> dict:  
        respuesta = { };
        try:
            
            conexion = pyodbc.connect(cl_Database.strConnection);
            
            if(not id):
                consulta: str = f"CALL SP_DetallesVentas_Listar(NULL, @p_resultado);";
            else: 
                consulta: str = f"CALL SP_DetallesVentas_Listar({id}, @p_resultado);";
            
            cursor = conexion.cursor();
            cursor.execute(consulta);

            respuesta: dict = { };
            contador = 0;
            for elemento in cursor:
                #LLENAR LISTA DE CLIENTES
                detalleVenta: cl_DetalleVenta = cl_DetalleVenta();
                detalleVenta.SetDetalleVentaID(elemento[0]);
                detalleVenta.SetVentaID(elemento[1]);
                detalleVenta.SetProductoID(elemento[2]);
                detalleVenta.SetCantidad(elemento[3]);
                detalleVenta.SetPrecioUnitario(elemento[4]);
                respuesta[str(contador)] = detalleVenta.__dict__;
                contador = contador + 1;
                
            cursor.close();
            conexion.close();
            return respuesta;
        except Exception as ex:
            respuesta["Error"] = str(ex);
            return respuesta;
    
    def Insertar(self, detalleVenta: cl_DetalleVenta) -> dict:  
        respuesta = { };
        try:
            
            conexion = pyodbc.connect(cl_Database.strConnection);
            cursor = conexion.cursor();
            
            consulta: str = "{CALL SP_DetallesVentas_Insertar( ";
            consulta += "" + str(detalleVenta.GetVentaID()) + ", " + str(detalleVenta.GetProductoID())+ ", " + str(detalleVenta.GetCantidad()) + ", ";
            consulta += "" + str(detalleVenta.GetPrecioUnitario()) + ", @Resultado);}";
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
    
    def Actualizar(self, detalleVenta: cl_DetalleVenta) -> dict:  
        respuesta = { };
        try:
            
            conexion = pyodbc.connect(cl_Database.strConnection);
            cursor = conexion.cursor();
            
            consulta: str = "{CALL SP_DetallesVentas_Actualizar( ";
            consulta += "" + str(detalleVenta.GetDetalleVentaID()) + ", " + str(detalleVenta.GetVentaID()) + ", " + str(detalleVenta.GetProductoID()) + ", ";
            consulta += "" + str(detalleVenta.GetCantidad()) + ", " + str(detalleVenta.GetPrecioUnitario()) + ", @Resultado);}";
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
            
            consulta: str = f"CALL SP_DetallesVentas_Eliminar({id}, @Resultado);";
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