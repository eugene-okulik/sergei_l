INSERT INTO students (name, second_name) VALUES ('Ivan', 'Ivanov');
INSERT INTO books (title, taken_by_student_id) VALUES ('Python basics', 20892);
INSERT INTO books (title, taken_by_student_id) VALUES ('Fullstack QAs', 20892);
INSERT INTO `groups` (title, start_date, end_date) VALUES ('Automation QAs', 'Jun 2025', 'Jan 2026');
UPDATE students SET group_id = 5484 WHERE id = 20892;
INSERT INTO subjects (title) VALUES ('Python');
INSERT INTO subjects (title) VALUES ('QA theory');
INSERT INTO lessons (title, subject_id) VALUES ('Loops', 11618);
INSERT INTO lessons (title, subject_id) VALUES ('OOP', 11618);
INSERT INTO lessons (title, subject_id) VALUES ('Test design methods', 11619);
INSERT INTO lessons (title, subject_id) VALUES ('Test documentation', 11619);
INSERT INTO marks (value, lesson_id, student_id) VALUES (7, 11668, 20892);
INSERT INTO marks (value, lesson_id, student_id) VALUES (6, 11669, 20892);
INSERT INTO marks (value, lesson_id, student_id) VALUES (7, 11670, 20892);
INSERT INTO marks (value, lesson_id, student_id) VALUES (8, 11671, 20892);
SELECT value FROM marks JOIN students ON marks.student_id = students.id WHERE students.id = 20892;
SELECT title FROM books JOIN students ON books.taken_by_student_id = students.id WHERE students.id = 20892;

SELECT s.name, s.second_name, b.title, g.title, m.`value`, l.title, sub.title
FROM students AS s
JOIN books AS b ON s.id = b.taken_by_student_id 
JOIN `groups` AS g ON s.group_id = g.id 
JOIN marks AS m ON s.id = m.student_id
JOIN lessons AS l ON m.lesson_id = l.id
JOIN subjects AS sub ON l.subject_id = sub.id
WHERE s.id = 20892;
