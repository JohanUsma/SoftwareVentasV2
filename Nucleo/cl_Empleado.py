class cl_Empleado:
    
    EmpleadoID: int = 0;
    Nombre: str = None;
    Apellido: str = None;
    Correo: str = None;
    Telefono: str = None;
    
    def GetEmpleadoID(self) -> int:
        return self.EmpleadoID;
    
    def SetEmpleadoID(self, value: int) -> None:
        self.EmpleadoID = value;
        
    def GetNombre(self) -> str:
        return self.Nombre;
    
    def SetNombre(self, value: str) -> None:
        self.Nombre = value;

    def GetApellido(self) -> str:
        return self.Apellido;
    
    def SetApellido(self, value: str) -> None:
        self.Apellido = value;

    def GetCorreo(self) -> str:
        return self.Correo;
    
    def SetCorreo(self, value: str) -> None:
        self.Correo = value;  

    def GetTelefono(self) -> str:
        return self.Telefono;
    
    def SetTelefono(self, value: str) -> None:
        self.Telefono = value; 