import pyodbc;

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