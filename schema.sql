CREATE TABLE Users (
  id serial PRIMARY KEY,
  username varchar(255) UNIQUE,
  password varchar(128),
  admin boolean,
  created_at timestamp DEFAULT CURRENT_TIMESTAMP,
  full_name varchar,
  sport varchar,
  team varchar,
  poll_updated_at date
);
CREATE TABLE Questions (
  question_id serial PRIMARY KEY,
  question_text text,
  question_type varchar,
  radio_low text,
  radio_high text,
  radio_scale integer,
  question_title text UNIQUE,
  category varchar
);
CREATE TABLE Data (
  entry_id serial PRIMARY KEY,
  user_id integer REFERENCES Users (id),
  question_id integer REFERENCES Questions (question_id),
  response integer,
  created_at timestamp DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE Tips (
  tip_id serial PRIMARY KEY,
  tip_text text,
  category varchar
);
CREATE TABLE UserTips (
  user_id integer REFERENCES Users (id),
  tip_id integer REFERENCES Tips (tip_id),
  last_shown timestamp,
  shown_count integer DEFAULT 0,
  PRIMARY KEY (user_id, tip_id)
);