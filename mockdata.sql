
INSERT INTO Tips (tip_text, category) VALUES
('Try setting small, achievable goals to boost your motivation.', 'motivation'),
('Ensure you are getting enough rest and recovery time between workouts.', 'recovery'),
('Consider gentle stretching or a warm bath to alleviate muscle soreness.', 'recovery'),
('Establish a calming bedtime routine to improve your sleep quality.', 'sleep'),
('Try mindfulness or breathing exercises to reduce stress.', 'mental health'),
('Incorporate more whole foods like fruits, vegetables, and lean proteins into your diet.', 'nutrition'),
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
  ('RPE for todays training:', 'radio', 'Light', 'Heavy', 10, 'RPE', null),
  ('Are you injured?', 'radio', 'No', 'Yes', 2, 'Injured', 'health'),
  ('Is it the first day of your menstrual cycle?', 'radio', 'No', 'Yes', 2, 'Menstrual cycle day 1', 'menstrual health');