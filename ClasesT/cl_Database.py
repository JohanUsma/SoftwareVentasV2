from flask import app
import pyodbc;
import datetime;
import flask;
from ClasesMN.cl_Cliente import cl_Cliente;

class cl_Database:
  
  def __init__(self):
    self.strConnection: str = """
        Driver={MySQL ODBC 9.0 Unicode Driver};
        Server=localhost;
        Database=sventas_pe;
        PORT=3306;
        user=user_ptyhon;
        password=Clas3s1Nt2024_!""";
    
    self.conexion = None;
  
  def OpenConnectionDB(self) -> None:  
    try:
      self.conexion = pyodbc.connect(self.strConnection);
      print("Conexión a la Base de Datos Exitosa");
    except Exception as e:
      print("Conexión a la Base de Datos Fallida: "+str(e));
        
  def CloseConnectionDB(self) -> None:  
    try:
      self.conexion.close();
      print("Cierre de la Base de Datos Exitosa");
    except Exception as e:
      print("Cierre de la Base de Datos Fallida: "+str(e));

  def EjecutarSP(self, nombreSp: str, accion: str, id: int, parametros: list)-> None:

    #GENERAMOS LOS MARCADORES PARA LOS ATRIBUTOS DEL SP
    marcadores: list = ','.join(["'%s'" for _ in parametros]);
    
    #CONSTRUCCIÓN DEL QUERY
    consulta = f"CALL {nombreSp}({accion},{id},{marcadores}, @p_resultado);";

    try:
      #EJECUCIÓN PROCEDURE
      cursor = self.conexion.cursor();
      cursor.execute(consulta % parametros);
      
      #SELECCIÓN DE RESULTADO
      if("SELECT" not in accion):
        cursor.execute("SELECT @p_resultado;");
        resultado = cursor.fetchone()[0];
        print("Resultado:", resultado);
      else: 
        #RECORRIDO DEL RESULTADO PARA TRABAJAR CON OBJETOS
        if(nombreSp == "SP_Clientes_SIUD"):
          ls_clientes: list = [];
          for elemento in cursor:
            cliente: cl_Cliente = cl_Cliente();
            cliente.SetClienteID(elemento[0]);
            cliente.SetNombre(elemento[1]);
            cliente.SetApellido(elemento[2]);
            cliente.SetCorreo(elemento[3]);
            cliente.SetTelefono(elemento[4]);
            cliente.SetDireccion(elemento[5]);
                
            ls_clientes.append(cliente);
            
          for c in ls_clientes:
            print(  str(c.GetClienteID()) + " - " + 
                    c.GetNombre() + " - " + 
                    c.GetApellido() + " - " + 
                    c.GetCorreo() + " - " + 
                    c.GetTelefono() + " - " + 
                    c.GetDireccion());
            
    except Exception as Error:
      cursor.execute("SELECT @p_resultado;");
      resultado = str(Error);
      print("Resultado:", resultado);
      
    #CIERRE DE TRANSACCIÓN
    cursor.execute("COMMIT;");
    cursor.close();