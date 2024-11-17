from Nucleo.cl_ProductoDescuento import cl_ProductoDescuento;
from Repositorios.cl_ProductoDescuento_Repositorio import cl_ProductoDescuento_Repositorio;

class cl_ProductoDescuento_Aplicacion:

    def __init__(self):
        self.respositorio = cl_ProductoDescuento_Repositorio();

    def Listar(self, id: str) -> None:
        return self.respositorio.Listar(id);
    
    def Insertar(self, datos: dict) -> None:
        respuesta: dict = { };

        if(not "ProductoID" in datos.keys() or 
           not "DescuentoID" in datos.keys()): 
            
            respuesta["Error"] = "Falta informacion";
            return respuesta;
        
        productoDescuento: cl_ProductoDescuento = cl_ProductoDescuento();
        productoDescuento.SetProductoID(datos["ProductoID"]);
        productoDescuento.SetDescuentoID(datos["DescuentoID"]);

        return self.respositorio.Insertar(productoDescuento);
    
    def Actualizar(self, datos: dict) -> None:
        respuesta: dict = { };

        if(not "ProductoDescuentoID" in datos.keys() or
           not "ProductoID" in datos.keys() or 
           not "DescuentoID" in datos.keys()): 
            
            respuesta["Error"] = "Falta informacion";
            return respuesta;
        
        productoDescuento: cl_ProductoDescuento = cl_ProductoDescuento();
        productoDescuento.SetProductoDescuentoID(datos["ProductoDescuentoID"]);
        productoDescuento.SetProductoID(datos["ProductoID"]);
        productoDescuento.SetDescuentoID(datos["DescuentoID"]);

        return self.respositorio.Actualizar(productoDescuento);

    def Eliminar(self, id: str) -> None:
        return self.respositorio.Eliminar(id);