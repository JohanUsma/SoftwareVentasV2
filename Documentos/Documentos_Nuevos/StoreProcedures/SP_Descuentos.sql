DELIMITER $$
CREATE PROCEDURE SP_Descuentos_Listar(
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
    IF p_DescuentoID IS NOT NULL THEN
        SELECT * FROM Descuentos WHERE DescuentoID = p_DescuentoID;
    ELSE
        SELECT * FROM Descuentos;
    END IF;

END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE SP_Descuentos_Insertar(
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

    -- INSERT
    INSERT INTO Descuentos (Nombre, Descripcion, Porcentaje)
    VALUES (p_Nombre, p_Descripcion, p_Porcentaje);

    IF v_error = 0 THEN
        SET p_resultado = 'Descuento ingresado correctamente';
    END IF;

END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE SP_Descuentos_Actualizar(
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
    
    -- UPDATE
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

END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE SP_Descuentos_Eliminar(
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

    -- DELETE
    DELETE FROM Descuentos WHERE DescuentoID = p_DescuentoID;

    IF v_error = 0 THEN
        IF ROW_COUNT() = 0 THEN
            SET p_resultado = 'No se encontró el Descuento para eliminar';
        ELSE
            SET p_resultado = 'Descuento eliminado correctamente';
        END IF;
    END IF;

END $$
DELIMITER ;