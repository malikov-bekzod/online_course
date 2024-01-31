import sys 
sys.path.append("../")
from connection import connection_db

cursor = connection_db.cursor()

def create_tables():

    cursor.execute("""CREATE TABLE language(
                   language_id SERIAL PRIMARY KEY NOT NULL,
                   name VARCHAR(20) NOT NULL,
                   last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW()
    )""")


    cursor.execute("""CREATE TABLE mentor(
                   mentor_id SERIAL PRIMARY KEY NOT NULL,
                   first_name VARCHAR(20) NOT NULL,
                   last_name VARCHAR(20) NOT NULL,
                   phone VARCHAR(20) NOT NULL,
                   email VARCHAR(50) NOT NULL,
                   bio TEXT,
                   last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW()
    )""")



    cursor.execute("""CREATE TABLE teacher(
                   teacher_id SERIAL PRIMARY KEY NOT NULL,
                   first_name VARCHAR(20) NOT NULL,
                   last_name VARCHAR(20) NOT NULL,
                   bio TEXT,
                   last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW()
    )""")


    cursor.execute("""CREATE TABLE customer(
                   customer_id SERIAL PRIMARY KEY NOT NULL,
                   first_name VARCHAR(20) NOT NULL,
                   last_name VARCHAR(20) NOT NULL,
                   phone VARCHAR(20) NOT NULL,
                   email VARCHAR(50) NOT NULL,
                   username VARCHAR(20) NOT NULL,
                   password VARCHAR(20) NOT NULL,
                   last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW()
    )""")



    cursor.execute("""CREATE TABLE category(
                   category_id SERIAL PRIMARY KEY NOT NULL,
                   name VARCHAR(60) NOT NULL,
                   description VARCHAR(180) NOT NULL,
                   last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW()
    )""")


    cursor.execute("""CREATE TABLE course(
                   course_id SERIAL PRIMARY KEY NOT NULL,
                   title VARCHAR(60) NOT NULL,
                   description TEXT,
                   duration VARCHAR(60) NOT NULL,
                   rating INT,
                   customer_count INT NOT NULL,
                   price NUMERIC(10,2) NOT NULL,
                   language_id INT NOT NULL REFERENCES language(language_id),
                   last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW()
    )""")




    cursor.execute("""CREATE TABLE course_category(
                   course_id INT REFERENCES course(course_id),
                   category_id INT REFERENCES category(category_id),
                   last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW()
    )""")



    cursor.execute("""CREATE TABLE course_mentor(
                   course_id INT REFERENCES course(course_id),
                   mentor_id INT REFERENCES mentor(mentor_id),
                   last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW()
    )""")


    cursor.execute("""CREATE TABLE course_teacher(
                   course_id INT REFERENCES course(course_id),
                   teacher_id INT REFERENCES teacher(teacher_id),
                   last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW()
    )""")


    cursor.execute("""CREATE TABLE lesson(
                   lesson_id SERIAL PRIMARY KEY NOT NULL,
                   course_id INT REFERENCES course(course_id),
                   title VARCHAR(60) NOT NULL,
                   content TEXT NOT NULL,
                   last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW()
    )""")



    cursor.execute("""CREATE TABLE exam(
                   exam_id SERIAL PRIMARY KEY NOT NULL,
                   title VARCHAR(60) NOT NULL,
                   description TEXT NOT NULL,
                   course_id INT REFERENCES course(course_id),
                   last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW()
    )""")



    cursor.execute("""CREATE TABLE question(
                   question_id SERIAL PRIMARY KEY NOT NULL,
                   exam_id INT NOT NULL REFERENCES exam(exam_id),
                   text TEXT NOT NULL,
                   answer TEXT NOT NULL,
                   explanation TEXT NOT NULL,
                   last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW()
    )""")




    cursor.execute("""CREATE TABLE enrollment(
                   enrollment_id SERIAL PRIMARY KEY NOT NULL,
                   customer_id INT NOT NULL REFERENCES customer(customer_id),
                   course_id INT NOT NULL REFERENCES course(course_id),
                   enrollment_date DATE NOT NULL,
                   last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW()
    )""")



    cursor.execute("""CREATE TABLE payment(
                   payment_id SERIAL PRIMARY KEY NOT NULL,
                   enrollment_id INT NOT NULL REFERENCES enrollment(enrollment_id),
                   amount NUMERIC(10,2) NOT NULL,
                   payment_date DATE NOT NULL,
                   customer_id INT NOT NULL REFERENCES customer(customer_id),
                   last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT NOW()
    )""")


    connection_db.commit()
    print("CREATE TABLE")

