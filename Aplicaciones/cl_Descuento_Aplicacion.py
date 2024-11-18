from Nucleo.cl_Descuento import cl_Descuento;
from Repositorios.cl_Descuento_Repositorio import cl_Descuento_Repositorio;

class cl_Descuento_Aplicacion:

    def __init__(self):
        self.respositorio = cl_Descuento_Repositorio();

    def Listar(self, id: str) -> None:
        return self.respositorio.Listar(id);
   
    def Insertar(self, datos: dict) -> None:
        respuesta: dict = { };

        if(not "Nombre" in datos.keys() or 
           not "Descripcion" in datos.keys() or 
           not "Porcentaje" in datos.keys()): 
            
            respuesta["Error"] = "Falta informacion";
            return respuesta;
        
        descuento: cl_Descuento = cl_Descuento();
        descuento.SetNombre(datos["Nombre"]);
        descuento.SetDescripcion(datos["Descripcion"]);
        descuento.SetPorcentaje(datos["Porcentaje"]);


        return self.respositorio.Insertar(descuento);
    
    def Actualizar(self, datos: dict) -> None:
        respuesta: dict = { };

        if(not "DescuentoID" in datos.keys() or
           not "Nombre" in datos.keys() or 
           not "Descripcion" in datos.keys() or 
           not "Porcentaje" in datos.keys()): 
            
            respuesta["Error"] = "Falta informacion";
            return respuesta;
        
        descuento: cl_Descuento = cl_Descuento();
        descuento.SetDescuentoID(datos["DescuentoID"]);
        descuento.SetNombre(datos["Nombre"]);
        descuento.SetDescripcion(datos["Descripcion"]);
        descuento.SetPorcentaje(datos["Porcentaje"]);


        return self.respositorio.Actualizar(descuento);

    def Eliminar(self, id: str) -> None:
        return self.respositorio.Eliminar(id);   