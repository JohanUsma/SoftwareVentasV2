from Nucleo.cl_Producto import cl_Producto;
from Repositorios.cl_Producto_Repositorio import cl_Producto_Repositorio;

class cl_Producto_Aplicacion:

    def __init__(self):
        self.respositorio = cl_Producto_Repositorio();

    def Listar(self, id: str) -> None:
        return self.respositorio.Listar(id);
    
    def Insertar(self, datos: dict) -> None:
        respuesta: dict = { };

        if(not "Nombre" in datos.keys() or 
           not "Precio" in datos.keys() or 
           not "Stock" in datos.keys()): 
            
            respuesta["Error"] = "Falta informacion";
            return respuesta;
        
        producto: cl_Producto = cl_Producto();
        producto.SetNombre(datos["Nombre"]);
        producto.SetPrecio(datos["Precio"]);
        producto.SetStock(datos["Stock"]);

        return self.respositorio.Insertar(producto);
    
    def Actualizar(self, datos: dict) -> None:
        respuesta: dict = { };

        if(not "ProductoID" in datos.keys() or
           not "Nombre" in datos.keys() or 
           not "Precio" in datos.keys() or 
           not "Stock" in datos.keys()): 
            
            respuesta["Error"] = "Falta informacion";
            return respuesta;
        
        producto: cl_Producto = cl_Producto();
        producto.SetProductoID(datos["ProductoID"]);
        producto.SetNombre(datos["Nombre"]);
        producto.SetPrecio(datos["Precio"]);
        producto.SetStock(datos["Stock"]);

        return self.respositorio.Actualizar(producto);

    def Eliminar(self, id: str) -> None:
        return self.respositorio.Eliminar(id);