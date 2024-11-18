DELIMITER $$

CREATE TRIGGER encrypt_insert_proveedores
BEFORE INSERT ON Proveedores
FOR EACH ROW
BEGIN
    SET NEW.Contacto = AES_ENCRYPT(NEW.Contacto, 'c0ntr4s3n4');
    SET NEW.Telefono = AES_ENCRYPT(NEW.Telefono, 'c0ntr4s3n4');
END; $$

DELIMITER ;

---------------------------------------------------------------------

DELIMITER $$

CREATE TRIGGER encrypt_update_proveedores
BEFORE UPDATE ON Proveedores
FOR EACH ROW
BEGIN
    SET NEW.Contacto = AES_ENCRYPT(NEW.Contacto, 'c0ntr4s3n4');
    SET NEW.Telefono = AES_ENCRYPT(NEW.Telefono, 'c0ntr4s3n4');
END; $$

DELIMITER ;
