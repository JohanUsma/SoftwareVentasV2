from Nucleo.cl_Venta import cl_Venta;
from Repositorios.cl_Venta_Repositorio import cl_Venta_Repositorio;

class cl_Venta_Aplicacion:

    def __init__(self):
        self.respositorio = cl_Venta_Repositorio();

    def Listar(self, id: str) -> None:
        return self.respositorio.Listar(id);

    def Insertar(self, datos: dict) -> None:
        respuesta: dict = { };

        if(not "ClienteID" in datos.keys() or 
           not "Fecha" in datos.keys() or 
           not "Total" in datos.keys()): 
                    
            respuesta["Error"] = "Falta informacion";
            return respuesta;
        
        venta: cl_Venta = cl_Venta();
        venta.SetClienteID(datos["ClienteID"]);
        venta.SetFecha(datos["Fecha"]);
        venta.SetTotal(datos["Total"]);

        return self.respositorio.Insertar(venta);

    def Actualizar(self, datos: dict) -> None:
            respuesta: dict = { };

            if(not "VentaID" in datos.keys() or
                not "ClienteID" in datos.keys() or 
                not "Fecha" in datos.keys() or 
                not "Total" in datos.keys()): 
                
                respuesta["Error"] = "Falta informacion";
                return respuesta;
            
            venta: cl_Venta = cl_Venta();
            venta.SetVentaID(datos["VentaID"]);
            venta.SetClienteID(datos["ClienteID"]);
            venta.SetFecha(datos["Fecha"]);
            venta.SetTotal(datos["Total"]);

            return self.respositorio.Actualizar(venta);

    def Eliminar(self, id: str) -> None:
        return self.respositorio.Eliminar(id);