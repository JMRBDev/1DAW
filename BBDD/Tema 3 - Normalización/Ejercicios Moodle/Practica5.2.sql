CREATE DATABASE Electienda;
USE Electienda;

CREATE TABLE Tienda(Cod_Tienda int PRIMARY KEY,
                    Nom_Tienda varchar(100) NOT NULL,
                    Direc_Tienda varchar(100) NOT NULL,
                    Tlf_Tienda char(9) NOT NULL,
                    CHECK (Cod_Tienda>999 and Cod_Tienda<10000));

CREATE TABLE Electros(Cod_Elect char(9) PRIMARY KEY,
                      Descripcion varchar(100) NOT NULL);

CREATE TABLE Clientes(Cod_Cli int PRIMARY KEY,
                      Nom_Cli varchar(100) NOT NULL,
                      Domicilio_Cli varchar(100) NOT NULL,
                      Tlf_Cli char(9) NOT NULL,
                      CHECK (Cod_Cli>10000));

CREATE TABLE Precios(Cod_Elect char(9),
                     Cod_Tienda int,
                     Precio_Unidad decimal(4,2) NOT NULL,
                     CONSTRAINT precios_electro_fk FOREIGN KEY (Cod_Elect) REFERENCES Electros(Cod_Elect),
                     CONSTRAINT precios_tienda_fk FOREIGN KEY (Cod_Tienda) REFERENCES Tienda(Cod_Tienda),
                     CONSTRAINT precios_pk PRIMARY KEY (Cod_Elect, Cod_Tienda),
                     CHECK (Cod_Elect>100000),
                     CHECK (Cod_Tienda>99 and Cod_Tienda<1000));

CREATE TABLE Vendedor(NIF_Vendedor char(9) PRIMARY KEY,
                      Nombre_Vendedor varchar(100) NOT NULL,
                      Tlf_Vendedor char(9) NOT NULL);

CREATE TABLE Ventas(Cod_Elect char(9),
                    Cod_Tienda int,
                    Cod_Cli int,
                    FechaHora_Venta datetime,
                    Unidades_Vendidas int NOT NULL,
                    Descuento decimal(3,2) NOT NULL,
                    NIF_Vendedor char(9) NOT NULL,
                    CONSTRAINT ventas_precios_fk FOREIGN KEY (Cod_Elect, Cod_Tienda) REFERENCES Precios(Cod_Elect, Cod_Tienda),
                    CONSTRAINT ventas_clientes_fk FOREIGN KEY (Cod_Cli) REFERENCES Clientes(Cod_Cli),
                    CONSTRAINT ventas_pk PRIMARY KEY (Cod_Elect, Cod_Tienda, Cod_Cli, FechaHora_Venta),
                    CHECK (Unidades_Vendidas>=1));