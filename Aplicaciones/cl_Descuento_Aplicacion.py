import datetime;
import decimal;
from Nucleo.cl_Descuento import cl_Descuento;
from Repositorios.cl_Descuento_Repositorio import cl_Descuento_Repositorio;

class cl_Descuento_Aplicacion:

    def __init__(self):
        self.respositorio = cl_Descuento_Repositorio();

    def Listar(self, id: str) -> None:
        return self.respositorio.Listar(id);