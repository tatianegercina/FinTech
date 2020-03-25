-- Query Tables
SELECT * FROM agents;
SELECT * FROM regions;
SELECT * FROM agent_region_junction;

-- A join statement to query all courses taken by students
SELECT s.id, s.last_name, s.first_name, c.id, c.course_name, j.course_term
FROM agents a
LEFT JOIN student_courses_junction b ON s.id = j.student_id
LEFT JOIN courses c ON c.id = j.course_id;





