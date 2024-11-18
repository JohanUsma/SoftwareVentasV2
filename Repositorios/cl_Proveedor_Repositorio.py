import pyodbc;
from Utilidades.cl_Database import cl_Database; 
from Nucleo.cl_Proveedor import cl_Proveedor;

class cl_Proveedor_Repositorio:
    
    def Listar(self, id: str) -> dict:  
        respuesta = { };
        try:
            
            conexion = pyodbc.connect(cl_Database.strConnection);
            
            if(not id):
                consulta: str = f"CALL SP_Proveedores_Listar(NULL, @p_resultado);";
            else: 
                consulta: str = f"CALL SP_Proveedores_Listar({id}, @p_resultado);";
            
            cursor = conexion.cursor();
            cursor.execute(consulta);

            respuesta: dict = { };
            contador = 0;
            for elemento in cursor:
                
                proveedor: cl_Proveedor = cl_Proveedor();
                proveedor.SetProveedorID(elemento[0]);
                proveedor.SetNombre(elemento[1]);
                proveedor.SetContacto(elemento[2]);
                proveedor.SetTelefono(elemento[3]);
                respuesta[str(contador)] = proveedor.__dict__;
                contador = contador + 1;
                
            cursor.close();
            conexion.close();
            return respuesta;
        except Exception as ex:
            respuesta["Error"] = str(ex);
            return respuesta;

    def Insertar(self, proveedor: cl_Proveedor) -> dict:  
        respuesta = { };
        try:
            
            conexion = pyodbc.connect(cl_Database.strConnection);
            cursor = conexion.cursor();
            
            consulta: str = "{CALL SP_Proveedores_Insertar( ";
            consulta += "'" + proveedor.GetNombre() + "', '" + proveedor.GetContacto() + "', '" + proveedor.GetTelefono() + "', @Resultado);}";
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
    
    def Actualizar(self, proveedor: cl_Proveedor) -> dict:  
        respuesta = { };
        try:
            
            conexion = pyodbc.connect(cl_Database.strConnection);
            cursor = conexion.cursor();
            
            consulta: str = "{CALL SP_Proveedores_Actualizar( ";
            consulta += "" + str(proveedor.GetProveedorID()) + ", '" + proveedor.GetNombre() + "', '" + proveedor.GetContacto() + "',";
            consulta += "'" + proveedor.GetTelefono() + "', @Resultado);}";
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
                
                consulta: str = f"CALL SP_Proveedores_Eliminar({id}, @Resultado);";
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