class cl_MetodoPago:
    
    MetodoPagoID: int;
    Nombre: str;

    def GetMetodoPagoID(self) -> int: 
        return self.MetodoPagoID;
    
    def SetMetodoPagoID(self, valor: int) -> None: 
        self.MetodoPagoID = valor;

    def GetNombre(self) -> str: 
        return self.Nombre;
    
    def SetNombre(self, valor: str) -> None: 
        self.Nombre = valor;