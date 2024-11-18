from Nucleo.cl_Empleado import cl_Empleado;
from Repositorios.cl_Empleado_Repositorio import cl_Empleado_Repositorio;

class cl_Empleado_Aplicacion:

    def __init__(self):
        self.respositorio = cl_Empleado_Repositorio();

    def Listar(self, id: str) -> None:
        return self.respositorio.Listar(id);

    def Insertar(self, datos: dict) -> None:
        respuesta: dict = { };

        if(not "Nombre" in datos.keys() or 
           not "Apellido" in datos.keys() or 
           not "Correo" in datos.keys() or 
           not "Telefono" in datos.keys()):
            
            respuesta["Error"] = "Falta informacion";
            return respuesta;
        
        empleado: cl_Empleado = cl_Empleado();
        empleado.SetNombre(datos["Nombre"]);
        empleado.SetApellido(datos["Apellido"]);
        empleado.SetCorreo(datos["Correo"]);
        empleado.SetTelefono(datos["Telefono"]);
        

        return self.respositorio.Insertar(empleado);

    def Actualizar(self, datos: dict) -> None:
        respuesta: dict = { };

        if(not "EmpleadoID" in datos.keys() or
            not "Nombre" in datos.keys() or 
            not "Apellido" in datos.keys() or 
            not "Correo" in datos.keys() or 
            not "Telefono" in datos.keys()): 
                
            respuesta["Error"] = "Falta informacion";
            return respuesta;
            
        empleado: cl_Empleado = cl_Empleado();
        empleado.SetEmpleadoID(datos["EmpleadoID"]);
        empleado.SetNombre(datos["Nombre"]);
        empleado.SetApellido(datos["Apellido"]);
        empleado.SetCorreo(datos["Correo"]);
        empleado.SetTelefono(datos["Telefono"]);
            
        return self.respositorio.Actualizar(empleado);

    def Eliminar(self, id: str) -> None:
        return self.respositorio.Eliminar(id);