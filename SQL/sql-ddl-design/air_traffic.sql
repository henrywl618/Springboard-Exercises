-- from the terminal run:
-- psql < air_traffic.sql

DROP DATABASE IF EXISTS air_traffic;

CREATE DATABASE air_traffic;

\c air_traffic


CREATE TABLE tickets
(
  id SERIAL PRIMARY KEY,
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  seat TEXT NOT NULL,
  departure TIMESTAMP NOT NULL,
  arrival TIMESTAMP NOT NULL,
  airline INTEGER NOT NULL,
  from_city INTEGER NOT NULL,
  from_country INTEGER NOT NULL,
  to_city INTEGER NOT NULL,
  to_country INTEGER NOT NULL
);

CREATE TABLE airline
(
  id SERIAL PRIMARY KEY,
  airline_name TEXT NOT NULL
);

CREATE TABLE city
(
  id SERIAL PRIMARY KEY,
  city_name TEXT UNIQUE NOT NULL
);

CREATE TABLE country
(
  id SERIAL PRIMARY KEY,
  country_name TEXT UNIQUE NOT NULL
);

INSERT INTO tickets
  (first_name, last_name, seat, departure, arrival, airline, from_city, from_country, to_city, to_country)
VALUES
  ('Jennifer', 'Finch', '33B', '2018-04-08 09:00:00', '2018-04-08 12:00:00', 1, 1, 1, 4, 1),
  ('Thadeus', 'Gathercoal', '8A', '2018-12-19 12:45:00', '2018-12-19 16:15:00', 7, 2, 9, 11, 3),
  ('Sonja', 'Pauley', '12F', '2018-01-02 07:00:00', '2018-01-02 08:03:00', 2, 3, 1, 12, 1),
  ('Jennifer', 'Finch', '20A', '2018-04-15 16:50:00', '2018-04-15 21:00:00', 2, 4, 1, 13, 6),
  ('Waneta', 'Skeleton', '23D', '2018-08-01 18:30:00', '2018-08-01 21:50:00', 5, 5, 8, 14, 5),
  ('Thadeus', 'Gathercoal', '18C', '2018-10-31 01:15:00', '2018-10-31 12:55:00', 4, 6, 7, 15, 2),
  ('Berkie', 'Wycliff', '9E', '2019-02-06 06:00:00', '2019-02-06 07:47:00', 1, 7, 1, 9, 1),
  ('Alvin', 'Leathes', '1A', '2018-12-22 14:42:00', '2018-12-22 15:56:00', 6, 8, 1, 16, 1),
  ('Berkie', 'Wycliff', '32B', '2019-02-06 16:28:00', '2019-02-06 19:18:00', 6, 9, 1, 17, 1),
  ('Cory', 'Squibbes', '10D', '2019-01-20 19:30:00', '2019-01-20 22:45:00', 3, 10, 10, 18, 4);
  
INSERT INTO airline
  (airline_name)
VALUES
 ('United'),
 ('Delta'),
 ('Avianca Brasil'),
 ('Air China'),
 ('TUI Fly Belgium'),
 ('American Airlines'),
 ('British Airways');

INSERT INTO city
  (city_name)
VALUES  
   ('Washington DC'),
   ('Tokyo'),
   ('Los Angeles'),
   ('Seattle'),
   ('Paris'),
   ('Dubai'),
   ('New York'),
   ('Cedar Rapids'),
   ('Charlotte'),
   ('Sao Paolo'),
   ('London'),
   ('Las Vegas'),
   ('Mexico City'),
   ('Casablanca'),
   ('Beijing'),
   ('Chicago'),
   ('New Orleans'),
   ('Santiago');

INSERT INTO country
  (country_name)
VALUES
  ('United States'),
  ('China'),
  ('United Kingdom'),
  ('Chile'),
  ('Morocco'),
  ('Mexico'),
  ('UAE'),
  ('France'),
  ('Japan'),
  ('Brazil');

ALTER TABLE tickets ADD CONSTRAINT fk_airline FOREIGN KEY (airline) REFERENCES airline;
ALTER TABLE tickets ADD CONSTRAINT fk_fromcity FOREIGN KEY (from_city) REFERENCES city;
ALTER TABLE tickets ADD CONSTRAINT fk_tocity FOREIGN KEY (to_city) REFERENCES city;
ALTER TABLE tickets ADD CONSTRAINT fk_fromcountry FOREIGN KEY (from_country) REFERENCES country;
ALTER TABLE tickets ADD CONSTRAINT fk_tocountry FOREIGN KEY (to_country) REFERENCES country;