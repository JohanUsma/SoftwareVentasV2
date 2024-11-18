DELIMITER $$
CREATE PROCEDURE SP_Ventas_Listar(
    IN p_VentaID INT,
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
    IF p_VentaID IS NOT NULL THEN
        SELECT VentaID, ClienteID, Fecha,
        CAST(AES_DECRYPT(Total, 'Cl4v3') AS DECIMAL(10,2)) AS Total
        FROM Ventas WHERE VentaID = p_VentaID;
    ELSE
        SELECT VentaID, ClienteID, Fecha,
        CAST(AES_DECRYPT(Total, 'Cl4v3') AS DECIMAL(10,2)) AS Total
        FROM Ventas;
    END IF;

END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE SP_Ventas_Insertar(
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

    -- INSERT
    INSERT INTO Ventas (ClienteID, Fecha, Total)
    VALUES (p_ClienteID, p_Fecha, p_Total);

    IF v_error = 0 THEN
        SET p_resultado = 'Venta ingresada correctamente';
    END IF;

END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE SP_Ventas_Actualizar(
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

    -- UPDATE
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

END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE SP_Ventas_Eliminar(
    IN p_VentaID INT,
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
    DELETE FROM Ventas WHERE VentaID = p_VentaID;

    IF v_error = 0 THEN
        IF ROW_COUNT() = 0 THEN
            SET p_resultado = 'No se encontró la venta para eliminar';
        ELSE
            SET p_resultado = 'Venta eliminada correctamente';
        END IF;
    END IF;

END $$
DELIMITER ;