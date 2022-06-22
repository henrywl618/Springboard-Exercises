DROP DATABASE IF EXISTS soccer_league_db;
CREATE DATABASE soccer_league_db;
\c soccer_league_db

CREATE TABLE team
(
    id SERIAL PRIMARY KEY,
    team_name TEXT NOT NULL,
    standing INTEGER
);

CREATE TABLE goal
(
    id SERIAL PRIMARY KEY,
    match_id INTEGER REFERENCES match,
    player_id INTEGER REFERENCES player,
    team_id INTEGER REFERENCES team,
    score_time TIMESTAMP
);

CREATE TABLE player
(
    id SERIAL PRIMARY KEY,
    player_name TEXT,
    team_id INTEGER REFERENCES team
);

CREATE TABLE referee
(
    id SERIAL PRIMARY KEY,
    ref_name TEXT NOT NULL
);

CREATE TABLE match
(
    id SERIAL PRIMARY KEY,
    match_date DATE,
    team1_id INTEGER REFERENCES team,
    team2_id INTEGER REFERENCES team,
);

CREATE TABLE match_referees
(
    id SERIAL PRIMARY KEY,
    match_id INTEGER REFERENCES match,
    referee_id INTEGER REFERENCES referee
);

CREATE TABLE season
(
    id SERIAL PRIMARY KEY,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL
);

