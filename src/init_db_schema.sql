DROP TABLE IF EXISTS human CASCADE;
DROP TABLE IF EXISTS name_details CASCADE;
DROP TABLE IF EXISTS coordinates CASCADE;
DROP TABLE IF EXISTS location CASCADE;
DROP TABLE IF EXISTS timezone CASCADE;
DROP TABLE IF EXISTS login_details CASCADE;
DROP TABLE IF EXISTS birth_date_details CASCADE;
DROP TABLE IF EXISTS registration_details CASCADE;
DROP TABLE IF EXISTS personal_number CASCADE;
DROP TABLE IF EXISTS picture_links CASCADE;

CREATE TABLE name_details (
    id SERIAL PRIMARY KEY,
    title VARCHAR(32) NULL,
    first_name VARCHAR(32) NULL,
    last_name VARCHAR(32) NULL
);

CREATE TABLE coordinates (
    id SERIAL PRIMARY KEY,
    latitude FLOAT,
    longitude FLOAT
);

CREATE TABLE timezone (
    id SERIAL PRIMARY KEY,
    t_offset VARCHAR(16),
    description VARCHAR(32)
);

CREATE TABLE location (
    id SERIAL PRIMARY KEY,
    street VARCHAR(64),
    city VARCHAR(32),
    state VARCHAR(32),
    postcode VARCHAR(16),
    id_coordinates INTEGER NULL,
    FOREIGN KEY(id_coordinates) REFERENCES coordinates(id)
);

CREATE TABLE login_details (
    id SERIAL PRIMARY KEY,
    uuid VARCHAR(64),
    username VARCHAR(32),
    password VARCHAR(32),
    salt VARCHAR(32),
    md5_hash VARCHAR(64),
    sha1_hash VARCHAR(64),
    sha256_hash VARCHAR(64)
);

CREATE TABLE birth_date_details (
    id SERIAL PRIMARY KEY,
    birth_date TIMESTAMP,
    age INTEGER
);

CREATE TABLE registration_details (
    id SERIAL PRIMARY KEY,
    date TIMESTAMP,
    age INTEGER
);

CREATE TABLE personal_number (
    id SERIAL PRIMARY KEY,
    name VARCHAR(16),
    value VARCHAR(32)
);

CREATE TABLE picture_links (
    id SERIAL PRIMARY KEY,
    large VARCHAR(128),
    medium VARCHAR(128),
    thumbnail VARCHAR(128)
);

CREATE TABLE human (
    id SERIAL PRIMARY KEY,
    gender VARCHAR(16) NULL,
    id_name INTEGER NULL,
    email VARCHAR(64),
    id_login INTEGER,
    id_birth INTEGER,
    id_registered INTEGER,
    phone VARCHAR(32),
    cell VARCHAR(32),
    id_p_num INTEGER,
    id_pictures INTEGER,
    nationality VARCHAR(8),
    FOREIGN KEY (id_name) REFERENCES name_details(id),
    FOREIGN KEY (id_login) REFERENCES login_details(id),
    FOREIGN KEY (id_birth) REFERENCES birth_date_details(id),
    FOREIGN KEY (id_registered) REFERENCES registration_details(id),
    FOREIGN KEY (id_p_num) REFERENCES personal_number(id),
    FOREIGN KEY (id_pictures) REFERENCES picture_links(id)
);