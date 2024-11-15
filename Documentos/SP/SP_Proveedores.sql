DELIMITER $$
CREATE PROCEDURE SP_Proveedores_Listar(
    IN p_ProveedorID INT,
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
    IF p_ProveedorID IS NOT NULL THEN
        SELECT ProveedorID, Nombre,
        CAST(AES_DECRYPT(Contacto, 'c0ntr4s3n4') AS CHAR(100)) AS Contacto,
        CAST(AES_DECRYPT(Telefono, 'c0ntr4s3n4') AS CHAR(100)) AS Telefono
        FROM Proveedores WHERE ProveedorID = p_ProveedorID;
    ELSE
        SELECT * FROM Proveedores;
    END IF;

END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE SP_Proveedores_Insertar(
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

    -- INSERT
    INSERT INTO Proveedores (Nombre, Contacto, Telefono)
    VALUES (p_Nombre, p_Contacto, p_Telefono);

    IF v_error = 0 THEN
        SET p_resultado = 'Proveedor ingresado correctamente';
    END IF;

END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE SP_Proveedores_Actualizar(
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

    -- UPDATE
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

END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE SP_Proveedores_Eliminar(
    IN p_ProveedorID INT,
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
    DELETE FROM Proveedores WHERE ProveedorID = p_ProveedorID;

    IF v_error = 0 THEN
        IF ROW_COUNT() = 0 THEN
            SET p_resultado = 'No se encontró el proveedor para eliminar';
        ELSE
            SET p_resultado = 'Proveedor eliminado correctamente';
        END IF;
    END IF;

END $$
DELIMITER ;