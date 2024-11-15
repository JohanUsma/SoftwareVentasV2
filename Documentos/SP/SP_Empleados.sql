DELIMITER $$
CREATE PROCEDURE SP_Empleados_Listar(
    IN p_EmpleadoID INT,
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
    IF p_EmpleadoID IS NOT NULL THEN
        SELECT EmpleadoID, Nombre, Apellido,
        CAST(AES_DECRYPT(Correo, 'P4ssw0rd') AS CHAR(100)) AS Correo,
        CAST(AES_DECRYPT(Telefono, 'P4ssw0rd') AS CHAR(100)) AS Telefono
        FROM Empleados WHERE EmpleadoID = p_EmpleadoID;
    ELSE
        SELECT * FROM Empleados;
    END IF;

END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE SP_Empleados_Insertar(
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

    -- INSERT
    INSERT INTO Empleados (Nombre, Apellido, Correo, Telefono)
    VALUES (p_Nombre, p_Apellido, p_Correo, p_Telefono);

    IF v_error = 0 THEN
        SET p_resultado = 'Empleado ingresado correctamente';
    END IF;

END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE SP_Empleados_Actualizar(
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

    -- UPDATE
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

END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE SP_Empleados_Eliminar(
    IN p_EmpleadoID INT,
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
    DELETE FROM Empleados WHERE EmpleadoID = p_EmpleadoID;

    IF v_error = 0 THEN
        IF ROW_COUNT() = 0 THEN
            SET p_resultado = 'No se encontró el empleado para eliminar';
        ELSE
            SET p_resultado = 'Empleado eliminado correctamente';
        END IF;
    END IF;

END $$
DELIMITER ;