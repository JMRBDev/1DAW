/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE IF NOT EXISTS `bank` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `bank`;

-- Dumping structure for table bank.accounts
DROP TABLE IF EXISTS `accounts`;
CREATE TABLE IF NOT EXISTS `accounts` (
  `id` int(11) NOT NULL,
  `account_holder_id` int(11) NOT NULL,
  `balance` decimal(19,4) DEFAULT '0.0000',
  PRIMARY KEY (`id`),
  KEY `fk_accounts_account_holders` (`account_holder_id`),
  CONSTRAINT `fk_accounts_account_holders` FOREIGN KEY (`account_holder_id`) REFERENCES `account_holders` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table bank.accounts: ~18 rows (approximately)
/*!40000 ALTER TABLE `accounts` DISABLE KEYS */;
INSERT INTO `accounts` (`id`, `account_holder_id`, `balance`) VALUES
	(1, 1, 123.1200),
	(2, 3, 4354.2300),
	(3, 12, 6546543.2300),
	(4, 9, 15345.6400),
	(5, 11, 36521.2000),
	(6, 8, 5436.3400),
	(7, 10, 565649.2000),
	(8, 11, 999453.5000),
	(9, 1, 5349758.2300),
	(10, 2, 543.3000),
	(11, 3, 10.2000),
	(12, 7, 245656.2300),
	(13, 5, 5435.3200),
	(14, 4, 1.2300),
	(15, 6, 0.1900),
	(16, 2, 5345.3400),
	(17, 11, 76653.2000),
	(18, 1, 235469.8900);
/*!40000 ALTER TABLE `accounts` ENABLE KEYS */;


-- Dumping structure for table bank.account_holders
DROP TABLE IF EXISTS `account_holders`;
CREATE TABLE IF NOT EXISTS `account_holders` (
  `id` int(11) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `ssn` char(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table bank.account_holders: ~12 rows (approximately)
/*!40000 ALTER TABLE `account_holders` DISABLE KEYS */;
INSERT INTO `account_holders` (`id`, `first_name`, `last_name`, `ssn`) VALUES
	(1, 'Susan', 'Cane', '1234567890'),
	(2, 'Kim', 'Novac', '1234567890'),
	(3, 'Jimmy', 'Henderson', '1234567890'),
	(4, 'Steve', 'Stevenson', '1234567890'),
	(5, 'Bjorn', 'Sweden', '1234567890'),
	(6, 'Kiril', 'Petrov', '1234567890'),
	(7, 'Petar', 'Kirilov', '1234567890'),
	(8, 'Michka', 'Tsekova', '1234567890'),
	(9, 'Zlatina', 'Pateva', '1234567890'),
	(10, 'Monika', 'Miteva', '1234567890'),
	(11, 'Zlatko', 'Zlatyov', '1234567890'),
	(12, 'Petko', 'Petkov Junior', '1234567890');
/*!40000 ALTER TABLE `account_holders` ENABLE KEYS */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;


USE bank;

-- 10
DROP PROCEDURE IF EXISTS nombreCompleto;
DELIMITER $$
CREATE PROCEDURE nombreCompleto()
BEGIN
    SELECT 
        CONCAT(' ', h.first_name, h.last_name) AS 'Nombre completo'
    FROM
        account_holders h
            JOIN
        (SELECT DISTINCT
            a.account_holder_id
        FROM
            accounts a) a ON h.id = a.account_holder_id
    ORDER BY `Nombre completo`;
END $$
DELIMITER ;

CALL nombreCompleto();

-- 11
DROP PROCEDURE IF EXISTS genteconmasdinerototal;
DELIMITER $$
CREATE PROCEDURE genteconmasdinerototal(cantidad DECIMAL(19, 4))
BEGIN
    SELECT 
         CONCAT(' ', h.first_name, h.last_name) AS 'Nombre completo'
    FROM
        account_holders h
            JOIN (SELECT 
				a.id, a.account_holder_id, SUM(a.balance) AS 'Dinero total'
			FROM
				accounts a
			GROUP BY (a.account_holder_id)
			HAVING `Dinero total` > cantidad) AS a ON h.id = a.account_holder_id
	ORDER BY `Nombre completo`;
END $$
DELIMITER ;

CALL genteconmasdinerototal(50000);

-- 12
DROP FUNCTION IF EXISTS valorfuturodelasuma;
DELIMITER $$
CREATE FUNCTION valorfuturodelasuma(
    suma DECIMAL(14, 4), interesAnual DECIMAL(14, 4), años INT)
RETURNS DECIMAL(14, 4)
DETERMINISTIC
BEGIN
    RETURN suma * POW((1 + interesAnual), años);
END $$
DELIMITER ;

SELECT valorfuturodelasuma(1000, 2, 3);

-- 13
DROP FUNCTION IF EXISTS formula_grande;
DELIMITER $$
CREATE FUNCTION formula_grande(
	  I 	DECIMAL(14,4),
    R 	DECIMAL(14,4),
    T 	DECIMAL(14,4)
)
RETURNS DECIMAL(14,4)
DETERMINISTIC
BEGIN
	DECLARE FV DECIMAL(14,4);
    SET FV = I * (1 + R);
    RETURN POW(FV,T);
END $$
DELIMITER ;

SELECT formula_grande(4,3,9);

-- 14
delimiter $$
CREATE PROCEDURE calcular_valor_futuro_cuenta (account_id INT, interest_rate DECIMAL(19,4))

BEGIN
	DECLARE future_value DECIMAL(14, 4);
    DECLARE balance DECIMAL(14, 4);
    SET balance := (SELECT a.balance FROM accounts AS a WHERE a.d = account_id);
    SET future_balance := valor_futuro(balance, interest_rate, 5);
    -- balance * (POW((1 + interest_rate), 5))_;
    
    SELECT 
		a.id AS account_id,
		ah.FirstName,
		ah.LastName,
		a.balance,
		future_value
	FROM
		accounts AS a
		INNER JOIN account_holders AS ah ON a.account_holder_id = ah_id
		AND a.id = account_id;
END $$
delimiter ;

-- 15 // ESTÁ MAL
delimiter $$
CREATE TRIGGER info_cuentas AFTER UPDATE ON accounts FOR EACH ROW
BEGIN
	SELECT ah.first_name 'Nombre', ah.last_name 'Apellido', a.balance
    FROM account_holders ah
    JOIN accounts a
    WHERE ah.id = a.id;
END $$

delimiter ;

-- 16

-- 17
delimiter $$
DROP PROCEDURE IF EXISTS retirardinero;
CREATE PROCEDURE retirardinero(
    idCuenta INT, cantidad DECIMAL(14, 4))
BEGIN
    IF accounts.balance > 0 THEN
        START TRANSACTION;
        UPDATE accounts a
        SET
            a.balance = a.balance - cantidad
        WHERE
            a.id = account_id;
        IF (SELECT a.balance
            FROM accounts a
            WHERE a.id = idCuenta) < 0
            THEN ROLLBACK;
        ELSE
            COMMIT;
        END IF;
    END IF;
END $$
delimiter ;

CALL retirardinero(13, 10);

SELECT
    a.id 'ID Cuenta', a.balance
FROM
    accounts a
WHERE
    a.id = 1;
    
-- 18
delimiter $$
DROP PROCEDURE IF EXISTS depositardinero;
CREATE PROCEDURE depositardinero(
    idCuenta INT, cantidad DECIMAL(14, 4))
BEGIN
    START TRANSACTION;
	UPDATE accounts a
    SET
        a.balance = a.balance + cantidad
    WHERE
        a.id = account_id;
    IF (SELECT a.balance
        FROM accounts a
        WHERE a.id = idCuenta) < 0
        THEN ROLLBACK;
    ELSE
        COMMIT;
    END IF;
END $$
delimiter ;

CALL depositardinero(13, 10);

SELECT
    a.id 'ID Cuenta', a.balance
FROM
    accounts a
WHERE
    a.id = 1;
    
-- 19
delimiter $$
DROP PROCEDURE IF EXISTS transferirdinero;
CREATE PROCEDURE transferirdinero(
    cuentaOrigen INT, cuentaDestino INT, cantidad DECIMAL(19, 4))
BEGIN
    IF (SELECT a.balance
		FROM accounts a
		WHERE a.id = cuentaOrigen) >= cantidad
    THEN
        START TRANSACTION;
        
        UPDATE accounts a
        SET
            a.balance = a.balance + cantidad
        WHERE
            a.id = cuentaDestino;
            
        UPDATE accounts a
        SET
            a.balance = a.balance - cantidad
        WHERE
            a.id = cuentaOrigen;
        
        IF (SELECT a.balance
            FROM accounts a
            WHERE a.id = cuentaOrigen) < 0
            THEN ROLLBACK;
        ELSE
            COMMIT;
        END IF;
    END IF;
END $$
delimiter ;

CALL transferirdinero(10, 12, 10);

SELECT
    a.id 'ID de cuenta', a.balance 'Balance'
FROM
    accounts a
WHERE
    a.id IN (10, 12);
    
-- 20

-- 21
DROP TABLE IF EXISTS tabla_logs;
CREATE TABLE tabla_logs (
    log_id INT PRIMARY KEY AUTO_INCREMENT,
    account_id INT NOT NULL,
    old_sum DECIMAL(14, 4) NOT NULL,
    new_sum DECIMAL(14, 4) NOT NULL);

DELIMITER $$
DROP TRIGGER IF EXISTS registrarlog;
CREATE TRIGGER registrarlog
AFTER UPDATE ON accounts
FOR EACH ROW
BEGIN
    IF OLD.balance <> NEW.balance THEN
        INSERT INTO tabla_logs
            (account_id, old_sum, new_sum)
        VALUES (OLD.id, OLD.balance, NEW.balance);
    END IF;
END $$
DELIMITER ;

CALL transferirdinero(10, 12, 10);

SELECT * FROM tabla_logs;

-- 22
DROP TABLE IF EXISTS emails;
CREATE TABLE emails (
    id INT PRIMARY KEY AUTO_INCREMENT,
    receptor INT NOT NULL,
    asunto VARCHAR(100) NOT NULL,
    mensaje VARCHAR(1000) NOT NULL);

DELIMITER $$
DROP TRIGGER IF EXISTS crearemail;
CREATE TRIGGER crearemail
AFTER INSERT ON tabla_logs
FOR EACH ROW
BEGIN
    INSERT INTO emails
        (receptor, asunto, mensaje)
    VALUES (
        NEW.account_id,
        CONCAT('Cambio en el balance de la cuenta: ', NEW.account_id),
        CONCAT('A fecha ', DATE_FORMAT(NOW(), '%d %M %Y'), ' el balance de su cuenta ', NEW.account_id, ' a cambiado de ' , ROUND(NEW.old_sum, 2), ' a ', ROUND(NEW.new_sum, 2), '.'));
END $$
DELIMITER ;

SELECT * FROM emails;