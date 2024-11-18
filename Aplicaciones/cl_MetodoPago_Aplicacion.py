from Nucleo.cl_MetodoPago import cl_MetodoPago;
from Repositorios.cl_MetodoPago_Repositorio import cl_MetodoPago_Repositorio;

class cl_MetodoPago_Aplicacion:

    def __init__(self):
        self.respositorio = cl_MetodoPago_Repositorio();

    def Listar(self, id: str) -> None:
        return self.respositorio.Listar(id);
    
    def Insertar(self, datos: dict) -> None:
        respuesta: dict = { };

        if(not "Nombre" in datos.keys()): 
            
            respuesta["Error"] = "Falta informacion";
            return respuesta;
        
        metodoPago: cl_MetodoPago = cl_MetodoPago();
        metodoPago.SetNombre(datos["Nombre"]);

        return self.respositorio.Insertar(metodoPago);
    
    def Actualizar(self, datos: dict) -> None:
        respuesta: dict = { };

        if(not "MetodoPagoID" in datos.keys() or
           not "Nombre" in datos.keys()): 
            
            respuesta["Error"] = "Falta informacion";
            return respuesta;
        
        metodoPago: cl_MetodoPago = cl_MetodoPago();
        metodoPago.SetMetodoPagoID(datos["MetodoPagoID"]);
        metodoPago.SetNombre(datos["Nombre"]);

        return self.respositorio.Actualizar(metodoPago);

    def Eliminar(self, id: str) -> None:
        return self.respositorio.Eliminar(id);