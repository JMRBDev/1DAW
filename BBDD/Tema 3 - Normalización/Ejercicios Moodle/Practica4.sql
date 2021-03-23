CREATE TABLE Centros(Numero decimal(8) PRIMARY KEY,
                     Nombre varchar(10) NOT NULL,
                     Direccion varchar(250) NOT NULL);

CREATE TABLE Empleados(Cod decimal(8) PRIMARY KEY,
                       Departamento decimal(8) NOT NULL,
                       Telefono decimal(9) NOT NULL,
                       Fecha_nacimiento date NOT NULL,
                       Fecha_ingreso date NOT NULL,
                       Salario decimal(5) NOT NULL,
                       Comision decimal(5),
                       Num_hijos decimal(2),
                       Nombre varchar(50) NOT NULL);

CREATE TABLE Departamentos(Numero decimal(8) PRIMARY KEY,
                           Centro decimal(8) NOT NULL,
                           Director decimal(6) NOT NULL,
                           Tipo_dir ENUM('P','F') NOT NULL,
                           Presupuesto decimal(5) NOT NULL,
                           Depto_jefe decimal(8),
                           Nombre varchar(50) NOT NULL,
                           CONSTRAINT dept_centros_fk FOREIGN KEY (Centro) REFERENCES Centros(Numero),
                           CONSTRAINT dept_empleados_fk FOREIGN KEY (Director) REFERENCES Empleados(Cod));

ALTER TABLE Empleados
ADD CONSTRAINT empleados_dept_fk FOREIGN KEY (Departamento) REFERENCES Departamentos(Numero);