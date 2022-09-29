DROP TABLE IF EXISTS sights;
DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS countries;
DROP TABLE IF EXISTS blogs;
DROP TABLE IF EXISTS photos;

CREATE TABLE photos (
    id SERIAL PRIMARY KEY,
    photo_date INT,
    photo_location VARCHAR (255),
    photo_url VARCHAR (255)
);

CREATE TABLE blogs (
    id SERIAL PRIMARY KEY,
    blog_name VARCHAR(255),
    blog_date INT,
    blog_content TEXT
);

CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    country_name VARCHAR(255),
    continent VARCHAR(255),
    visited BOOLEAN
);

CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    city_name VARCHAR(255),
    country_id INT NOT NULL REFERENCES countries(id) ON DELETE CASCADE,
    visited BOOLEAN
);

CREATE TABLE sights (
    id SERIAL PRIMARY KEY,
    sight_name VARCHAR(255),
    city_id INT NOT NULL REFERENCES cities(id) ON DELETE CASCADE,
    visited BOOLEAN
);