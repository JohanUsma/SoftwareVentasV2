from ClasesT.cl_Database import cl_Database;
import os;

os.system('cls')
objDatabase: cl_Database = cl_Database();
objDatabase.OpenConnectionDB();

print("\n------------CONEXION BASE DE DATOS------------\n")

proceso: str = "Stock";

if(proceso == "Cliente"):
    print("\n------------PROCESOS TABLA CLIENTE------------\n")

    print("\n**Prueba Insertar Cliente\n")
    parametros_cliente: list = ("Juan", "Pérez", "prueba@x.com", "Calle Falsa 123", "1234567890")
    objDatabase.EjecutarSP("SP_Clientes_SIUD", "'INSERT'", "NULL", parametros_cliente)

    print("\n**Prueba Actualizar Cliente\n")
    parametros_cliente: list = ("Juan2", "Pérez2", "prueba@x.com", "Calle Falsa 123", "1234567890")
    objDatabase.EjecutarSP("SP_Clientes_SIUD", "'UPDATE'", "14", parametros_cliente)

    print("\n**Prueba Eliminar Cliente\n")
    objDatabase.EjecutarSP("SP_Clientes_SIUD", "'DELETE'", "13", parametros_cliente)
    
    print("\n**Prueba Selecionar Tabla Cliente\n")
    objDatabase.EjecutarSP("SP_Clientes_SIUD", "'SELECT'", "NULL", parametros_cliente)

if(proceso == "Descuento"):
    print("\n------------PROCESOS TABLA DESCUENTO------------\n")

    print("\n**Prueba Insertar Descuento\n")
    parametros_descuento: list = ("Decuento Prueba", "Descripcion Descuento Prueba", 25.000)
    objDatabase.EjecutarSP("SP_Descuentos_SIUD", "'INSERT'", "NULL", parametros_descuento)

    print("\n**Prueba Actualizar Descuento\n")
    parametros_descuento: list = ("Decuento Prueba Act", "Descripcion Descuento Prueba", 35.000)
    objDatabase.EjecutarSP("SP_Descuentos_SIUD", "'UPDATE'", "10", parametros_descuento)

    print("\n**Prueba Eliminar Descuento\n")
    objDatabase.EjecutarSP("SP_Descuentos_SIUD", "'DELETE'", "9", parametros_descuento)
    
    print("\n**Prueba Selecionar Tabla Descuento\n")
    objDatabase.EjecutarSP("SP_Descuentos_SIUD", "'SELECT'", "NULL", parametros_descuento)

if(proceso == "DetalleVenta"):
    print("\n------------PROCESOS TABLA DETALLE VENTA------------\n")

    print("\n**Prueba Insertar DetalleVenta\n")
    parametros_detalle_v: list = (2, 4, 5, 12500.000)
    objDatabase.EjecutarSP("SP_DetallesVentas_SIUD", "'INSERT'", "NULL", parametros_detalle_v)

    print("\n**Prueba Actualizar DetalleVenta\n")
    parametros_detalle_v: list = (3, 1, 2, 12800.000)
    objDatabase.EjecutarSP("SP_DetallesVentas_SIUD", "'UPDATE'", "7", parametros_detalle_v)

    print("\n**Prueba Eliminar DetalleVenta\n")
    objDatabase.EjecutarSP("SP_DetallesVentas_SIUD", "'DELETE'", "10", parametros_detalle_v)
    
    print("\n**Prueba Selecionar Tabla DetalleVenta\n")
    objDatabase.EjecutarSP("SP_DetallesVentas_SIUD", "'SELECT'", "NULL", parametros_detalle_v)

if(proceso == "Empleado"):
    print("\n------------PROCESOS TABLA EMPLEADO------------\n")

    print("\n**Prueba Insertar Empleado\n")
    parametros_empleado: list = ("NomPrueba", "ApePrueba", "CorrPrueba@gmail.com", "8445121")
    objDatabase.EjecutarSP("SP_Empleados_SIUD", "'INSERT'", "NULL", parametros_empleado)

    print("\n**Prueba Actualizar Empleado\n")
    parametros_empleado: list = ("NomPruebaAct", "ApePruebaAct", "CorrPruebaAct@gmail.com", "8445121")
    objDatabase.EjecutarSP("SP_Empleados_SIUD", "'UPDATE'", "4", parametros_empleado)

    print("\n**Prueba Eliminar Empleado\n")
    objDatabase.EjecutarSP("SP_Empleados_SIUD", "'DELETE'", "10", parametros_empleado)
    
    print("\n**Prueba Selecionar Tabla Empleado\n")
    objDatabase.EjecutarSP("SP_Empleados_SIUD", "'SELECT'", "NULL", parametros_empleado)
    
if(proceso == "MetodoPago"):
    
    print("\n------------PROCESOS TABLA METODO PAGO------------\n")

    print("\n**Prueba Insertar Metodo Pago\n")
    parametros_metodo_pago: list = ("Mercadolibre",)
    objDatabase.EjecutarSP("SP_MetodosPago_SIUD", "'INSERT'", "NULL", parametros_metodo_pago)

    print("\n**Prueba Actualizar Metodo Pago\n")
    parametros_metodo_pago: list = ("Gana",)
    objDatabase.EjecutarSP("SP_MetodosPago_SIUD", "'UPDATE'", "5", parametros_metodo_pago)

    print("\n**Prueba Eliminar Metodo Pago\n")
    objDatabase.EjecutarSP("SP_MetodosPago_SIUD", "'DELETE'", "10", parametros_metodo_pago)
    
    print("\n**Prueba Selecionar Tabla Metodo Pago\n")
    objDatabase.EjecutarSP("SP_MetodosPago_SIUD", "'SELECT'", "NULL", parametros_metodo_pago)
    
if(proceso == "Pago"):
    
    print("\n------------PROCESOS TABLA PAGO------------\n")

    print("\n**Prueba Insertar Pago\n")
    parametros_pago: list = (3, 7, 2750.000)
    objDatabase.EjecutarSP("SP_Pagos_SIUD", "'INSERT'", "NULL", parametros_pago)

    print("\n**Prueba Actualizar Pago\n")
    parametros_pago: list = (3, 1, 3750.000)
    objDatabase.EjecutarSP("SP_Pagos_SIUD", "'UPDATE'", "5", parametros_pago)

    print("\n**Prueba Eliminar Pago\n")
    objDatabase.EjecutarSP("SP_Pagos_SIUD", "'DELETE'", "10", parametros_pago)
    
    print("\n**Prueba Selecionar Tabla Pago\n")
    objDatabase.EjecutarSP("SP_Pagos_SIUD", "'SELECT'", "NULL", parametros_pago)
    
if(proceso == "Producto"):
    
    print("\n------------PROCESOS TABLA PRODUCTO------------\n")

    print("\n**Prueba Insertar Producto\n")
    parametros_producto: list = ("Cargador", 11.00, 100)
    objDatabase.EjecutarSP("SP_Productos_SIUD", "'INSERT'", "NULL", parametros_producto)

    print("\n**Prueba Actualizar Producto\n")
    parametros_producto: list = ("Monitor OLEDx", 350.00, 10)
    objDatabase.EjecutarSP("SP_Productos_SIUD", "'UPDATE'", "4", parametros_producto)

    print("\n**Prueba Eliminar Producto\n")
    objDatabase.EjecutarSP("SP_Productos_SIUD", "'DELETE'", "10", parametros_producto)
    
    print("\n**Prueba Selecionar Tabla Producto\n")
    objDatabase.EjecutarSP("SP_Productos_SIUD", "'SELECT'", "NULL", parametros_producto)

if(proceso == "ProductoDescuento"):
    
    print("\n------------PROCESOS TABLA PRODUCTO DESCUENTO------------\n")

    print("\n**Prueba Insertar Producto Descuento\n")
    parametros_producto_desc: list = (3, 8)
    objDatabase.EjecutarSP("SP_ProductosDescuentos_SIUD", "'INSERT'", "NULL", parametros_producto_desc)

    print("\n**Prueba Actualizar Producto Descuento\n")
    parametros_producto_desc: list = (1, 8)
    objDatabase.EjecutarSP("SP_ProductosDescuentos_SIUD", "'UPDATE'", "1", parametros_producto_desc)

    print("\n**Prueba Eliminar Producto Descuento\n")
    objDatabase.EjecutarSP("SP_ProductosDescuentos_SIUD", "'DELETE'", "10", parametros_producto_desc)
    
    print("\n**Prueba Selecionar Tabla Producto Descuento\n")
    objDatabase.EjecutarSP("SP_ProductosDescuentos_SIUD", "'SELECT'", "NULL", parametros_producto_desc)
    
if(proceso == "Proveedor"):
    
    print("\n------------PROCESOS TABLA PROVEEDOR------------\n")

    print("\n**Prueba Insertar Proveedor\n")
    parametros_proveedor: list = ("Alkomprar", "Jesus González", "5959926")
    objDatabase.EjecutarSP("SP_Proveedores_SIUD", "'INSERT'", "NULL", parametros_proveedor)

    print("\n**Prueba Actualizar Proveedor\n")
    parametros_proveedor: list = ("SmartTech 2.0", "Cristian González", "987654321")
    objDatabase.EjecutarSP("SP_Proveedores_SIUD", "'UPDATE'", "1", parametros_proveedor)

    print("\n**Prueba Eliminar Proveedor\n")
    objDatabase.EjecutarSP("SP_Proveedores_SIUD", "'DELETE'", "10", parametros_proveedor)
    
    print("\n**Prueba Selecionar Tabla Proveedor\n")
    objDatabase.EjecutarSP("SP_Proveedores_SIUD", "'SELECT'", "NULL", parametros_proveedor)

if(proceso == "Venta"):
    
    print("\n------------PROCESOS TABLA VENTA------------\n")

    print("\n**Prueba Insertar Venta\n")
    parametros_venta: list = (7, "2024-10-20", 7550.00)
    objDatabase.EjecutarSP("SP_Ventas_SIUD", "'INSERT'", "NULL", parametros_venta)

    print("\n**Prueba Actualizar Venta\n")
    parametros_venta: list = (5, "2024-01-15", 1750.00)
    objDatabase.EjecutarSP("SP_Ventas_SIUD", "'UPDATE'", "1", parametros_venta)

    print("\n**Prueba Eliminar Venta\n")
    objDatabase.EjecutarSP("SP_Ventas_SIUD", "'DELETE'", "10", parametros_venta)
    
    print("\n**Prueba Selecionar Tabla Venta\n")
    objDatabase.EjecutarSP("SP_Ventas_SIUD", "'SELECT'", "NULL", parametros_venta)

if(proceso == "Stock"):
    print("\n------------PROCESOS STOCK MENOR A 25 PRODUCTOS------------\n")
    objDatabase.EjecutarSP_Perso("SP_Stock_Productos");

if(proceso == "Top"):
    print("\n------------PROCESOS TOP 3 PRODUCTOS------------\n")
    objDatabase.EjecutarSP_Perso("SP_Top_Productos");

print("\n------------CIERRE BASE DE DATOS------------\n")

#CIERRE DE CONEXIÓN A LA BASE DE DATOS
objDatabase.CloseConnectionDB();