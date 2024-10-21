-- SP_Clientes_SIUD ======================================================================================
DELIMITER $$
CREATE PROCEDURE SP_Clientes_SIUD(
    IN action_type VARCHAR(10),
    IN p_ClienteID INT,
    IN p_Nombre VARCHAR(100),
    IN p_Apellido VARCHAR(100),
    IN p_Correo VARCHAR(100),
    IN p_Direccion VARCHAR(200),
    IN p_Telefono VARCHAR(15),
    OUT p_resultado VARCHAR(255)
)
BEGIN
    DECLARE v_error INT DEFAULT 0;
    DECLARE v_error_message VARCHAR(255);

    -- MANEJAR EXCEPCIONES
    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION 
    BEGIN
        GET DIAGNOSTICS CONDITION 1 v_error_message = MESSAGE_TEXT;
        SET p_resultado = CONCAT('Error: ', v_error_message);
        SET v_error = 1;
    END;

    -- SELECT
    IF action_type = 'SELECT' THEN
        IF p_ClienteID IS NOT NULL THEN
            SELECT * FROM Clientes WHERE ClienteID = p_ClienteID;
        ELSE
            SELECT * FROM Clientes;
        END IF;
    
    -- INSERT
    ELSEIF action_type = 'INSERT' THEN
        INSERT INTO Clientes (Nombre, Apellido, Correo, Direccion, Telefono)
        VALUES (p_Nombre, p_Apellido, p_Correo, p_Direccion, p_Telefono);

        IF v_error = 0 THEN
            SET p_resultado = 'Cliente ingresado correctamente';
        END IF;
    
    -- UPDATE
    ELSEIF action_type = 'UPDATE' THEN
        UPDATE Clientes
        SET Nombre = p_Nombre,
            Apellido = p_Apellido,
            Correo = p_Correo,
            Direccion = p_Direccion,
            Telefono = p_Telefono
        WHERE ClienteID = p_ClienteID;

        IF v_error = 0 THEN
            IF ROW_COUNT() = 0 THEN
                SET p_resultado = 'No se encontró el cliente para actualizar';
            ELSE
                SET p_resultado = 'Cliente actualizado correctamente';
            END IF;
        END IF;

    -- DELETE
    ELSEIF action_type = 'DELETE' THEN
        DELETE FROM Clientes WHERE ClienteID = p_ClienteID;

        IF v_error = 0 THEN
            IF ROW_COUNT() = 0 THEN
                SET p_resultado = 'No se encontró el cliente para eliminar';
            ELSE
                SET p_resultado = 'Cliente eliminado correctamente';
            END IF;
        END IF;

    ELSE
        SET p_resultado = 'Acción no reconocida';
    END IF;
END $$
DELIMITER ;

-- SP_Productos_SIUD ======================================================================================
DELIMITER $$
CREATE PROCEDURE SP_Productos_SIUD(
    IN action_type VARCHAR(10),
    IN p_ProductoID INT,
    IN p_Nombre VARCHAR(100),
    IN p_Precio DECIMAL(10, 2),
    IN p_Stock INT,
    OUT p_resultado VARCHAR(255)
)
BEGIN
    DECLARE v_error INT DEFAULT 0;
    DECLARE v_error_message VARCHAR(255);

    -- MANEJAR EXCEPCIONES ======================================================================================
    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION 
    BEGIN
        GET DIAGNOSTICS CONDITION 1 v_error_message = MESSAGE_TEXT;
        SET p_resultado = CONCAT('Error: ', v_error_message);
        SET v_error = 1;
    END;

    -- SELECT
    IF action_type = 'SELECT' THEN
        IF p_ProductoID IS NOT NULL THEN
            SELECT * FROM Productos WHERE ProductoID = p_ProductoID;
        ELSE
            SELECT * FROM Productos;
        END IF;

    -- INSERT
    ELSEIF action_type = 'INSERT' THEN
        INSERT INTO Productos (Nombre, Precio, Stock)
        VALUES (p_Nombre, p_Precio, p_Stock);

        IF v_error = 0 THEN
            SET p_resultado = 'Producto ingresado correctamente';
        END IF;
    
    -- UPDATE
    ELSEIF action_type = 'UPDATE' THEN
        UPDATE Productos
        SET Nombre = p_Nombre,
            Precio = p_Precio,
            Stock = p_Stock
        WHERE ProductoID = p_ProductoID;

        IF v_error = 0 THEN
            IF ROW_COUNT() = 0 THEN
                SET p_resultado = 'No se encontró el producto para actualizar';
            ELSE
                SET p_resultado = 'Producto actualizado correctamente';
            END IF;
        END IF;

    -- DELETE
    ELSEIF action_type = 'DELETE' THEN
        DELETE FROM Productos WHERE ProductoID = p_ProductoID;

        IF v_error = 0 THEN
            IF ROW_COUNT() = 0 THEN
                SET p_resultado = 'No se encontró el producto para eliminar';
            ELSE
                SET p_resultado = 'Producto eliminado correctamente';
            END IF;
        END IF;

    ELSE
        SET p_resultado = 'Acción no reconocida';
    END IF;
END $$
DELIMITER ;

-- SP_Ventas_SIUD ======================================================================================
DELIMITER $$
CREATE PROCEDURE SP_Ventas_SIUD(
    IN action_type VARCHAR(10),
    IN p_VentaID INT,
    IN p_ClienteID INT,
    IN p_Fecha DATETIME,
    IN p_Total DECIMAL(10, 2),
    OUT p_resultado VARCHAR(255)
)
BEGIN
    DECLARE v_error INT DEFAULT 0;
    DECLARE v_error_message VARCHAR(255);

    -- MANEJAR EXCEPCIONES
    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION 
    BEGIN
        GET DIAGNOSTICS CONDITION 1 v_error_message = MESSAGE_TEXT;
        SET p_resultado = CONCAT('Error: ', v_error_message);
        SET v_error = 1;
    END;

    -- SELECT
    IF action_type = 'SELECT' THEN
        IF p_VentaID IS NOT NULL THEN
            SELECT * FROM Ventas WHERE VentaID = p_VentaID;
        ELSE
            SELECT * FROM Ventas;
        END IF;

    -- INSERT
    ELSEIF action_type = 'INSERT' THEN
        INSERT INTO Ventas (ClienteID, Fecha, Total)
        VALUES (p_ClienteID, p_Fecha, p_Total);

        IF v_error = 0 THEN
            SET p_resultado = 'Venta ingresada correctamente';
        END IF;
    
    -- UPDATE
    ELSEIF action_type = 'UPDATE' THEN
        UPDATE Ventas
        SET ClienteID = p_ClienteID,
            Fecha = p_Fecha,
            Total = p_Total
        WHERE VentaID = p_VentaID;

        IF v_error = 0 THEN
            IF ROW_COUNT() = 0 THEN
                SET p_resultado = 'No se encontró la venta para actualizar';
            ELSE
                SET p_resultado = 'Venta actualizada correctamente';
            END IF;
        END IF;

    -- DELETE
    ELSEIF action_type = 'DELETE' THEN
        DELETE FROM Ventas WHERE VentaID = p_VentaID;

        IF v_error = 0 THEN
            IF ROW_COUNT() = 0 THEN
                SET p_resultado = 'No se encontró la venta para eliminar';
            ELSE
                SET p_resultado = 'Venta eliminada correctamente';
            END IF;
        END IF;

    ELSE
        SET p_resultado = 'Acción no reconocida';
    END IF;
END $$
DELIMITER ;

-- SP_Empleados_SIUD ======================================================================================
DELIMITER $$
CREATE PROCEDURE SP_Empleados_SIUD(
    IN action_type VARCHAR(10),
    IN p_EmpleadoID INT,
    IN p_Nombre VARCHAR(100),
    IN p_Apellido VARCHAR(100),
    IN p_Correo VARCHAR(100),
    IN p_Telefono VARCHAR(15),
    OUT p_resultado VARCHAR(255)
)
BEGIN
    DECLARE v_error INT DEFAULT 0;
    DECLARE v_error_message VARCHAR(255);

    -- MANEJAR EXCEPCIONES
    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION 
    BEGIN
        GET DIAGNOSTICS CONDITION 1 v_error_message = MESSAGE_TEXT;
        SET p_resultado = CONCAT('Error: ', v_error_message);
        SET v_error = 1;
    END;

    -- SELECT
    IF action_type = 'SELECT' THEN
        IF p_EmpleadoID IS NOT NULL THEN
            SELECT * FROM Empleados WHERE EmpleadoID = p_EmpleadoID;
        ELSE
            SELECT * FROM Empleados;
        END IF;

    -- INSERT
    ELSEIF action_type = 'INSERT' THEN
        INSERT INTO Empleados (Nombre, Apellido, Correo, Telefono)
        VALUES (p_Nombre, p_Apellido, p_Correo, p_Telefono);

        IF v_error = 0 THEN
            SET p_resultado = 'Empleado ingresado correctamente';
        END IF;
    
    -- UPDATE
    ELSEIF action_type = 'UPDATE' THEN
        UPDATE Empleados
        SET Nombre = p_Nombre,
            Apellido = p_Apellido,
            Correo = p_Correo,
            Telefono = p_Telefono
        WHERE EmpleadoID = p_EmpleadoID;

        IF v_error = 0 THEN
            IF ROW_COUNT() = 0 THEN
                SET p_resultado = 'No se encontró el empleado para actualizar';
            ELSE
                SET p_resultado = 'Empleado actualizado correctamente';
            END IF;
        END IF;

    -- DELETE
    ELSEIF action_type = 'DELETE' THEN
        DELETE FROM Empleados WHERE EmpleadoID = p_EmpleadoID;

        IF v_error = 0 THEN
            IF ROW_COUNT() = 0 THEN
                SET p_resultado = 'No se encontró el empleado para eliminar';
            ELSE
                SET p_resultado = 'Empleado eliminado correctamente';
            END IF;
        END IF;

    ELSE
        SET p_resultado = 'Acción no reconocida';
    END IF;
END $$
DELIMITER ;

-- SP_Proveedores_SIUD ======================================================================================
DELIMITER $$
CREATE PROCEDURE SP_Proveedores_SIUD(
    IN action_type VARCHAR(10),
    IN p_ProveedorID INT,
    IN p_Nombre VARCHAR(100),
    IN p_Contacto VARCHAR(100),
    IN p_Telefono VARCHAR(15),
    OUT p_resultado VARCHAR(255)
)
BEGIN
    DECLARE v_error INT DEFAULT 0;
    DECLARE v_error_message VARCHAR(255);

    -- MANEJAR EXCEPCIONES
    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION 
    BEGIN
        GET DIAGNOSTICS CONDITION 1 v_error_message = MESSAGE_TEXT;
        SET p_resultado = CONCAT('Error: ', v_error_message);
        SET v_error = 1;
    END;

    -- SELECT
    IF action_type = 'SELECT' THEN
        IF p_ProveedorID IS NOT NULL THEN
            SELECT * FROM Proveedores WHERE ProveedorID = p_ProveedorID;
        ELSE
            SELECT * FROM Proveedores;
        END IF;

    -- INSERT
    ELSEIF action_type = 'INSERT' THEN
        INSERT INTO Proveedores (Nombre, Contacto, Telefono)
        VALUES (p_Nombre, p_Contacto, p_Telefono);

        IF v_error = 0 THEN
            SET p_resultado = 'Proveedor ingresado correctamente';
        END IF;
    
    -- UPDATE
    ELSEIF action_type = 'UPDATE' THEN
        UPDATE Proveedores
        SET Nombre = p_Nombre,
            Contacto = p_Contacto,
            Telefono = p_Telefono
        WHERE ProveedorID = p_ProveedorID;

        IF v_error = 0 THEN
            IF ROW_COUNT() = 0 THEN
                SET p_resultado = 'No se encontró el proveedor para actualizar';
            ELSE
                SET p_resultado = 'Proveedor actualizado correctamente';
            END IF;
        END IF;

    -- DELETE
    ELSEIF action_type = 'DELETE' THEN
        DELETE FROM Proveedores WHERE ProveedorID = p_ProveedorID;

        IF v_error = 0 THEN
            IF ROW_COUNT() = 0 THEN
                SET p_resultado = 'No se encontró el proveedor para eliminar';
            ELSE
                SET p_resultado = 'Proveedor eliminado correctamente';
            END IF;
        END IF;

    ELSE
        SET p_resultado = 'Acción no reconocida';
    END IF;
END $$
DELIMITER ;

-- SP_DetallesVentas_SIUD ======================================================================================
DELIMITER $$
CREATE PROCEDURE SP_DetallesVentas_SIUD(
    IN action_type VARCHAR(10),
    IN p_DetalleVentaID INT,
    IN p_VentaID INT,
    IN p_ProductoID INT,
    IN p_Cantidad INT,
    IN p_PrecioUnitario DECIMAL(10, 2),
    OUT p_resultado VARCHAR(255)
)
BEGIN
    DECLARE v_error INT DEFAULT 0;
    DECLARE v_error_message VARCHAR(255);

    -- MANEJAR EXCEPCIONES
    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION 
    BEGIN
        GET DIAGNOSTICS CONDITION 1 v_error_message = MESSAGE_TEXT;
        SET p_resultado = CONCAT('Error: ', v_error_message);
        SET v_error = 1;
    END;

    -- SELECT
    IF action_type = 'SELECT' THEN
        IF p_DetalleVentaID IS NOT NULL THEN
            SELECT * FROM DetallesVentas WHERE DetalleVentaID = p_DetalleVentaID;
        ELSE
            SELECT * FROM DetallesVentas;
        END IF;

    -- INSERT
    ELSEIF action_type = 'INSERT' THEN
        INSERT INTO DetallesVentas (VentaID, ProductoID, Cantidad, PrecioUnitario)
        VALUES (p_VentaID, p_ProductoID, p_Cantidad, p_PrecioUnitario);

        IF v_error = 0 THEN
            SET p_resultado = 'Detalle Venta ingresada correctamente';
        END IF;
    
    -- UPDATE
    ELSEIF action_type = 'UPDATE' THEN
        UPDATE DetallesVentas
        SET VentaID = p_VentaID,
            ProductoID = p_ProductoID,
            Cantidad = p_Cantidad,
            PrecioUnitario = p_PrecioUnitario
        WHERE DetalleVentaID = p_DetalleVentaID;

        IF v_error = 0 THEN
            IF ROW_COUNT() = 0 THEN
                SET p_resultado = 'No se encontró el Detalle Venta para actualizar';
            ELSE
                SET p_resultado = 'Detalle Venta actualizada correctamente';
            END IF;
        END IF;

    -- DELETE
    ELSEIF action_type = 'DELETE' THEN
        DELETE FROM DetallesVentas WHERE DetalleVentaID = p_DetalleVentaID;

        IF v_error = 0 THEN
            IF ROW_COUNT() = 0 THEN
                SET p_resultado = 'No se encontró el Detalle Venta para eliminar';
            ELSE
                SET p_resultado = 'Detalle Venta eliminada correctamente';
            END IF;
        END IF;

    ELSE
        SET p_resultado = 'Acción no reconocida';
    END IF;
END $$
DELIMITER ;

-- SP_MetodosPago_SIUD ======================================================================================
DELIMITER $$
CREATE PROCEDURE SP_MetodosPago_SIUD(
    IN action_type VARCHAR(10),
    IN p_MetodoPagoID INT,
    IN p_Nombre VARCHAR(100),
    OUT p_resultado VARCHAR(255)
)
BEGIN
    DECLARE v_error INT DEFAULT 0;
    DECLARE v_error_message VARCHAR(255);

    -- MANEJAR EXCEPCIONES
    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION 
    BEGIN
        GET DIAGNOSTICS CONDITION 1 v_error_message = MESSAGE_TEXT;
        SET p_resultado = CONCAT('Error: ', v_error_message);
        SET v_error = 1;
    END;

    -- SELECT
    IF action_type = 'SELECT' THEN
        IF p_MetodoPagoID IS NOT NULL THEN
            SELECT * FROM MetodosPago WHERE MetodoPagoID = p_MetodoPagoID;
        ELSE
            SELECT * FROM MetodosPago;
        END IF;

    -- INSERT
    ELSEIF action_type = 'INSERT' THEN
        INSERT INTO MetodosPago (Nombre)
        VALUES (p_Nombre);

        IF v_error = 0 THEN
            SET p_resultado = 'Metodo Pago ingresado correctamente';
        END IF;
    
    -- UPDATE
    ELSEIF action_type = 'UPDATE' THEN
        UPDATE MetodosPago
        SET Nombre = p_Nombre
        WHERE MetodoPagoID = p_MetodoPagoID;

        IF v_error = 0 THEN
            IF ROW_COUNT() = 0 THEN
                SET p_resultado = 'No se encontró el Metodo Pago para actualizar';
            ELSE
                SET p_resultado = 'Metodo Pago actualizado correctamente';
            END IF;
        END IF;

    -- DELETE
    ELSEIF action_type = 'DELETE' THEN
        DELETE FROM MetodosPago WHERE MetodoPagoID = p_MetodoPagoID;

        IF v_error = 0 THEN
            IF ROW_COUNT() = 0 THEN
                SET p_resultado = 'No se encontró el Metodo Pago para eliminar';
            ELSE
                SET p_resultado = 'Metodo Pago eliminado correctamente';
            END IF;
        END IF;

    ELSE
        SET p_resultado = 'Acción no reconocida';
    END IF;
END $$
DELIMITER ;

-- SP_Pagos_SIUD ======================================================================================
DELIMITER $$
CREATE PROCEDURE SP_Pagos_SIUD(
    IN action_type VARCHAR(10),
    IN p_PagoID INT,
    IN p_VentaID INT,
    IN p_MetodoPagoID INT,
    IN p_Monto DECIMAL(10, 2),
    OUT p_resultado VARCHAR(255)
)
BEGIN
    DECLARE v_error INT DEFAULT 0;
    DECLARE v_error_message VARCHAR(255);

    -- MANEJAR EXCEPCIONES
    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION 
    BEGIN
        GET DIAGNOSTICS CONDITION 1 v_error_message = MESSAGE_TEXT;
        SET p_resultado = CONCAT('Error: ', v_error_message);
        SET v_error = 1;
    END;

    -- SELECT
    IF action_type = 'SELECT' THEN
        IF p_PagoID IS NOT NULL THEN
            SELECT * FROM Pagos WHERE PagoID = p_PagoID;
        ELSE
            SELECT * FROM Pagos;
        END IF;

    -- INSERT
    ELSEIF action_type = 'INSERT' THEN
        INSERT INTO Pagos (VentaID, MetodoPagoID, Monto)
        VALUES (p_VentaID, p_MetodoPagoID, p_Monto);

        IF v_error = 0 THEN
            SET p_resultado = 'Pago ingresado correctamente';
        END IF;
    
    -- UPDATE
    ELSEIF action_type = 'UPDATE' THEN
        UPDATE Pagos
        SET VentaID = p_VentaID,
            MetodoPagoID = p_MetodoPagoID,
            Monto = p_Monto
        WHERE PagoID = p_PagoID;

        IF v_error = 0 THEN
            IF ROW_COUNT() = 0 THEN
                SET p_resultado = 'No se encontró el Pago para actualizar';
            ELSE
                SET p_resultado = 'Pago actualizado correctamente';
            END IF;
        END IF;

    -- DELETE
    ELSEIF action_type = 'DELETE' THEN
        DELETE FROM Pagos WHERE PagoID = p_PagoID;

        IF v_error = 0 THEN
            IF ROW_COUNT() = 0 THEN
                SET p_resultado = 'No se encontró el Pago para eliminar';
            ELSE
                SET p_resultado = 'Pago eliminado correctamente';
            END IF;
        END IF;

    ELSE
        SET p_resultado = 'Acción no reconocida';
    END IF;
END $$
DELIMITER ;

-- SP_Descuentos_SIUD ======================================================================================
DELIMITER $$
CREATE PROCEDURE SP_Descuentos_SIUD(
    IN action_type VARCHAR(10),
    IN p_DescuentoID INT,
    IN p_Nombre VARCHAR(100),
    IN p_Descripcion VARCHAR(200),
    IN p_Porcentaje DECIMAL(5, 2),
    OUT p_resultado VARCHAR(255)
)
BEGIN
    DECLARE v_error INT DEFAULT 0;
    DECLARE v_error_message VARCHAR(255);

    -- MANEJAR EXCEPCIONES
    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION 
    BEGIN
        GET DIAGNOSTICS CONDITION 1 v_error_message = MESSAGE_TEXT;
        SET p_resultado = CONCAT('Error: ', v_error_message);
        SET v_error = 1;
    END;

    -- SELECT
    IF action_type = 'SELECT' THEN
        IF p_DescuentoID IS NOT NULL THEN
            SELECT * FROM Descuentos WHERE DescuentoID = p_DescuentoID;
        ELSE
            SELECT * FROM Descuentos;
        END IF;

    -- INSERT
    ELSEIF action_type = 'INSERT' THEN
        INSERT INTO Descuentos (Nombre, Descripcion, Porcentaje)
        VALUES (p_Nombre, p_Descripcion, p_Porcentaje);

        IF v_error = 0 THEN
            SET p_resultado = 'Descuento ingresado correctamente';
        END IF;
    
    -- UPDATE
    ELSEIF action_type = 'UPDATE' THEN
        UPDATE Descuentos
        SET Nombre = p_Nombre,
            Descripcion = p_Descripcion,
            Porcentaje = p_Porcentaje
        WHERE DescuentoID = p_DescuentoID;

        IF v_error = 0 THEN
            IF ROW_COUNT() = 0 THEN
                SET p_resultado = 'No se encontró el Descuento para actualizar';
            ELSE
                SET p_resultado = 'Descuento actualizado correctamente';
            END IF;
        END IF;

    -- DELETE
    ELSEIF action_type = 'DELETE' THEN
        DELETE FROM Descuentos WHERE DescuentoID = p_DescuentoID;

        IF v_error = 0 THEN
            IF ROW_COUNT() = 0 THEN
                SET p_resultado = 'No se encontró el Descuento para eliminar';
            ELSE
                SET p_resultado = 'Descuento eliminado correctamente';
            END IF;
        END IF;

    ELSE
        SET p_resultado = 'Acción no reconocida';
    END IF;
END $$
DELIMITER ;

-- SP_ProductosDescuentos_SIUD ======================================================================================
DELIMITER $$
CREATE PROCEDURE SP_ProductosDescuentos_SIUD(
    IN action_type VARCHAR(10),
    IN p_ProductoDescuentoID INT,
    IN p_ProductoID INT,
    IN p_DescuentoID INT,
    OUT p_resultado VARCHAR(255)
)
BEGIN
    DECLARE v_error INT DEFAULT 0;
    DECLARE v_error_message VARCHAR(255);

    -- MANEJAR EXCEPCIONES
    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION 
    BEGIN
        GET DIAGNOSTICS CONDITION 1 v_error_message = MESSAGE_TEXT;
        SET p_resultado = CONCAT('Error: ', v_error_message);
        SET v_error = 1;
    END;

    -- SELECT
    IF action_type = 'SELECT' THEN
        IF p_ProductoDescuentoID IS NOT NULL THEN
            SELECT * FROM ProductoDescuento WHERE ProductoDescuentoID = p_ProductoDescuentoID;
        ELSE
            SELECT * FROM ProductoDescuento;
        END IF;

    -- INSERT
    ELSEIF action_type = 'INSERT' THEN
        INSERT INTO ProductoDescuento (ProductoID, DescuentoID)
        VALUES (p_ProductoID, p_DescuentoID);

        IF v_error = 0 THEN
            SET p_resultado = 'Descuento de Producto ingresado correctamente';
        END IF;
    
    -- UPDATE
    ELSEIF action_type = 'UPDATE' THEN
        UPDATE ProductoDescuento
        SET ProductoID = p_ProductoID,
            DescuentoID = p_DescuentoID
        WHERE ProductoDescuentoID = p_ProductoDescuentoID;

        IF v_error = 0 THEN
            IF ROW_COUNT() = 0 THEN
                SET p_resultado = 'No se encontró el Descuento del Producto para actualizar';
            ELSE
                SET p_resultado = 'Descuento del Producto actualizado correctamente';
            END IF;
        END IF;

    -- DELETE
    ELSEIF action_type = 'DELETE' THEN
        DELETE FROM ProductoDescuento WHERE ProductoDescuentoID = p_ProductoDescuentoID;

        IF v_error = 0 THEN
            IF ROW_COUNT() = 0 THEN
                SET p_resultado = 'No se encontró el Descuento del Producto para eliminar';
            ELSE
                SET p_resultado = 'Descuento del Producto eliminado correctamente';
            END IF;
        END IF;

    ELSE
        SET p_resultado = 'Acción no reconocida';
    END IF;
END $$
DELIMITER ;