from Nucleo.cl_Cliente import cl_Cliente;
from Nucleo.cl_DetalleVenta import cl_DetalleVenta;
from Repositorios.cl_Cliente_Repositorio import cl_Cliente_Repositorio;
from Repositorios.cl_DetalleVenta_Repositorio import cl_DetalleVenta_Repositorio;

class cl_DetalleVenta_Aplicacion:

    def __init__(self):
        self.respositorio = cl_DetalleVenta_Repositorio();

    def Listar(self, id: str) -> None:
        return self.respositorio.Listar(id);
    
    def Insertar(self, datos: dict) -> None:
        respuesta: dict = { };

        if(not "VentaID" in datos.keys() or 
           not "ProductoID" in datos.keys() or 
           not "Cantidad" in datos.keys() or 
           not "PrecioUnitario" in datos.keys()): 
            
            respuesta["Error"] = "Falta informacion";
            return respuesta;
        
        detalleVenta: cl_DetalleVenta = cl_DetalleVenta();
        detalleVenta.SetVentaID(datos["VentaID"]);
        detalleVenta.SetProductoID(datos["ProductoID"]);
        detalleVenta.SetCantidad(datos["Cantidad"]);
        detalleVenta.SetPrecioUnitario(datos["PrecioUnitario"]);

        return self.respositorio.Insertar(detalleVenta);
    
    def Actualizar(self, datos: dict) -> None:
        respuesta: dict = { };

        if(not "DetalleVentaID" in datos.keys() or 
           not "VentaID" in datos.keys() or 
           not "ProductoID" in datos.keys() or 
           not "Cantidad" in datos.keys() or 
           not "PrecioUnitario" in datos.keys()): 
            
            respuesta["Error"] = "Falta informacion";
            return respuesta;
        
        detalleVenta: cl_DetalleVenta = cl_DetalleVenta();
        detalleVenta.SetDetalleVentaID(datos["DetalleVentaID"]);
        detalleVenta.SetVentaID(datos["VentaID"]);
        detalleVenta.SetProductoID(datos["ProductoID"]);
        detalleVenta.SetCantidad(datos["Cantidad"]);
        detalleVenta.SetPrecioUnitario(datos["PrecioUnitario"]);

        return self.respositorio.Actualizar(detalleVenta);

    def Eliminar(self, id: str) -> None:
        return self.respositorio.Eliminar(id);