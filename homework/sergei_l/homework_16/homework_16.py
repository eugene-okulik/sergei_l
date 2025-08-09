import os
import csv
import dotenv
import mysql.connector as mysql


def fetch_file():
    base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    file_path = os.path.join(base_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')

    with open(file_path, newline='') as file:
        file_data = csv.DictReader(file)
        for row in file_data:
            yield row


def fetch_db():
    dotenv.load_dotenv()

    db = mysql.connect(
        user=os.getenv('DB_USER'),
        passwd=os.getenv('DB_PASSW'),
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT'),
        database=os.getenv('DB_NAME')
    )

    cursor = db.cursor(dictionary=True)

    cursor.execute(
        '''
        SELECT s.name, s.second_name, g.title AS group_title,
        b.title AS book_title, sub.title AS subject_title, l.title AS lesson_title, m.`value` AS mark_value
        FROM students as s
        JOIN `groups` AS g ON s.group_id = g.id
        JOIN books AS b ON s.id = b.taken_by_student_id
        JOIN marks AS m ON s.id = m.student_id
        JOIN lessons AS l ON m.lesson_id = l.id
        JOIN subjects AS sub ON l.subject_id = sub.id
        '''
    )

    for row in cursor.fetchall():
        yield row

    db.close()


for line_file in fetch_file():
    is_found = False
    for line_db in fetch_db():
        if line_file == line_db:
            is_found = True
            break
    if not is_found:
        print(f'В БД остутствует: {line_file}')
