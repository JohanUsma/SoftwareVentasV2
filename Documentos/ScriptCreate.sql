CREATE DATABASE SVentas_PE;

USE SVentas_PE;

CREATE TABLE Clientes (
    ClienteID INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(100),
    Apellido VARCHAR(100),
    Correo BLOB,
    Telefono BLOB,
    Direccion BLOB
);

CREATE TABLE Productos (
    ProductoID INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(100),
    Precio DECIMAL(10, 2),
    Stock INT
);

CREATE TABLE Ventas (
    VentaID INT PRIMARY KEY AUTO_INCREMENT,
    ClienteID INT,
    Fecha DATETIME,
    Total BLOB,
    FOREIGN KEY (ClienteID) REFERENCES Clientes(ClienteID)
);

CREATE TABLE Empleados (
    EmpleadoID INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(100),
    Apellido VARCHAR(100),
    Correo BLOB,
    Telefono BLOB
);

CREATE TABLE Proveedores (
    ProveedorID INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(100),
    Contacto BLOB,
    Telefono BLOB
);

CREATE TABLE DetallesVentas (
    DetalleVentaID INT PRIMARY KEY AUTO_INCREMENT,
    VentaID INT,
    ProductoID INT,
    Cantidad INT,
    PrecioUnitario DECIMAL(10, 2),
    FOREIGN KEY (VentaID) REFERENCES Ventas(VentaID),
    FOREIGN KEY (ProductoID) REFERENCES Productos(ProductoID)
);

CREATE TABLE MetodosPago (
    MetodoPagoID INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(100)
);

CREATE TABLE Pagos (
    PagoID INT PRIMARY KEY AUTO_INCREMENT,
    VentaID INT,
    MetodoPagoID INT,
    Monto BLOB,
    FOREIGN KEY (VentaID) REFERENCES Ventas(VentaID),
    FOREIGN KEY (MetodoPagoID) REFERENCES MetodosPago(MetodoPagoID)
);

CREATE TABLE Descuentos (
    DescuentoID INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(100),
    Descripcion VARCHAR(200),
    Porcentaje DECIMAL(5, 2)
);

CREATE TABLE ProductoDescuento (
    ProductoDescuentoID INT PRIMARY KEY AUTO_INCREMENT,
    ProductoID INT,
    DescuentoID INT,
    FOREIGN KEY (ProductoID) REFERENCES Productos(ProductoID),
    FOREIGN KEY (DescuentoID) REFERENCES Descuentos(DescuentoID)
);