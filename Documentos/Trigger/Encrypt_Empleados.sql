DELIMITER $$

CREATE TRIGGER encrypt_insert_empleados
BEFORE INSERT ON Empleados
FOR EACH ROW
BEGIN
    SET NEW.Correo = AES_ENCRYPT(NEW.Correo, 'P4ssw0rd');
    SET NEW.Telefono = AES_ENCRYPT(NEW.Telefono, 'P4ssw0rd');
END; $$

DELIMITER ;

---------------------------------------------------------------------

DELIMITER $$

CREATE TRIGGER encrypt_update_empleados
BEFORE UPDATE ON Empleados
FOR EACH ROW
BEGIN
    SET NEW.Correo = AES_ENCRYPT(NEW.Correo, 'P4ssw0rd');
    SET NEW.Telefono = AES_ENCRYPT(NEW.Telefono, 'P4ssw0rd');
END; $$

DELIMITER ;