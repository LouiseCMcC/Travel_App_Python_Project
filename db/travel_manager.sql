DROP TABLE IF EXISTS sights;
DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS countries;

CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    country_name VARCHAR(255),
    continent VARCHAR(255),
    visited BOOLEAN
);

CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    city_name VARCHAR(255),
    country_id INT NOT NULL REFERENCES countries(id),
    visited BOOLEAN
);

CREATE TABLE sights (
    id SERIAL PRIMARY KEY,
    sight_name VARCHAR(255),
    city_id INT NOT NULL REFERENCES cities(id),
    visited BOOLEAN
);