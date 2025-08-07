import mysql.connector as mysql


db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor()

cursor.execute("INSERT INTO students (name, second_name) VALUES ('Sergei', 'Sergeev')")
student_id = cursor.lastrowid

create_books_query = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
create_books_values = [
    ('Python Advanced', student_id),
    ('Fullstack QAs Advanced', student_id)
]
cursor.executemany(create_books_query, create_books_values)

cursor.execute(
    "INSERT INTO `groups` (title, start_date, end_date) VALUES ('Automation QAs Advanced', 'Aug 2025', 'Feb 2026')"
)
group_id = cursor.lastrowid

add_group_query = "UPDATE students SET group_id = %s WHERE id = %s"
add_group_values = (group_id, student_id)
cursor.execute(add_group_query, add_group_values)

create_subject_query = "INSERT INTO subjects (title) VALUES (%s)"
create_subject_values = [
    ('Python Advanced', ),
    ('QA Theory Advanced', )
]
cursor.execute(create_subject_query, create_subject_values[0])
subject1_id = cursor.lastrowid
cursor.execute(create_subject_query, create_subject_values[1])
subject2_id = cursor.lastrowid

create_lesson_query = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
create_lesson_values = [
    ('Loops Advanced', subject1_id),
    ('OOP Advanced', subject1_id),
    ('Test design Advanced', subject2_id),
    ('Test documentation Advanced', subject2_id)
]
cursor.execute(create_lesson_query, create_lesson_values[0])
lesson_id1 = cursor.lastrowid
cursor.execute(create_lesson_query, create_lesson_values[1])
lesson_id2 = cursor.lastrowid
cursor.execute(create_lesson_query, create_lesson_values[2])
lesson_id3 = cursor.lastrowid
cursor.execute(create_lesson_query, create_lesson_values[3])
lesson_id4 = cursor.lastrowid

create_mark_query = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
create_mark_values = [
    (5, lesson_id1, student_id),
    (6, lesson_id2, student_id),
    (6, lesson_id3, student_id),
    (7, lesson_id4, student_id)
]
cursor.executemany(create_mark_query, create_mark_values)

db.commit()

student_id_value = [student_id]
cursor.execute(
    '''
    SELECT value FROM marks
    JOIN students ON marks.student_id = students.id
    WHERE students.id = %s
    ''', student_id_value
)
get_student_marks = cursor.fetchall()
print(get_student_marks)

cursor.execute(
    '''
    SELECT title FROM books
    JOIN students ON books.taken_by_student_id = students.id
    WHERE students.id = %s
    ''', student_id_value
)
get_student_books = cursor.fetchall()
print(get_student_books)

cursor.execute(
    '''
    SELECT s.name, s.second_name, b.title, g.title, m.`value`, l.title, sub.title
    FROM students AS s
    JOIN books AS b ON s.id = b.taken_by_student_id
    JOIN `groups` AS g ON s.group_id = g.id
    JOIN marks AS m ON s.id = m.student_id
    JOIN lessons AS l ON m.lesson_id = l.id
    JOIN subjects AS sub ON l.subject_id = sub.id
    WHERE s.id = %s
''', student_id_value
)
get_all_student_data = cursor.fetchall()
print(get_all_student_data)

db.close()
