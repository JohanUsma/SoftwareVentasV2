import datetime; 
from Nucleo.cl_Cliente import cl_Cliente

class cl_Venta:
    
    VentaID: int;
    ClienteID: int = None;
    Fecha: datetime = None;
    Total: float = None;
    Cliente: cl_Cliente = cl_Cliente();

    def GetVentaID(self) -> int: 
        return self.VentaID;
    
    def SetVentaID(self, valor: int) -> None: 
        self.VentaID = valor;
    
    def GetClienteID(self) -> int:
        return self.ClienteID;
    
    def SetClienteID(self, value: int) -> None:
        self.ClienteID = value;
    
    def GetFecha(self) -> datetime:
        return self.Fecha;
    
    def SetFecha(self, value: datetime) -> None:
        self.Fecha = value;
        
    def GetTotal(self) -> float:
        return self.Total;
    
    def SetTotal(self, value: float) -> None:
        self.Total = value;
    
    def GetCliente(self) -> cl_Cliente:
        return self.Cliente;
    
    def SetCliente(self, value: cl_Cliente) -> None:
        self.Cliente = value;