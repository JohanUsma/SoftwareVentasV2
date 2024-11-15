import datetime;
import decimal;
from Repositorios.cl_Cliente_Repositorio import cl_Cliente_Repositorio;

class cl_Cliente_Aplicacion:

    def __init__(self):
        self.respositorio = cl_Cliente_Repositorio();

    def Listar(self, id: str) -> None:
        return self.respositorio.Listar(id);