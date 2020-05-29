DROP DATABASE cine;
CREATE DATABASE IF NOT EXISTS cine;
USE cine;

CREATE TABLE IF NOT EXISTS usuarios(
	username VARCHAR(30) UNIQUE NOT NULL,
    nombre VARCHAR(80) NOT NULL,
    apellido_pat VARCHAR(80) NOT NULL,
	apellido_mat VARCHAR(80) NOT NULL, 
    contraseña VARCHAR(80) NOT NULL,
    admin ENUM('Si', 'No') NOT NULL,
    PRIMARY KEY (username)
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS peliculas(
	pelicula_id INT UNIQUE NOT NULL,
    titulo VARCHAR(80) NOT NULL,
    descripcion VARCHAR(255) NOT NULL,
    duracion INT NOT NULL,
    idioma ENUM('Español', 'Ingles') NOT NULL,
    subtitulos ENUM('Español', 'Ingles', 'No') NOT NULL,
    clasificacion ENUM ('AA', 'A', 'B', 'B-15', 'C', 'D') NOT NULL,
    precio_pelicula FLOAT NOT NULL
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS asientos(
	asiento_id INT UNIQUE NOT NULL,
    categoria VARCHAR(50) NOT NULL
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS salas(
	numero_sala INT UNIQUE NOT NULL,
    tipo ENUM ('Premium', 'Xtremo', 'X4D', 'Platino', 'Tradicional'),
    descripcion VARCHAR(255) NOT NULL,
    precio_sala FLOAT NOT NULL
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS sala_asiento(
    sa_numero_sala INT NOT NULL,
    sa_asiento_id INT NOT NULL,
    cantidad INT NOT NULL,
    PRIMARY KEY (sa_asiento_id, sa_numero_sala),
    CONSTRAINT fk_sa_asiento_id
    FOREIGN KEY(sa_asiento_id)
    REFERENCES asientos(asiento_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    CONSTRAINT fk_sa_numero_sala
    FOREIGN KEY(sa_numero_sala)
    REFERENCES salas(numero_sala)
    ON DELETE CASCADE
    ON UPDATE CASCADE
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS horario(
	horario_id INT NOT NULL AUTO_INCREMENT,
    h_pelicula_id INT NOT NULL,
    h_numero_sala INT NOT NULL,
    fecha_hora DATETIME NOT NULL,
    asientos_disponibles INT NOT NULL,
    terminado ENUM('Si', 'No') NOT NULL,
    PRIMARY KEY (horario_id),
    CONSTRAINT fk_h_pelicula_id
    FOREIGN KEY (h_pelicula_id)
    REFERENCES peliculas(pelicula_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    CONSTRAINT fk_h_numero_sala
    FOREIGN KEY (h_numero_sala)
    REFERENCES salas(numero_sala)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
	UNIQUE KEY (fecha_hora, h_numero_sala, h_pelicula_id)
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS tickets(
	ticket_id INT NOT NULL AUTO_INCREMENT,
    t_username VARCHAR(30) NOT NULL,
    t_horario_id INT NOT NULL,
    precio_ticket FLOAT NOT NULL,
    PRIMARY KEY (ticket_id),
    CONSTRAINT fk_t_username
    FOREIGN KEY (t_username)
    REFERENCES usuarios(username)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    CONSTRAINT fk_t_horario_id
    FOREIGN KEY (t_horario_id)
    REFERENCES horario(horario_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
)ENGINE = INNODB;


-- Insercion de usuarios
INSERT INTO usuarios VALUES('andy', 'Andres', 'Castro', 'Cabrera', '1234', 'Si');
INSERT INTO usuarios VALUES('sandy', 'Sandra', 'Castro', 'Cabrera', '4321', 'No');

-- Insercion de peliculas
INSERT INTO peliculas VALUES(1, 'Titanic', 'Un barco se unde.', 120, 'Español', 'Español', 'B-15', 30.5);
INSERT INTO peliculas VALUES(2, 'Cars', 'Un coche con problemas de ego.', 125, 'Español', 'No', 'AA', 30.5);

-- Insercion de asientos
INSERT INTO asientos VALUES(1, 'Chico');
INSERT INTO asientos VALUES(2, 'Mediano');
INSERT INTO asientos VALUES(3, 'Grande');

-- Insercion de salas
INSERT INTO salas VALUES(1, 'Tradicional', 'Sala normal de imagen en 2 dimensiones.', 20.0);
INSERT INTO salas VALUES(2, 'Premium', 'Sala normal de imagen en 2 o 3 dimensiones y asientos grandes.', 30.0);
INSERT INTO salas VALUES(3, 'Xtremo', 'Sala con asientos grandes de pantalla grande e imagen en 2 o 3 dimensiones.', 40.0);
INSERT INTO salas VALUES(4, 'X4D', 'Experiencia 4D con efectos de luz movimiento y ambiente.', 50.0);
INSERT INTO salas VALUES(5, 'Platino', 'Sala VIP con las mejores atenciones.', 60.0);

-- Insercion de sala-asiento
INSERT INTO sala_asiento VALUES(1, 1, 70);
INSERT INTO sala_asiento VALUES(2, 3, 50);
INSERT INTO sala_asiento VALUES(3, 2, 40);
INSERT INTO sala_asiento VALUES(4, 3, 30);
INSERT INTO sala_asiento VALUES(5, 3, 20);

-- Insercion de horario
INSERT INTO horario(h_pelicula_id, h_numero_sala, fecha_hora, asientos_disponibles, terminado) VALUES(1,2, '2020-05-29 16:15:00',15, 'Si');
INSERT INTO horario(h_pelicula_id, h_numero_sala, fecha_hora, asientos_disponibles, terminado) VALUES(2,1, '2020-05-29 18:15:00',40, 'No');
INSERT INTO horario(h_pelicula_id, h_numero_sala, fecha_hora, asientos_disponibles, terminado) VALUES(1,3, '2020-05-29 13:00:00',30, 'No');
INSERT INTO horario(h_pelicula_id, h_numero_sala, fecha_hora, asientos_disponibles, terminado) VALUES(1,5, '2020-06-02 12:30:00',2, 'No');