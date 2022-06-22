DROP DATABASE IF EXISTS craigslist_db;

CREATE DATABASE craigslist_db;

\c craigslist_db

CREATE TABLE region
(
    id SERIAL PRIMARY KEY,
    name TEXT,
);

CREATE TABLE user
(
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    prefered_region INTEGER REFERENCES region
);

CREATE TABLE category
(
    id SERIAL PRIMARY KEY,
    category_name TEXT NOT NULL,

);

CREATE TABLE post
(
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    text TEXT NOT NULL,
    posted_by_user INTEGER NOT NULL REFERENCES user,
    location TEXT,
    post_region TEXT REFERENCES region
);

CREATE TABLE post_category
(
    id SERIAL PRIMARY KEY,
    post_id INTEGER REFERENCES post,
    category_id INTEGER REFERENCES category
);