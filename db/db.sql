-- Drop tables
DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS authors;

-- Create the tables

CREATE TABLE authors(
    id SERIAL PRIMARY KEY NOT NULL,
    first_name VARCHAR(64),
    last_name VARCHAR(64)
);

CREATE TABLE books(
    id SERIAL PRIMARY KEY NOT NULL,
    title VARCHAR(128),
    release_date VARCHAR(10),
    author_id INT REFERENCES authors(id) NOT NULL
);