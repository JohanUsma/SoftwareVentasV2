from Nucleo.cl_Proveedor import cl_Proveedor;
from Repositorios.cl_Proveedor_Repositorio import cl_Proveedor_Repositorio;

class cl_Proveedor_Aplicacion:

    def __init__(self):
        self.respositorio = cl_Proveedor_Repositorio();

    def Listar(self, id: str) -> None:
        return self.respositorio.Listar(id);

    def Insertar(self, datos: dict) -> None:
        respuesta: dict = { };

        if(not "Nombre" in datos.keys() or 
           not "Contacto" in datos.keys() or 
           not "Telefono" in datos.keys()):
            
            respuesta["Error"] = "Falta informacion";
            return respuesta;
        
        proveedor: cl_Proveedor = cl_Proveedor();
        proveedor.SetNombre(datos["Nombre"]);
        proveedor.SetContacto(datos["Contacto"]);
        proveedor.SetTelefono(datos["Telefono"]);

        return self.respositorio.Insertar(proveedor);

    def Actualizar(self, datos: dict) -> None:
        respuesta: dict = { };

        if(not "ProveedorID" in datos.keys() or
            not "Nombre" in datos.keys() or 
            not "Contacto" in datos.keys() or 
            not "Telefono" in datos.keys()): 
            
            respuesta["Error"] = "Falta informacion";
            return respuesta;
        
        proveedor: cl_Proveedor = cl_Proveedor();
        proveedor.SetProveedorID(datos["ProveedorID"]);
        proveedor.SetNombre(datos["Nombre"]);
        proveedor.SetContacto(datos["Contacto"]);
        proveedor.SetTelefono(datos["Telefono"]);
        
        return self.respositorio.Actualizar(proveedor);

    def Eliminar(self, id: str) -> None:
            return self.respositorio.Eliminar(id);