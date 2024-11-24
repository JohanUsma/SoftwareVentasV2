DELIMITER $$

CREATE TRIGGER encrypt_insert_clientes
BEFORE INSERT ON Clientes
FOR EACH ROW
BEGIN
    SET NEW.Correo = AES_ENCRYPT(NEW.Correo, 'S3cr3t');
    SET NEW.Telefono = AES_ENCRYPT(NEW.Telefono, 'S3cr3t');
    SET NEW.Direccion = AES_ENCRYPT(NEW.Direccion, 'S3cr3t');
END; $$

DELIMITER ;

----------------------------------------------------------------------

DELIMITER $$

CREATE TRIGGER encrypt_update_clientes
BEFORE UPDATE ON Clientes
FOR EACH ROW
BEGIN
    SET NEW.Correo = AES_ENCRYPT(NEW.Correo, 'S3cr3t');
    SET NEW.Telefono = AES_ENCRYPT(NEW.Telefono, 'S3cr3t');
    SET NEW.Direccion = AES_ENCRYPT(NEW.Direccion, 'S3cr3t');
END; $$

DELIMITER ;