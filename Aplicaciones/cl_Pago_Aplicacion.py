from Nucleo.cl_Pago import cl_Pago;
from Repositorios.cl_Pago_Repositorio import cl_Pago_Repositorio;

class cl_Pago_Aplicacion:

    def __init__(self):
        self.respositorio = cl_Pago_Repositorio();

    def Listar(self, id: str) -> None:
        return self.respositorio.Listar(id);
    
    def Insertar(self, datos: dict) -> None:
        respuesta: dict = { };

        if(not "VentaID" in datos.keys() or 
           not "MetodoPagoID" in datos.keys() or 
           not "Monto" in datos.keys()): 
            
            respuesta["Error"] = "Falta informacion";
            return respuesta;
        
        pago: cl_Pago = cl_Pago();
        pago.SetVentaID(datos["VentaID"]);
        pago.SetMetodoPagoID(datos["MetodoPagoID"]);
        pago.SetMonto(datos["Monto"]);

        return self.respositorio.Insertar(pago);
    
    def Actualizar(self, datos: dict) -> None:
        respuesta: dict = { };

        if(not "PagoID" in datos.keys() or
           not "VentaID" in datos.keys() or 
           not "MetodoPagoID" in datos.keys() or 
           not "Monto" in datos.keys()): 
            
            respuesta["Error"] = "Falta informacion";
            return respuesta;
        
        pago: cl_Pago = cl_Pago();
        pago.SetPagoID(datos["PagoID"]);
        pago.SetVentaID(datos["VentaID"]);
        pago.SetMetodoPagoID(datos["MetodoPagoID"]);
        pago.SetMonto(datos["Monto"]);

        return self.respositorio.Actualizar(pago);

    def Eliminar(self, id: str) -> None:
        return self.respositorio.Eliminar(id);