import pyodbc;
from Utilidades.cl_Database import cl_Database; 
from Nucleo.cl_Producto import cl_Producto;

class cl_Producto_Repositorio:
    
    def Listar(self, id: str) -> dict:  
        respuesta = { };
        try:
            
            conexion = pyodbc.connect(cl_Database.strConnection);
            
            if(not id):
                consulta: str = f"CALL SP_Productos_Listar(NULL, @p_resultado);";
            else: 
                consulta: str = f"CALL SP_Productos_Listar({id}, @p_resultado);";
            
            cursor = conexion.cursor();
            cursor.execute(consulta);

            respuesta: dict = { };
            contador = 0;
            for elemento in cursor:
                
                producto: cl_Producto = cl_Producto();
                producto.SetProductoID(elemento[0]);
                producto.SetNombre(elemento[1]);
                producto.SetPrecio(elemento[2]);
                producto.SetStock(elemento[3]);
                respuesta[str(contador)] = producto.__dict__;
                contador = contador + 1;
                
            cursor.close();
            conexion.close();
            return respuesta;
        except Exception as ex:
            respuesta["Error"] = str(ex);
            return respuesta;
    
    def Insertar(self, producto: cl_Producto) -> dict:  
        respuesta = { };
        try:
            
            conexion = pyodbc.connect(cl_Database.strConnection);
            cursor = conexion.cursor();
            
            consulta: str = "{CALL SP_Productos_Insertar( ";
            consulta += "'" + producto.GetNombre() + "', " + str(producto.GetPrecio()) + ", " + str(producto.GetStock()) + ", @Resultado);}";
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
    
    def Actualizar(self, producto: cl_Producto) -> dict:  
        respuesta = { };
        try:
            
            conexion = pyodbc.connect(cl_Database.strConnection);
            cursor = conexion.cursor();
            
            consulta: str = "{CALL SP_Productos_Actualizar( ";
            consulta += "" + str(producto.GetProductoID()) + ", '" + producto.GetNombre() + "', " + str(producto.GetPrecio()) + ",";
            consulta += "" + str(producto.GetStock()) + "";
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
    
    def Eliminar(self, id: str) -> dict:  
        respuesta = { };
        try:
            
            conexion = pyodbc.connect(cl_Database.strConnection);
            cursor = conexion.cursor();
            
            consulta: str = f"CALL SP_Productos_Eliminar({id}, @Resultado);";
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