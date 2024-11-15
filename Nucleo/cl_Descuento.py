class cl_Descuento:
    
    DescuentoID: int = 0;
    Nombre: str = None;
    Descripcion: str = None;
    Porcentaje: float = None;
    
    def GetDescuentoID(self) -> int:
        return self.DescuentoID;
    
    def SetDescuentoID(self, value: int) -> None:
        self.DescuentoID = value;
    
    def GetNombre(self) -> str:
        return self.Nombre;
    
    def SetNombre(self, value: str) -> None:
        self.Nombre = value;

    def GetDescripcion(self) -> str:
        return self.Descripcion;
    
    def SetDescripcion(self, value: str) -> None:
        self.Descripcion = value;
    
    def GetPorcentaje(self) -> float:
        return self.Porcentaje;
    
    def SetPorcentaje(self, value: float) -> None:
        self.Porcentaje = value;