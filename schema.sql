CREATE TABLE Data (
  entry_id serial PRIMARY KEY,
  user_id integer,
  question_id integer,
  response integer,
  created_at timestamp DEFAULT CURRENT_TIMESTAMP
);

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
  question_type varchar
);


ALTER TABLE Data ADD FOREIGN KEY (user_id) REFERENCES Users (id);
ALTER TABLE Data ADD FOREIGN KEY (question_id) REFERENCES Questions (question_id);




INSERT INTO questions (question_text) VALUES ('How would you rate your motivation level yesterday?');
INSERT INTO questions (question_text) VALUES ('How would you rate your physical fatigue yesterday?');
INSERT INTO questions (question_text) VALUES ('How would you rate your muscle soreness yesterday?');
INSERT INTO questions (question_text) VALUES ('How would you rate your sleep quality yesterday?');
INSERT INTO questions (question_text) VALUES ('How would you rate your stress level yesterday?');
INSERT INTO questions (question_text) VALUES ('How would you rate your diet quality yesterday?');
INSERT INTO questions (question_text) VALUES ('How would you rate your performance in yesterdays training or game?');

