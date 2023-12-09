
INSERT INTO Tips (tip_text, category) VALUES
('Try setting small, achievable goals to boost your motivation.', 'motivation'),
('Ensure you are getting enough rest and recovery time between workouts.', 'recovery'),
('Consider gentle stretching or a warm bath to alleviate muscle soreness.', 'recovery'),
('Establish a calming bedtime routine to improve your sleep quality.', 'sleep'),
('Try mindfulness or breathing exercises to reduce stress.', 'mental health'),
('Incorporate more whole foods like fruits, vegetables, and lean proteins into your diet.', 'nutrition'),
('Review your training plan to ensure it aligns with your performance goals.', 'training'),
('Listen to your body and adjust training intensity based on your RPE.', 'training'),
('If injured, give your body time to heal and consider consulting a healthcare professional.', 'health');

INSERT INTO Questions (question_text, question_type, radio_low, radio_high, radio_scale, question_title, category) 
VALUES 
  ('How would you rate your motivation level today?', 'radio', 'Low', 'High', 5, 'Motivation', 'motivation'),
  ('How would you rate your physical fatigue today?', 'radio', 'Low', 'High', 5, 'Fatigue', 'recovery'),
  ('How would you rate your muscle soreness today?', 'radio', 'Low', 'High', 5, 'Soreness', 'recovery'),
  ('How would you rate your sleep quality today?', 'radio', 'Bad', 'Good', 5, 'Sleep quality', 'sleep'),
  ('How would you rate your stress level today?', 'radio', 'Low', 'High', 5, 'Stress level', 'mental health'),
  ('How would you rate your diet quality today?', 'radio', 'Junk', 'Great', 5, 'Diet quality', 'nutrition'),
  ('How would you rate your performance in todays training or game?', 'radio', 'Poor', 'Excellent', 10, 'Performance', 'training'),
  ('RPE for todays training:', 'radio', null, null, 10, 'RPE', null),
  ('Are you injured?', 'radio', 'No', 'Yes', 2, 'Injured', 'health'),
  ('Is it the first day of your menstrual cycle?', 'radio', 'No', 'Yes', 2, 'Menstrual cycle day 1', 'menstrual health');

INSERT INTO Data (user_id, question_id, response, created_at)
VALUES 
  (1, 1, 3, '2023-11-15 12:00:00'),
  (1, 2, 2, '2023-11-15 12:00:00'),
  (1, 3, 3, '2023-11-15 12:00:00'),
  (1, 4, 4, '2023-11-15 12:00:00'),
  (1, 5, 5, '2023-11-15 12:00:00'),
  (1, 6, 4, '2023-11-15 12:00:00'),
  (1, 7, 5, '2023-11-15 12:00:00'),
  (1, 8, 6, '2023-11-15 12:00:00'),
  (1, 9, 1, '2023-11-15 12:00:00'),
  (1, 10, 1,'2023-11-15 12:00:00'),
  (1, 1, 2, '2023-11-16 12:00:00'),
  (1, 2, 3, '2023-11-16 12:00:00'),
  (1, 3, 2, '2023-11-16 12:00:00'),
  (1, 4, 4, '2023-11-16 12:00:00'),
  (1, 5, 5, '2023-11-16 12:00:00'),
  (1, 6, 5, '2023-11-16 12:00:00'),
  (1, 7, 4, '2023-11-16 12:00:00'),
  (1, 8, 8, '2023-11-16 12:00:00'),
  (1, 9, 1, '2023-11-16 12:00:00'),
  (1, 10, 1,'2023-11-16 12:00:00'),
  (1, 1, 4, '2023-11-17 12:00:00'),
  (1, 2, 4, '2023-11-17 12:00:00'),
  (1, 3, 4, '2023-11-17 12:00:00'),
  (1, 4, 5, '2023-11-17 12:00:00'),
  (1, 5, 3, '2023-11-17 12:00:00'),
  (1, 6, 2, '2023-11-17 12:00:00'),
  (1, 7, 3, '2023-11-17 12:00:00'),
  (1, 8, 2, '2023-11-17 12:00:00'),
  (1, 9, 1, '2023-11-17 12:00:00'),
  (1, 10, 2,'2023-11-17 12:00:00'),
  (1, 1, 5, '2023-11-19 12:00:00'),
  (1, 2, 2, '2023-11-19 12:00:00'),
  (1, 3, 1, '2023-11-19 12:00:00'),
  (1, 4, 2, '2023-11-19 12:00:00'),
  (1, 5, 3, '2023-11-19 12:00:00'),
  (1, 6, 4, '2023-11-19 12:00:00'),
  (1, 7, 4, '2023-11-19 12:00:00'),
  (1, 8, 6, '2023-11-19 12:00:00'),
  (1, 9, 1, '2023-11-19 12:00:00'),
  (1, 10, 1,'2023-11-19 12:00:00'),
  (1, 1, 2, '2023-11-23 12:00:00'),
  (1, 2, 3, '2023-11-23 12:00:00'),
  (1, 3, 2, '2023-11-23 12:00:00'),
  (1, 4, 4, '2023-11-23 12:00:00'),
  (1, 5, 5, '2023-11-23 12:00:00'),
  (1, 6, 5, '2023-11-23 12:00:00'),
  (1, 7, 4, '2023-11-23 12:00:00'),
  (1, 8, 8, '2023-11-23 12:00:00'),
  (1, 9, 1, '2023-11-23 12:00:00'),
  (1, 10, 1,'2023-11-23 12:00:00'),
  (1, 1, 4, '2023-12-01 12:00:00'),
  (1, 2, 4, '2023-12-01 12:00:00'),
  (1, 3, 4, '2023-12-01 12:00:00'),
  (1, 4, 5, '2023-12-01 12:00:00'),
  (1, 5, 3, '2023-12-01 12:00:00'),
  (1, 6, 2, '2023-12-01 12:00:00'),
  (1, 7, 3, '2023-12-01 12:00:00'),
  (1, 8, 2, '2023-12-01 12:00:00'),
  (1, 9, 1, '2023-12-01 12:00:00'),
  (1, 10, 2,'2023-12-01 12:00:00');
  