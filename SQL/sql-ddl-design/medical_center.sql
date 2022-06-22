DROP DATABASE IF EXISTS medical_center_db;

CREATE DATABASE medical_center_db;

\c medical_center_db

CREATE TABLE doctor (
  id SERIAL PRIMARY KEY,
  name text NOT NULL,
  ph_number varchar(10)
);

CREATE TABLE patient (
  id SERIAL PRIMARY KEY,
  name text NOT NULL,
  ph_number varchar(10)
);

CREATE TABLE disease (
  id SERIAL PRIMARY KEY,
  disease_name text NOT NULL
);

CREATE TABLE visit (
  id SERIAL PRIMARY KEY,
  doctor_id integer,
  patient_id integer,
  visit_date date
);

CREATE TABLE diagnosis (
  id SERIAL PRIMARY KEY,
  visit_id integer,
  disease_id integer
);

ALTER TABLE visit ADD FOREIGN KEY ("doctor_id") REFERENCES "doctor" ("id");

ALTER TABLE visit ADD FOREIGN KEY ("patient_id") REFERENCES "patient" ("id");

ALTER TABLE diagnosis ADD FOREIGN KEY ("visit_id") REFERENCES "visit" ("id");

ALTER TABLE diagnosis ADD FOREIGN KEY ("disease_id") REFERENCES "disease" ("id");
