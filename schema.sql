CREATE TABLE Users (
  id serial PRIMARY KEY,
  username varchar(255) UNIQUE,
  password varchar(128),
  admin boolean,
  created_at timestamp DEFAULT CURRENT_TIMESTAMP,
  full_name varchar,
  sport varchar,
  team varchar,
  menstrual_cycle integer,
  last_menstrual_date date
);

CREATE TABLE Questions (
  question_id serial PRIMARY KEY,
  question_text text,
  question_type varchar,
  radio_low text,
  radio_high text,
  radio_scale integer
);

CREATE TABLE Data (
  entry_id serial PRIMARY KEY,
  user_id integer REFERENCES Users (id),
  question_id integer REFERENCES Questions (question_id),
  response integer,
  created_at timestamp DEFAULT CURRENT_TIMESTAMP
);


INSERT INTO Questions (question_text, question_type, radio_low, radio_high, radio_scale) 
VALUES ('How would you rate your motivation level today?', 'radio', 'Low', 'High', 5);

INSERT INTO Questions (question_text, question_type, radio_low, radio_high, radio_scale) 
VALUES ('How would you rate your physical fatigue today?', 'radio', 'Low', 'High', 5);

INSERT INTO Questions (question_text, question_type, radio_low, radio_high, radio_scale) 
VALUES ('How would you rate your muscle soreness today?', 'radio', 'Low', 'High', 5);

INSERT INTO Questions (question_text, question_type, radio_low, radio_high, radio_scale) 
VALUES ('How would you rate your sleep quality today?', 'radio', 'Bad', 'Good', 5);

INSERT INTO Questions (question_text, question_type, radio_low, radio_high, radio_scale) 
VALUES ('How would you rate your stress level today?', 'radio', 'Low', 'High', 5);

INSERT INTO Questions (question_text, question_type, radio_low, radio_high, radio_scale) 
VALUES ('How would you rate your diet quality today?', 'radio', 'Junk', 'Great', 5);

INSERT INTO Questions (question_text, question_type, radio_low, radio_high, radio_scale) 
VALUES ('How would you rate your performance in todays training or game?', 'radio', 'Poor', 'Excellent', 10);

INSERT INTO Questions (question_text, question_type, radio_low, radio_high, radio_scale) 
VALUES ('Are you injured?', 'radio', 'No', 'Yes', 2);

