DELIMITER $$
CREATE PROCEDURE SP_DetallesVentas_Listar(
    IN p_DetalleVentaID INT,
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
    IF p_DetalleVentaID IS NOT NULL THEN
        SELECT * FROM DetallesVentas WHERE DetalleVentaID = p_DetalleVentaID;
    ELSE
        SELECT * FROM DetallesVentas;
    END IF;

END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE SP_DetallesVentas_Insertar(
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

    -- INSERT
    INSERT INTO DetallesVentas (VentaID, ProductoID, Cantidad, PrecioUnitario)
    VALUES (p_VentaID, p_ProductoID, p_Cantidad, p_PrecioUnitario);

    IF v_error = 0 THEN
        SET p_resultado = 'Detalle Venta ingresada correctamente';
    END IF;

END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE SP_DetallesVentas_Actualizar(
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
    
    -- UPDATE
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

END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE SP_DetallesVentas_Eliminar(
    IN p_DetalleVentaID INT,
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

    -- DELETE
    DELETE FROM DetallesVentas WHERE DetalleVentaID = p_DetalleVentaID;

    IF v_error = 0 THEN
        IF ROW_COUNT() = 0 THEN
            SET p_resultado = 'No se encontró el Detalle Venta para eliminar';
        ELSE
            SET p_resultado = 'Detalle Venta eliminada correctamente';
        END IF;
    END IF;

END $$
DELIMITER ;