import pyodbc;
from Utilidades.cl_Database import cl_Database; 
from Nucleo.cl_Empleado import cl_Empleado;


class cl_Empleado_Repositorio:
    
    def Listar(self, id: str) -> dict:  
        respuesta = { };
        try:
            
            conexion = pyodbc.connect(cl_Database.strConnection);
            
            if(not id):
                consulta: str = f"CALL SP_Empleados_Listar(NULL, @p_resultado);";
            else: 
                consulta: str = f"CALL SP_Empleados_Listar({id}, @p_resultado);";
            
            cursor = conexion.cursor();
            cursor.execute(consulta);

            respuesta: dict = { };
            contador = 0;
            for elemento in cursor:
                #LLENAR LISTA DE CLIENTES
                empleado: cl_Empleado = cl_Empleado();
                empleado.SetEmpleadoID(elemento[0]);
                empleado.SetNombre(elemento[1]);
                empleado.SetApellido(elemento[2]);
                empleado.SetCorreo(elemento[3]);
                empleado.SetTelefono(elemento[4]);
                respuesta[str(contador)] = empleado.__dict__;
                contador = contador + 1;
                
            cursor.close();
            conexion.close();
            return respuesta;
        except Exception as ex:
            respuesta["Error"] = str(ex);
            return respuesta;

    def Insertar(self, empleado: cl_Empleado) -> dict:  
        respuesta = { };
        try:
            
            conexion = pyodbc.connect(cl_Database.strConnection);
            cursor = conexion.cursor();
            
            consulta: str = "{CALL SP_Empleados_Insertar( ";
            consulta += "'" + empleado.GetNombre() + "', '" + empleado.GetApellido() + "', '" + empleado.GetCorreo() + "',";
            consulta += "'" + empleado.GetTelefono() + "'";
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
    
    def Actualizar(self, empleado: cl_Empleado) -> dict:  
        respuesta = { };
        try:
            
            conexion = pyodbc.connect(cl_Database.strConnection);
            cursor = conexion.cursor();
            
            consulta: str = "{CALL SP_Empleados_Actualizar( ";
            consulta += "'" + empleado.GetEmpleadoID() + "', '" + empleado.GetNombre() + "', '" + empleado.GetApellido() + "',";
            consulta += "'" + empleado.GetCorreo() + "','" + empleado.GetTelefono() + "'";
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
                
                consulta: str = f"CALL SP_Empleados_Eliminar({id}, @Resultado);";
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