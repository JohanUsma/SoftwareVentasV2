USE SVentas_PE;

INSERT INTO Clientes (Nombre, Apellido, Correo, Telefono, Direccion)
VALUES 
('Juan', 'Pérez', 'juanp@gmail.com', '123456789', 'Calle 1 #12-34'),
('Ana', 'Gómez', 'anag@gmail.com', '987654321', 'Calle 2 #45-67'),
('Luis', 'Martínez', 'luism@gmail.com', '567890123', 'Calle 3 #89-01'),
('Carlos', 'Rodríguez', 'carlosr@gmail.com', '098765432', 'Calle 4 #23-45'),
('Laura', 'López', 'laural@gmail.com', '321654987', 'Calle 5 #67-89'),
('Sofía', 'García', 'sofiag@gmail.com', '765432109', 'Calle 6 #90-12'),
('Pedro', 'Morales', 'pedrom@gmail.com', '432109876', 'Calle 7 #34-56'),
('Jorge', 'Jiménez', 'jorjej@gmail.com', '109876543', 'Calle 8 #78-90'),
('María', 'Torres', 'mariat@gmail.com', '876543210', 'Calle 9 #12-34'),
('Andrés', 'Hernández', 'andresh@gmail.com', '543210987', 'Calle 10 #56-78');

INSERT INTO Productos (Nombre, Precio, Stock)
VALUES 
('Laptop', 1500.00, 10),
('Teclado', 50.00, 100),
('Mouse', 25.00, 150),
('Monitor', 300.00, 50),
('Impresora', 200.00, 30),
('Teléfono', 800.00, 20),
('Tablet', 600.00, 15),
('Auriculares', 100.00, 75),
('Cámara', 400.00, 10),
('Parlantes', 120.00, 40);

INSERT INTO Ventas (ClienteID, Fecha, Total)
VALUES 
(1, '2024-01-10', 1550.00),
(2, '2024-01-12', 800.00),
(3, '2024-01-15', 600.00),
(4, '2024-01-17', 1500.00),
(5, '2024-01-20', 320.00),
(6, '2024-01-25', 1200.00),
(7, '2024-01-30', 700.00),
(8, '2024-02-02', 150.00),
(9, '2024-02-10', 1100.00),
(10, '2024-02-15', 1000.00);

INSERT INTO Empleados (Nombre, Apellido, Correo, Telefono)
VALUES 
('José', 'Sánchez', 'joses@gmail.com', '987123456'),
('Lucía', 'Fernández', 'luciaf@gmail.com', '654321987'),
('Miguel', 'Pérez', 'miguelp@gmail.com', '321987654'),
('Carolina', 'Rojas', 'carolinar@gmail.com', '654123987'),
('Diego', 'Cruz', 'diegoc@gmail.com', '321654987'),
('Felipe', 'Vargas', 'felipev@gmail.com', '876543210'),
('Sara', 'Ortiz', 'sarao@gmail.com', '543210876'),
('Daniel', 'Castillo', 'danielc@gmail.com', '432109876'),
('Roberto', 'Reyes', 'robertor@gmail.com', '321987654'),
('Paula', 'Navarro', 'paulan@gmail.com', '654987321');

INSERT INTO Proveedores (Nombre, Contacto, Telefono)
VALUES 
('TecnoPro', 'Carlos Díaz', '123456789'),
('GlobalTech', 'María López', '987654321'),
('InnovaComp', 'Sergio Méndez', '123456789'),
('Distribuidores ABC', 'Ana González', '987654321'),
('DigitalWorld', 'Andrés Torres', '123456789'),
('SmartTech', 'Laura Ríos', '987654321'),
('CompuCenter', 'Sofía García', '123456789'),
('ElectroPlus', 'Roberto Pérez', '987654321'),
('RedesPro', 'Lucía Fernández', '123456789'),
('Proveetech', 'Daniel Suárez', '987654321');

INSERT INTO DetallesVentas (VentaID, ProductoID, Cantidad, PrecioUnitario)
VALUES 
(1, 1, 1, 1500.000),
(1, 2, 1, 50.000),
(2, 6, 1, 800.000),
(3, 7, 2, 600.000),
(4, 1, 1, 1500.000),
(5, 3, 5, 25.000),
(6, 4, 2, 300.000),
(7, 9, 1, 400.000),
(8, 8, 3, 100.000),
(9, 10, 2, 120.000);

INSERT INTO MetodosPago (Nombre)
VALUES 
('Efectivo'),
('Tarjeta de Crédito'),
('Tarjeta de Débito'),
('Transferencia Bancaria'),
('PayPal'),
('Cheque'),
('Pago Móvil'),
('Crédito Empresarial'),
('Crédito del Cliente'),
('Pago Contra Entrega');

INSERT INTO Pagos (VentaID, MetodoPagoID, Monto)
VALUES 
(1, 1, 1550.000),
(2, 2, 800.000),
(3, 3, 600.000),
(4, 4, 1500.000),
(5, 5, 320.000),
(6, 6, 1200.000),
(7, 7, 700.000),
(8, 8, 150.000),
(9, 9, 1100.000),
(10, 10, 1000.000);

INSERT INTO Descuentos (Nombre, Descripcion, Porcentaje)
VALUES 
('Descuento por Temporada', 'Descuento especial para la temporada navideña', 10.000),
('Descuento por Volumen', 'Aplica al comprar más de 5 productos iguales', 5.000),
('Descuento VIP', 'Para clientes VIP', 15.000),
('Descuento de Bienvenida', 'Para nuevos clientes', 8.000),
('Descuento Especial', 'Descuento por evento especial', 20.000),
('Descuento Liquidación', 'Para productos en liquidación', 30.000),
('Descuento Aniversario', 'Para celebrar el aniversario de la tienda', 12.000),
('Descuento Promocional', 'Descuento por promociones', 25.000),
('Descuento Cumpleaños', 'Para clientes en su cumpleaños', 7.500),
('Descuento Fin de Año', 'Para ventas de fin de año', 5.000);

INSERT INTO ProductoDescuento (ProductoID, DescuentoID)
VALUES 
(1, 1), (2, 2), (3, 3), (4, 4), (5, 5),
(6, 6), (7, 7), (8, 8), (9, 9), (10, 10);