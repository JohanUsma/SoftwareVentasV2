DELIMITER $$
CREATE PROCEDURE SP_MetodosPago_Listar(
    IN p_MetodoPagoID INT,
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
    IF p_MetodoPagoID IS NOT NULL THEN
        SELECT * FROM MetodosPago WHERE MetodoPagoID = p_MetodoPagoID;
    ELSE
        SELECT * FROM MetodosPago;
    END IF;

END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE SP_MetodosPago_Insertar(
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

    -- INSERT
    INSERT INTO MetodosPago (Nombre)
    VALUES (p_Nombre);

    IF v_error = 0 THEN
        SET p_resultado = 'Metodo Pago ingresado correctamente';
    END IF;

END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE SP_MetodosPago_Actualizar(
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

    -- UPDATE
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

END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE SP_MetodosPago_Eliminar(
    IN p_MetodoPagoID INT,
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
    DELETE FROM MetodosPago WHERE MetodoPagoID = p_MetodoPagoID;

    IF v_error = 0 THEN
        IF ROW_COUNT() = 0 THEN
            SET p_resultado = 'No se encontró el Metodo Pago para eliminar';
        ELSE
            SET p_resultado = 'Metodo Pago eliminado correctamente';
        END IF;
    END IF;

END $$
DELIMITER ;