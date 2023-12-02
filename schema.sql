CREATE TABLE Users (
  id serial PRIMARY KEY,
  username varchar(255) UNIQUE,
  password varchar(128),
  admin boolean,
  created_at timestamp DEFAULT CURRENT_TIMESTAMP,
  full_name varchar,
  sport varchar,
  team varchar,
  last_menstrual_date date,
  poll_updated_at date
);

CREATE TABLE Questions (
  question_id serial PRIMARY KEY,
  question_text text,
  question_type varchar,
  radio_low text,
  radio_high text,
  radio_scale integer,
  question_title text UNIQUE
);

CREATE TABLE Data (
  entry_id serial PRIMARY KEY,
  user_id integer REFERENCES Users (id),
  question_id integer REFERENCES Questions (question_id),
  response integer,
  created_at timestamp DEFAULT CURRENT_TIMESTAMP
);
