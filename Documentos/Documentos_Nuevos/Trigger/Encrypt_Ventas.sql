DELIMITER $$

CREATE TRIGGER encrypt_insert_ventas
BEFORE INSERT ON Ventas
FOR EACH ROW
BEGIN
    SET NEW.Total = AES_ENCRYPT(NEW.Total, 'Cl4v3');
END $$

DELIMITER ;

---------------------------------------------------------------------

DELIMITER $$

CREATE TRIGGER encrypt_update_ventas
BEFORE UPDATE ON Ventas
FOR EACH ROW
BEGIN
    SET NEW.Total = AES_ENCRYPT(NEW.Total, 'Cl4v3');
END; $$

DELIMITER ;