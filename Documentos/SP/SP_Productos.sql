DELIMITER $$
CREATE PROCEDURE SP_Productos_Listar(
    IN p_ProductoID INT,
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
    IF p_ProductoID IS NOT NULL THEN
        SELECT * FROM Productos WHERE ProductoID = p_ProductoID;
    ELSE
        SELECT * FROM Productos;
    END IF;

END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE SP_Productos_Insertar(
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

    -- INSERT
    INSERT INTO Productos (Nombre, Precio, Stock)
    VALUES (p_Nombre, p_Precio, p_Stock);

    IF v_error = 0 THEN
        SET p_resultado = 'Producto ingresado correctamente';
    END IF;

END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE SP_Productos_Actualizar(
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

    -- UPDATE
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

END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE SP_Productos_Eliminar(
    IN p_ProductoID INT,
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

    -- DELETE
    DELETE FROM Productos WHERE ProductoID = p_ProductoID;

    IF v_error = 0 THEN
        IF ROW_COUNT() = 0 THEN
            SET p_resultado = 'No se encontró el producto para eliminar';
        ELSE
            SET p_resultado = 'Producto eliminado correctamente';
        END IF;
    END IF;

END $$
DELIMITER ;