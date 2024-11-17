from Nucleo.cl_Venta import cl_Venta
from Nucleo.cl_MetodoPago import cl_MetodoPago

class cl_Pago:
    
    PagoID: int = 0;
    VentaID: int = 0;
    MetodoPagoID: int = 0;
    Monto: float = None;
    Venta: cl_Venta = cl_Venta();
    MetodoPago: cl_MetodoPago = cl_MetodoPago();
    
    def GetPagoID(self) -> int:
        return self.PagoID;
    
    def SetPagoID(self, value: int) -> None:
        self.PagoID = value;

    def GetVentaID(self) -> int:
        return self.VentaID;
    
    def SetVentaID(self, value: int) -> None:
        self.VentaID = value;

    def GetMetodoPagoID(self) -> int:
        return self.MetodoPagoID;
    
    def SetMetodoPagoID(self, value: int) -> None:
        self.MetodoPagoID = value;
    
    def GetMonto(self) -> float:
        return self.Monto;
    
    def SetMonto(self, value: float) -> None:
        self.Monto = value;
    
    def GetVenta(self) -> cl_Venta:
        return self.Venta;
    
    def SetVenta(self, value: cl_Venta) -> None:
        self.Venta = value;
    
    def GetMetodoPago(self) -> cl_MetodoPago:
        return self.MetodoPago;
    
    def SetMetodoPago(self, value: cl_MetodoPago) -> None:
        self.MetodoPago = value;