DELIMITER $$
CREATE PROCEDURE SP_Pagos_Listar(
    IN p_PagoID INT,
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
    IF p_PagoID IS NOT NULL THEN
        SELECT * FROM Pagos WHERE PagoID = p_PagoID;
    ELSE
        SELECT * FROM Pagos;
    END IF;

END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE SP_Pagos_Insertar(
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

    -- INSERT
    INSERT INTO Pagos (VentaID, MetodoPagoID, Monto)
    VALUES (p_VentaID, p_MetodoPagoID, p_Monto);

    IF v_error = 0 THEN
        SET p_resultado = 'Pago ingresado correctamente';
    END IF;

END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE SP_Pagos_Actualizar(
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

    -- UPDATE
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

END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE SP_Pagos_Eliminar(
    IN p_PagoID INT,
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
    DELETE FROM Pagos WHERE PagoID = p_PagoID;

    IF v_error = 0 THEN
        IF ROW_COUNT() = 0 THEN
            SET p_resultado = 'No se encontró el Pago para eliminar';
        ELSE
            SET p_resultado = 'Pago eliminado correctamente';
        END IF;
    END IF;

END $$
DELIMITER ;