from Nucleo.cl_Producto import cl_Producto
from Nucleo.cl_Descuento import cl_Descuento

class cl_ProductoDescuento:
    
    ProductoDescuentoID: int;
    ProductoID: int;
    DescuentoID: int = 0;
    Producto: cl_Producto = cl_Producto();
    Descuento: cl_Descuento = cl_Descuento();

    def GetProductoDescuentoID(self) -> int: 
        return self.ProductoDescuentoID;
    
    def SetProductoDescuentoID(self, valor: int) -> None: 
        self.ProductoDescuentoID = valor;
    
    def GetProductoID(self) -> int: 
        return self.ProductoID;
    
    def SetProductoID(self, valor: int) -> None: 
        self.ProductoID = valor;

    def GetDescuentoID(self) -> int:
        return self.DescuentoID;
    
    def SetDescuentoID(self, value: int) -> None:
        self.DescuentoID = value;
    
    def GetProducto(self) -> cl_Producto:
        return self.Producto;
    
    def SetProducto(self, value: cl_Producto) -> None:
        self.Producto = value;
    
    def GetDescuento(self) -> cl_Descuento:
        return self.Descuento;
    
    def SetDescuento(self, value: cl_Descuento) -> None:
        self.Descuento = value;