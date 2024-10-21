class cl_Proveedor:
    
    ProveedorID: int = 0;
    Nombre: str = None;
    Contacto: str = None;
    Telefono: str = None;
    
    def GetProveedorID(self) -> int:
        return self.ProveedorID;
    
    def SetProveedorID(self, value: int) -> None:
        self.ProveedorID = value;
        
    def GetNombre(self) -> str:
        return self.Nombre;
    
    def SetNombre(self, value: str) -> None:
        self.Nombre = value;

    def GetContacto(self) -> str:
        return self.Contacto;
    
    def SetContacto(self, value: str) -> None:
        self.Contacto = value;  

    def GetTelefono(self) -> str:
        return self.Telefono;
    
    def SetTelefono(self, value: str) -> None:
        self.Telefono = value; 