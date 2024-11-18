DELIMITER $$
CREATE PROCEDURE SP_ProductosDescuentos_Listar(
    IN p_ProductoDescuentoID INT,
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
    IF p_ProductoDescuentoID IS NOT NULL THEN
        SELECT * FROM ProductoDescuento WHERE ProductoDescuentoID = p_ProductoDescuentoID;
    ELSE
        SELECT * FROM ProductoDescuento;
    END IF;

END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE SP_ProductosDescuentos_Insertar(
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

    -- INSERT
    INSERT INTO ProductoDescuento (ProductoID, DescuentoID)
    VALUES (p_ProductoID, p_DescuentoID);

    IF v_error = 0 THEN
        SET p_resultado = 'Descuento de Producto ingresado correctamente';
    END IF;

END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE SP_ProductosDescuentos_Actualizar(
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

    -- UPDATE
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

END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE SP_ProductosDescuentos_Eliminar(
    IN p_ProductoDescuentoID INT,
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
    DELETE FROM ProductoDescuento WHERE ProductoDescuentoID = p_ProductoDescuentoID;

    IF v_error = 0 THEN
        IF ROW_COUNT() = 0 THEN
            SET p_resultado = 'No se encontró el Descuento del Producto para eliminar';
        ELSE
            SET p_resultado = 'Descuento del Producto eliminado correctamente';
        END IF;
    END IF;

END $$
DELIMITER ;