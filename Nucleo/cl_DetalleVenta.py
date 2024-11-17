from Nucleo.cl_Venta import cl_Venta
from Nucleo.cl_Producto import cl_Producto

class cl_DetalleVenta:
    
    DetalleVentaID: int = 0;
    VentaID: int = 0;
    ProductoID: int = 0;
    Cantidad: int = None;
    PrecioUnitario: float = None;
    Venta: cl_Venta = cl_Venta();
    Producto: cl_Producto = cl_Producto();
    
    def GetDetalleVentaID(self) -> int:
        return self.DetalleVentaID;
    
    def SetDetalleVentaID(self, value: int) -> None:
        self.DetalleVentaID = value;

    def GetVentaID(self) -> int:
        return self.VentaID;
    
    def SetVentaID(self, value: int) -> None:
        self.VentaID = value;

    def GetProductoID(self) -> int:
        return self.ProductoID;
    
    def SetProductoID(self, value: int) -> None:
        self.ProductoID = value;
    
    def GetCantidad(self) -> int:
        return self.Cantidad;
    
    def SetCantidad(self, value: int) -> None:
        self.Cantidad = value;
    
    def GetPrecioUnitario(self) -> float:
        return self.PrecioUnitario;
    
    def SetPrecioUnitario(self, value: float) -> None:
        self.PrecioUnitario = value;
    
    def GetVenta(self) -> cl_Venta:
        return self.Venta;
    
    def SetVenta(self, value: cl_Venta) -> None:
        self.Venta = value;
    
    def GetProducto(self) -> cl_Producto:
        return self.Producto;
    
    def SetProducto(self, value: cl_Producto) -> None:
        self.Producto = value;