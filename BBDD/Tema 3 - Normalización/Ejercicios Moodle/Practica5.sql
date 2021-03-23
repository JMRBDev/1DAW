CREATE DATABASE Multas;
USE Multas;

CREATE TABLE Infraccion(Codigo_Infraccion decimal(4) PRIMARY KEY,
                        Importe_Sancion decimal(5) NOT NULL,
                        Descripcion_Infraccion varchar(300) NOT NULL);

CREATE TABLE Infractor(NIF_Sancionado varchar(9) PRIMARY KEY,
                       Nombre_Sancionado varchar(100) NOT NULL);

CREATE TABLE Agente(NIF_Agente varchar(9) PRIMARY KEY,
                    Num_Agente decimal(4) UNIQUE NOT NULL,
                    Nombre_Agente varchar(100) NOT NULL,
                    Rango_Agente varchar(20) NOT NULL DEFAULT 'Agente');

CREATE TABLE Denuncia(NIF_Agente varchar(9) NOT NULL,
                      FechaHora_Infraccion dateTime DEFAULT NOW(),
                      Lugar varchar(200) NOT NULL,
                      Codigo_Infraccion decimal(4),
                      Matricula varchar(7) NOT NULL,
                      NIF_Sancionado varchar(9),
                      Papel_Sancionado varchar(20) NOT NULL,
                      Inmovilizado ENUM('S','N') NOT NULL DEFAULT 'N',
                      Matricula_Grua varchar(7),
                      NIF_Grua varchar(9),
                      CONSTRAINT denuncia_pk PRIMARY KEY (FechaHora_Infraccion, Codigo_Infraccion, NIF_Sancionado),
                      CONSTRAINT denuncia_infraccion_fk FOREIGN KEY (Codigo_Infraccion) REFERENCES Infraccion(Codigo_Infraccion),
                      CONSTRAINT denuncia_infractor_fk FOREIGN KEY (NIF_Sancionado) REFERENCES Infractor(NIF_Sancionado),
                      CONSTRAINT denuncia_agente_fk FOREIGN KEY (NIF_Agente) REFERENCES Agente(NIF_Agente));

CREATE TABLE Vehiculo(Matricula varchar(7) PRIMARY KEY,
                      Marca varchar(30) NOT NULL,
                      Modelo varchar(30) NOT NULL,
                      Color varchar(30),
                      NIF_Propietario varchar(9) NOT NULL,
                      CIA_Aseguradora decimal(10),
                      NUM_Poliza varchar(15));

CREATE TABLE Propietario(NIF_Propietario varchar(9) PRIMARY KEY,
                         Nombre_Propietario varchar(50) NOT NULL);