from Nucleo.cl_Venta import cl_Venta;
from Repositorios.cl_Venta_Repositorio import cl_Venta_Repositorio;

class cl_Venta_Aplicacion:

    def __init__(self):
        self.respositorio = cl_Venta_Repositorio();

    def Listar(self, id: str) -> None:
        return self.respositorio.Listar(id);