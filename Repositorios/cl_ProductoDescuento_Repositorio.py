import pyodbc;
from Utilidades.cl_Database import cl_Database; 
from Nucleo.cl_ProductoDescuento import cl_ProductoDescuento;

class cl_ProductoDescuento_Repositorio:
    
    def Listar(self, id: str) -> dict:  
        respuesta = { };
        try:
            
            conexion = pyodbc.connect(cl_Database.strConnection);
            
            if(not id):
                consulta: str = f"CALL SP_ProductosDescuentos_Listar(NULL, @p_resultado);";
            else: 
                consulta: str = f"CALL SP_ProductosDescuentos_Listar({id}, @p_resultado);";
            
            cursor = conexion.cursor();
            cursor.execute(consulta);

            respuesta: dict = { };
            contador = 0;
            for elemento in cursor:
                
                productoDescuento: cl_ProductoDescuento = cl_ProductoDescuento();
                productoDescuento.SetProductoDescuentoID(elemento[0]);
                productoDescuento.SetProductoID(elemento[1]);
                productoDescuento.SetDescuentoID(elemento[2]);
                respuesta[str(contador)] = productoDescuento.__dict__;
                contador = contador + 1;
                
            cursor.close();
            conexion.close();
            return respuesta;
        except Exception as ex:
            respuesta["Error"] = str(ex);
            return respuesta;
    
    def Insertar(self, productoDescuento: cl_ProductoDescuento) -> dict:  
        respuesta = { };
        try:
            
            conexion = pyodbc.connect(cl_Database.strConnection);
            cursor = conexion.cursor();
            
            consulta: str = "{CALL SP_ProductosDescuentos_Insertar( ";
            consulta += "" + str(productoDescuento.GetProductoID()) + ", " + str(productoDescuento.GetDescuentoID()) + ", @Resultado);}";
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
    
    def Actualizar(self, productoDescuento: cl_ProductoDescuento) -> dict:  
        respuesta = { };
        try:
            
            conexion = pyodbc.connect(cl_Database.strConnection);
            cursor = conexion.cursor();
            
            consulta: str = "{CALL SP_ProductosDescuentos_Actualizar( ";
            consulta += "" + str(productoDescuento.GetProductoDescuentoID()) + ", " + str(productoDescuento.GetProductoID()) + ", ";
            consulta += "" + str(productoDescuento.GetDescuentoID()) + ", @Resultado);}";
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
            
            consulta: str = f"CALL SP_ProductosDescuentos_Eliminar({id}, @Resultado);";
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