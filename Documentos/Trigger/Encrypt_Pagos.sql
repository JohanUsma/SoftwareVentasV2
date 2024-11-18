DELIMITER $$

CREATE TRIGGER encrypt_insert_pagos
BEFORE INSERT ON Pagos
FOR EACH ROW
BEGIN
    SET NEW.Monto = AES_ENCRYPT(NEW.Monto, 'Cl4v3');
END $$

DELIMITER ;

---------------------------------------------------------------------

DELIMITER $$

CREATE TRIGGER encrypt_update_pagos
BEFORE UPDATE ON Pagos
FOR EACH ROW
BEGIN
    SET NEW.Monto = AES_ENCRYPT(NEW.Monto, 'Cl4v3');
END; $$

DELIMITER ;