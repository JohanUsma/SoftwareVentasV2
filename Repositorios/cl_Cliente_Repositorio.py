import pyodbc;
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
    
    def Insertar(self, cliente: cl_Cliente) -> dict:  
        respuesta = { };
        try:
            
            conexion = pyodbc.connect(cl_Database.strConnection);
            cursor = conexion.cursor();
            
            consulta: str = "{CALL SP_Clientes_Insertar( ";
            consulta += "'" + cliente.GetNombre() + "', '" + cliente.GetApellido() + "', '" + cliente.GetCorreo() + "',";
            consulta += "'" + cliente.GetDireccion() + "', '" + cliente.GetTelefono() + "'";
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
    
    def Actualizar(self, cliente: cl_Cliente) -> dict:  
        respuesta = { };
        try:
            
            conexion = pyodbc.connect(cl_Database.strConnection);
            cursor = conexion.cursor();
            
            consulta: str = "{CALL SP_Clientes_Actualizar( ";
            consulta += "'" + cliente.GetClienteID() + "', '" + cliente.GetNombre() + "', '" + cliente.GetApellido() + "',";
            consulta += "'" + cliente.GetCorreo() + "','" + cliente.GetDireccion() + "', '" + cliente.GetTelefono() + "'";
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
            
            consulta: str = f"CALL SP_Clientes_Eliminar({id}, @Resultado);";
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