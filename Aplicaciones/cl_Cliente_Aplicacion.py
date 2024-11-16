import datetime;
import decimal;
from Nucleo.cl_Cliente import cl_Cliente;
from Repositorios.cl_Cliente_Repositorio import cl_Cliente_Repositorio;

class cl_Cliente_Aplicacion:

    def __init__(self):
        self.respositorio = cl_Cliente_Repositorio();

    def Listar(self, id: str) -> None:
        return self.respositorio.Listar(id);
    
    def Insertar(self, datos: dict) -> None:
        respuesta: dict = { };

        if(not "Nombre" in datos.keys() or 
           not "Apellido" in datos.keys() or 
           not "Correo" in datos.keys() or 
           not "Telefono" in datos.keys() or 
           not "Direccion" in datos.keys()): 
            
            respuesta["Error"] = "Falta informacion";
            return respuesta;
        
        cliente: cl_Cliente = cl_Cliente();
        cliente.SetNombre(datos["Nombre"]);
        cliente.SetApellido(datos["Apellido"]);
        cliente.SetCorreo(datos["Correo"]);
        cliente.SetTelefono(datos["Telefono"]);
        cliente.SetDireccion(datos["Direccion"]);

        return self.respositorio.Insertar(cliente);
    
    def Actualizar(self, datos: dict) -> None:
        respuesta: dict = { };

        if(not "ClienteID" in datos.keys() or
           not "Nombre" in datos.keys() or 
           not "Apellido" in datos.keys() or 
           not "Correo" in datos.keys() or 
           not "Telefono" in datos.keys() or 
           not "Direccion" in datos.keys()): 
            
            respuesta["Error"] = "Falta informacion";
            return respuesta;
        
        cliente: cl_Cliente = cl_Cliente();
        cliente.SetClienteID(datos["ClienteID"]);
        cliente.SetNombre(datos["Nombre"]);
        cliente.SetApellido(datos["Apellido"]);
        cliente.SetCorreo(datos["Correo"]);
        cliente.SetTelefono(datos["Telefono"]);
        cliente.SetDireccion(datos["Direccion"]);

        return self.respositorio.Actualizar(cliente);

    def Eliminar(self, id: str) -> None:
        return self.respositorio.Eliminar(id);