DROP TABLE IF EXISTS destinations;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255)
);

CREATE TABLE destinations (
    id SERIAL PRIMARY KEY,
    continent VARCHAR(255),
    country VARCHAR(255),
    city VARCHAR(255),
    sight VARCHAR(255),
    visited BOOLEAN,
    user_id INT NOT NULL REFERENCES users(id)
);