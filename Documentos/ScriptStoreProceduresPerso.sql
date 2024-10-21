-- SP_Stock_Productos ======================================================================================
DELIMITER $$
CREATE PROCEDURE SP_Stock_Productos()
BEGIN
    DECLARE v_error INT DEFAULT 0;
    DECLARE v_error_message VARCHAR(255);

    -- MANEJAR EXCEPCIONES
    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION 
    BEGIN
        DECLARE v_error_message VARCHAR(255);
        GET DIAGNOSTICS CONDITION 1 v_error_message = MESSAGE_TEXT;
        SELECT CONCAT('Error: ', v_error_message) AS ErrorMensaje;
    END;

    SELECT * FROM Productos WHERE Stock < 50;
END $$
DELIMITER ;

-- SP_Top_Productos ======================================================================================
DELIMITER $$
CREATE PROCEDURE SP_Top_Productos()
BEGIN
    DECLARE v_error INT DEFAULT 0;
    DECLARE v_error_message VARCHAR(255);

    -- MANEJAR EXCEPCIONES
    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION 
    BEGIN
        DECLARE v_error_message VARCHAR(255);
        GET DIAGNOSTICS CONDITION 1 v_error_message = MESSAGE_TEXT;
        SELECT CONCAT('Error: ', v_error_message) AS ErrorMensaje;
    END;

    SELECT p.Nombre, SUM(dv.Cantidad) AS TotalVendido
    FROM DetallesVentas dv
    JOIN Productos p ON dv.ProductoID = p.ProductoID
    GROUP BY p.Nombre
    ORDER BY TotalVendido DESC
    LIMIT 3;

END $$
DELIMITER ;