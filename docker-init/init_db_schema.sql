DROP TABLE IF EXISTS human;


CREATE TABLE human (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(32),
    gender VARCHAR(16),
    email VARCHAR(64),
    phone VARCHAR(32),
    cell VARCHAR(32),
    picture_url VARCHAR(128),
    nationality VARCHAR(8)
);