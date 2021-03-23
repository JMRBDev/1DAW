CREATE DATABASE MediaMarkting;
USE MediaMarkting;

CREATE TABLE Alquiler(cod_alquiler char(6) PRIMARY KEY,
					  cod_cliente char(6) NOT NULL,
                      valor_alquiler int NOT NULL);
                      
CREATE TABLE AlquilerCliente(cod_alquiler char(6),
							 cod_dvds char(6),
                             fecha_alquiler date NOT NULL,
                             fecha_dev date NOT NULL,
                             cantidad int NOT NULL,
                             CONSTRAINT alquilerCliente_pk PRIMARY KEY (cod_alquiler, cod_dvds));
                             
CREATE TABLE Cliente(cod_cliente char(6) PRIMARY KEY,
					 nom_cliente varchar(150) NOT NULL,
                     dir_cliente varchar(250) NOT NULL,
                     cp_direccion varchar(15) NOT NULL,
                     ciudad varchar(100) NOT NULL,
                     telef_cliente varchar(9) NOT NULL,
                     fecha_nac_cliente date NOT NULL,
                     edad_cliente int NOT NULL,
                     CHECK (edad_cliente > 0 and edad_cliente < 140),
                     datos_cliente varchar(500) NOT NULL);
                     
CREATE TABLE Dvds(cod_dvds char(6) PRIMARY KEY,
				  num_copias int NOT NULL,
                  formato ENUM('dvd', 'bluray', 'blurayEXT') NOT NULL DEFAULT 'dvd',
                  cod_pelicula char(6) NOT NULL);
                  
CREATE TABLE Pelicula(cod_pelicula char(6) PRIMARY KEY,
					  titulo varchar(150) NOT NULL,
                      cod_tipo char(6) NOT NULL);
                      
CREATE TABLE TipoPelicula(cod_tipo char(6) PRIMARY KEY,
						  categoria ENUM('comedia', 'suspense', 'drama', 'accion',
										 'ciencia ficcion', 'romantico', 'terror') NOT NULL);
                                         
CREATE TABLE PeliculaActor(cod_pelicula char(6),
						   cod_actor char(6),
                           CONSTRAINT peliculaActor_pk PRIMARY KEY (cod_pelicula, cod_actor));
                           
CREATE TABLE Actor(cod_actor char(6) PRIMARY KEY,
				   nom_actor varchar(150) NOT NULL,
                   fecha_nac_actor date NOT NULL);
                   
                   
ALTER TABLE Alquiler
ADD CONSTRAINT alquiler_cliente_fk FOREIGN KEY (cod_cliente) REFERENCES Cliente(cod_cliente);

ALTER TABLE Dvds
ADD CONSTRAINT dvds_pelicula_fk FOREIGN KEY (cod_pelicula) REFERENCES Pelicula(cod_pelicula);

ALTER TABLE Pelicula
ADD CONSTRAINT pelicula_tipoPelicula_fk FOREIGN KEY (cod_tipo) REFERENCES TipoPelicula(cod_tipo);