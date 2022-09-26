DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS countries;

CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    country_name VARCHAR(255),
    continent VARCHAR(255),
    city VARCHAR(255),
    visited BOOLEAN
);

CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    city_name VARCHAR(255),
    country_id VARCHAR(255) REFERENCES countries(country_name),
    visited BOOLEAN
);