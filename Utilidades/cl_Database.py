import pyodbc;

class cl_Database:
  strConnection: str = """
    Driver={MySQL ODBC 9.1 Unicode Driver};
    Server=localhost;
    Database=sventas_pe;
    PORT=3306;
    user=user_ptyhon;
    password=Clas3s1Nt2024_!""";