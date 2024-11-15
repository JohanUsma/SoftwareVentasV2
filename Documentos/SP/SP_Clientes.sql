DELIMITER $$
CREATE PROCEDURE SP_Clientes_Listar(
    IN p_ClienteID INT,
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
    IF p_ClienteID IS NOT NULL THEN
        SELECT * FROM Clientes WHERE ClienteID = p_ClienteID;
    ELSE
        SELECT * FROM Clientes;
    END IF;

END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE SP_Clientes_Insertar(
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
    
    -- INSERT
    INSERT INTO Clientes (Nombre, Apellido, Correo, Direccion, Telefono)
    VALUES (p_Nombre, p_Apellido, p_Correo, p_Direccion, p_Telefono);

    IF v_error = 0 THEN
        SET p_resultado = 'Cliente ingresado correctamente';
    END IF;

END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE SP_Clientes_Actualizar(
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
    
    -- UPDATE
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

END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE SP_Clientes_Eliminar(
    IN p_ClienteID INT,
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
    DELETE FROM Clientes WHERE ClienteID = p_ClienteID;

    IF v_error = 0 THEN
        IF ROW_COUNT() = 0 THEN
            SET p_resultado = 'No se encontró el cliente para eliminar';
        ELSE
            SET p_resultado = 'Cliente eliminado correctamente';
        END IF;
    END IF;

END $$
DELIMITER ;