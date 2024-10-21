import pyodbc;
import datetime;

from ClasesMN.cl_Cliente import cl_Cliente;
from ClasesMN.cl_Descuento import cl_Descuento;
from ClasesMN.cl_DetalleVenta import cl_DetalleVenta;
from ClasesMN.cl_Empleado import cl_Empleado;
from ClasesMN.cl_MetodoPago import cl_MetodoPago;
from ClasesMN.cl_Pago import cl_Pago
from ClasesMN.cl_Producto import cl_Producto
from ClasesMN.cl_ProductoDescuento import cl_ProductoDescuento
from ClasesMN.cl_Proveedor import cl_Proveedor
from ClasesMN.cl_Venta import cl_Venta;

class cl_Database:
  
  def __init__(self):
    self.strConnection: str = """
        Driver={MySQL ODBC 9.0 Unicode Driver};
        Server=localhost;
        Database=sventas_pe;
        PORT=3306;
        user=user_ptyhon;
        password=Clas3s1Nt2024_!""";
    
    self.conexion = None;
  
  def OpenConnectionDB(self) -> None:  
    try:
      self.conexion = pyodbc.connect(self.strConnection);
      print("Conexión a la Base de Datos Exitosa");
    except Exception as e:
      print("Conexión a la Base de Datos Fallida: "+str(e));
        
  def CloseConnectionDB(self) -> None:  
    try:
      self.conexion.close();
      print("Cierre de la Base de Datos Exitosa");
    except Exception as e:
      print("Cierre de la Base de Datos Fallida: "+str(e));

  def EjecutarSP(self, nombreSp: str, accion: str, id: int, parametros: list)-> None:

    #GENERAMOS LOS MARCADORES PARA LOS ATRIBUTOS DEL SP
    marcadores: list = ','.join(["'%s'" for _ in parametros]);
    
    #CONSTRUCCIÓN DEL QUERY
    consulta = f"CALL {nombreSp}({accion},{id},{marcadores}, @p_resultado);";

    try:
      #EJECUCIÓN PROCEDURE
      cursor = self.conexion.cursor();
      cursor.execute(consulta % parametros);
      
      #SELECCIÓN DE RESULTADO
      if("SELECT" not in accion):
        cursor.execute("SELECT @p_resultado;");
        resultado = cursor.fetchone()[0];
        print("Resultado:", resultado);
      else: 
        
        #for elemento in cursor:
        #  print(elemento)
        
        #RECORRIDO DEL RESULTADO PARA TRABAJAR CON OBJETOS
        ls_generico: list = [];
        
        if(nombreSp == "SP_Clientes_SIUD"):
          
          #LLENAR LISTA DE CLIENTES
          for elemento in cursor:
            cliente: cl_Cliente = cl_Cliente();
            cliente.SetClienteID(elemento[0]);
            cliente.SetNombre(elemento[1]);
            cliente.SetApellido(elemento[2]);
            cliente.SetCorreo(elemento[3]);
            cliente.SetTelefono(elemento[4]);
            cliente.SetDireccion(elemento[5]);
                
            ls_generico.append(cliente);
            
          #IMPRIMIR CLIENTES
          for c in ls_generico:
            print(  str(c.GetClienteID()) + " - " + 
                    c.GetNombre() + " - " + 
                    c.GetApellido() + " - " + 
                    c.GetCorreo() + " - " + 
                    c.GetTelefono() + " - " + 
                    c.GetDireccion());
        
        if(nombreSp == "SP_Descuentos_SIUD"):
          
          #LLENAR LISTA DE DESCUENTOS
          for elemento in cursor:
            descuento: cl_Descuento = cl_Descuento();
            descuento.SetDescuentoID(elemento[0]);
            descuento.SetNombre(elemento[1]);
            descuento.SetDescripcion(elemento[2]);
            descuento.SetPorcentaje(elemento[3]);
                
            ls_generico.append(descuento);
          
          #IMPRIIR LISTA DE DESCUENTOS
          for d in ls_generico:
            print(  str(d.GetDescuentoID()) + " - " + 
                    d.GetNombre() + " - " + 
                    d.GetDescripcion() + " - " + 
                    str(d.GetPorcentaje()));
          
        if(nombreSp == "SP_DetallesVentas_SIUD"):
          
          #LLENAR LISTA DE DETALES VENTAS
          for elemento in cursor:
            detalleVenta: cl_DetalleVenta = cl_DetalleVenta();
            detalleVenta.SetDetalleVentaID(elemento[0]);
            detalleVenta.SetVentaID(elemento[1]);
            detalleVenta.SetProductoID(elemento[2]);
            detalleVenta.SetCantidad(elemento[3]);
            detalleVenta.SetPrecioUnitario(elemento[4]);
                
            ls_generico.append(detalleVenta);
            
          #IMPRIMIR DETALLES VENTAS
          for dv in ls_generico:
            print(  str(dv.GetDetalleVentaID()) + " - " + 
                    str(dv.GetVentaID()) + " - " + 
                    str(dv.GetProductoID()) + " - " + 
                    str(dv.GetCantidad()) + " - " + 
                    str(dv.GetPrecioUnitario()));
        
        if(nombreSp == "SP_Empleados_SIUD"):
          
          #LLENAR LISTA DE EMPLEADOS
          for elemento in cursor:
            empleado: cl_Empleado = cl_Empleado();
            empleado.SetEmpleadoID(elemento[0]);
            empleado.SetNombre(elemento[1]);
            empleado.SetApellido(elemento[2]);
            empleado.SetCorreo(elemento[3]);
            empleado.SetTelefono(elemento[4]);
                
            ls_generico.append(empleado);
            
          #IMPRIMIR EMPLEADO
          for e in ls_generico:
            print(  str(e.GetEmpleadoID()) + " - " + 
                    e.GetNombre() + " - " + 
                    e.GetApellido() + " - " + 
                    e.GetCorreo() + " - " + 
                    e.GetTelefono());
        
        if(nombreSp == "SP_MetodosPago_SIUD"):
          
          #LLENAR LISTA DE CLIENTES
          for elemento in cursor:
            metodoPago: cl_MetodoPago = cl_MetodoPago();
            metodoPago.SetMetodoPagoID(elemento[0]);
            metodoPago.SetNombre(elemento[1]);
                
            ls_generico.append(metodoPago);
            
          #IMPRIMIR CLIENTES
          for mp in ls_generico:
            print(  str(mp.GetMetodoPagoID()) + " - " + 
                    mp.GetNombre());
        
        if(nombreSp == "SP_Pagos_SIUD"):
          
          #LLENAR LISTA DE CLIENTES
          for elemento in cursor:
            pago: cl_Pago = cl_Pago();
            pago.SetPagoID(elemento[0]);
            pago.SetVentaID(elemento[1]);
            pago.SetMetodoPagoID(elemento[2]);
            pago.SetMonto(elemento[3]);
                
            ls_generico.append(pago);
            
          #IMPRIMIR CLIENTES
          for p in ls_generico:
            print(  str(p.GetPagoID()) + " - " + 
                    str(p.GetVentaID()) + " - " + 
                    str(p.GetMetodoPagoID()) + " - " + 
                    str(p.GetMonto()));
        
        if(nombreSp == "SP_Productos_SIUD"):
          
          #LLENAR LISTA DE CLIENTES
          for elemento in cursor:
            producto: cl_Producto = cl_Producto();
            producto.SetProductoID(elemento[0]);
            producto.SetNombre(elemento[1]);
            producto.SetPrecio(elemento[2]);
            producto.SetStock(elemento[3]);
                
            ls_generico.append(producto);
            
          #IMPRIMIR CLIENTES
          for pr in ls_generico:
            print(  str(pr.GetProductoID()) + " - " + 
                    pr.GetNombre() + " - " + 
                    str(pr.GetPrecio()) + " - " + 
                    str(pr.GetStock()));
        
        if(nombreSp == "SP_ProductosDescuentos_SIUD"):
          
          #LLENAR LISTA DE CLIENTES
          for elemento in cursor:
            productoDesc: cl_ProductoDescuento = cl_ProductoDescuento();
            productoDesc.SetProductoDescuentoID(elemento[0]);
            productoDesc.SetProductoID(elemento[1]);
            productoDesc.SetDescuentoID(elemento[2]);
                
            ls_generico.append(productoDesc);
            
          #IMPRIMIR CLIENTES
          for pd in ls_generico:
            print(  str(pd.GetProductoDescuentoID()) + " - " + 
                    str(pd.GetProductoID()) + " - " + 
                    str(pd.GetDescuentoID()));
        
        if(nombreSp == "SP_Proveedores_SIUD"):
          
          #LLENAR LISTA DE CLIENTES
          for elemento in cursor:
            proveedor: cl_Proveedor = cl_Proveedor();
            proveedor.SetProveedorID(elemento[0]);
            proveedor.SetNombre(elemento[1]);
            proveedor.SetContacto(elemento[2]);
            proveedor.SetTelefono(elemento[3]);
                
            ls_generico.append(proveedor);
            
          #IMPRIMIR CLIENTES
          for prov in ls_generico:
            print(  str(prov.GetProveedorID()) + " - " + 
                    prov.GetNombre() + " - " +  
                    prov.GetContacto() + " - " + 
                    prov.GetTelefono());
        
        if(nombreSp == "SP_Ventas_SIUD"):
          
          #LLENAR LISTA DE CLIENTES
          for elemento in cursor:
            venta: cl_Venta = cl_Venta();
            venta.SetVentaID(elemento[0]);
            venta.SetClienteID(elemento[1]);
            venta.SetFecha(elemento[2]);
            venta.SetTotal(elemento[3]);
                
            ls_generico.append(venta);
            
          #IMPRIMIR CLIENTES
          for v in ls_generico:
            print(  str(v.GetVentaID()) + " - " + 
                    str(v.GetClienteID()) + " - " + 
                    str(v.GetFecha()) + " - " + 
                    str(v.GetTotal()));
        
    except Exception as Error:
      cursor.execute("SELECT @p_resultado;");
      resultado = str(Error);
      print("Resultado:", resultado);
      
    #CIERRE DE TRANSACCIÓN
    cursor.execute("COMMIT;");
    cursor.close();
    
  def EjecutarSP_Perso(self, nombreSp: str)-> None:

    #CONSTRUCCIÓN DEL QUERY
    consulta = f"CALL {nombreSp};";

    #EJECUCIÓN PROCEDURE
    cursor = self.conexion.cursor();
    cursor.execute(consulta);
      
    filas = cursor.fetchall();
      
    if(len(filas) != 0):
      for elemento in filas:
        registro = "";
        cont = 0;
        for x in elemento:
          cont += 1;
          if(cont != len(elemento)):
            registro += str(x) + " - ";
          else:
            registro += str(x);
        print(registro);
    else:
      print("No se encontraron resultados");
    
    #CIERRE DE TRANSACCIÓN
    cursor.execute("COMMIT;");
    cursor.close();