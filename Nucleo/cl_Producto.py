class cl_Producto:
    
    ProductoID: int;
    Nombre: str;
    Precio: float = None;
    Stock: int = None;

    def GetProductoID(self) -> int: 
        return self.ProductoID;
    
    def SetProductoID(self, valor: int) -> None: 
        self.ProductoID = valor;

    def GetNombre(self) -> str: 
        return self.Nombre;
    
    def SetNombre(self, valor: str) -> None: 
        self.Nombre = valor;
        
    def GetPrecio(self) -> float:
        return self.Precio;
    
    def SetPrecio(self, value: float) -> None:
        self.Precio = value;

    def GetStock(self) -> int:
        return self.Stock;
    
    def SetStock(self, value: int) -> None:
        self.Stock = value;