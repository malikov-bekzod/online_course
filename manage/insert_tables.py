import sys 
sys.path.append("../")
from connection import connection_db

cursor = connection_db.cursor()

def insert_tables():
    
    languages = ["uzbek","russian","english","portuges","french","japanese","chinese"]
    for i in languages:
        cursor.execute(f"INSERT INTO language(name) VALUES('{i}')")


    query_to_insert_mentors = """
    INSERT INTO mentor (first_name, last_name, phone, email, bio)
    VALUES
        ('John', 'Doe', '1234567890', 'john.doe@example.com', 'Experienced mentor specializing in software development.'),
        ('Jane', 'Smith', '9876543210', 'jane.smith@example.com', 'Passionate mentor with expertise in data analysis.'),
        ('Michael', 'Johnson', '5551234567', 'michael.johnson@example.com', 'Seasoned mentor offering guidance in project management.'),
        ('Emily', 'Brown', '8885551234', 'emily.brown@example.com', 'Knowledgeable mentor focusing on web design and development.'),
        ('David', 'Wilson', '7778889999', 'david.wilson@example.com', 'Experienced mentor specializing in database administration.'),
        ('Sarah', 'Anderson', '4443332222', 'sarah.anderson@example.com', 'Skilled mentor with expertise in cybersecurity.'),
        ('Robert', 'Taylor', '2224446666', 'robert.taylor@example.com', 'Passionate mentor offering guidance in machine learning.'),
        ('Jennifer', 'Lee', '9990001111', 'jennifer.lee@example.com', 'Knowledgeable mentor focusing on mobile app development.'),
        ('Christopher', 'Martinez', '1112223333', 'christopher.martinez@example.com', 'Experienced mentor specializing in cloud computing.'),
        ('Laura', 'Harris', '6667778888', 'laura.harris@example.com', 'Seasoned mentor offering guidance in software testing.');"""
    cursor.execute(query_to_insert_mentors)

    
    query_for_insert_teahcer = """INSERT INTO teacher (first_name, last_name, bio)
VALUES
    ('Robert', 'Smith', 'Experienced teacher specializing in mathematics.'),
    ('Emily', 'Johnson', 'Passionate teacher with expertise in science.'),
    ('Michael', 'Williams', 'Seasoned teacher offering guidance in history.'),
    ('Sophia', 'Brown', 'Knowledgeable teacher focusing on literature.'),
    ('David', 'Jones', 'Experienced teacher specializing in computer science.'),
    ('Olivia', 'Anderson', 'Skilled teacher with expertise in foreign languages.'),
    ('Ethan', 'Taylor', 'Passionate teacher offering guidance in music.'),
    ('Isabella', 'Lee', 'Knowledgeable teacher focusing on art.'),
    ('Daniel', 'Martinez', 'Experienced teacher specializing in physical education.'),
    ('Ava', 'Harris', 'Seasoned teacher offering guidance in geography.');"""
    cursor.execute(query_for_insert_teahcer)


    query_for_customer = """INSERT INTO customer (first_name, last_name, phone, email, username, password)
VALUES
    ('Emma', 'Johnson', '1234567890', 'emma.johnson@example.com', 'emma123', 'password123'),
    ('Liam', 'Smith', '9876543210', 'liam.smith@example.com', 'liam456', 'password456'),
    ('Olivia', 'Anderson', '5551234567', 'olivia.anderson@example.com', 'olivia789', 'password789'),
    ('Noah', 'Brown', '8885551234', 'noah.brown@example.com', 'noah012', 'password012'),
    ('Ava', 'Williams', '7778889999', 'ava.williams@example.com', 'ava345', 'password345'),
    ('Sophia', 'Davis', '4443332222', 'sophia.davis@example.com', 'sophia678', 'password678'),
    ('Jackson', 'Wilson', '2224446666', 'jackson.wilson@example.com', 'jackson901', 'password901'),
    ('Isabella', 'Lee', '9990001111', 'isabella.lee@example.com', 'isabella234', 'password234'),
    ('Lucas', 'Garcia', '1112223333', 'lucas.garcia@example.com', 'lucas567', 'password567'),
    ('Mia', 'Rodriguez', '6667778888', 'mia.rodriguez@example.com', 'mia890', 'password890');"""

    cursor.execute(query_for_customer)
    

    query_for_the_category = """INSERT INTO category (name, description)
VALUES
    ('Programming', 'Courses related to programming languages and software development.'),
    ('Database', 'Courses focused on database management and administration.'),
    ('Network', 'Courses covering computer networks and network security.'),
    ('Web Development', 'Courses for web development technologies and frameworks.'),
    ('Data Science', 'Courses on data analysis, data visualization, and machine learning.'),
    ('Cybersecurity', 'Courses specializing in cybersecurity and ethical hacking.'),
    ('Cloud Computing', 'Courses related to cloud platforms and infrastructure.'),
    ('Mobile App Development', 'Courses focusing on mobile application development.'),
    ('Artificial Intelligence', 'Courses exploring artificial intelligence and its applications.'),
    ('Software Testing', 'Courses covering software testing methodologies and techniques.');"""
    cursor.execute(query_for_the_category)


    qury_for_course = """INSERT INTO course (title, description, duration, rating, customer_count, price, language_id)
VALUES
    ('Introduction to Python', 'Learn the basics of Python programming language.', '05:30:00', 8, 1000, 250000, 1),
    ('Database Management Fundamentals', 'Master the fundamentals of database management.', '03:15:00', 7, 800, 150000, 2),
    ('Network Security Essentials', 'Learn essential concepts of network security.', '04:00:00', 9, 1200, 200000, 3),
    ('Web Development with HTML and CSS', 'Build responsive websites using HTML and CSS.', '06:45:00', 8, 1500, 300000, 4),
    ('Data Analysis with Python', 'Learn data analysis techniques using Python.', '07:30:00', 9, 1800, 350000, 1),
    ('Ethical Hacking and Penetration Testing', 'Master the skills of ethical hacking and penetration testing.', '09:30:00', 9, 2000, 400000, 3),
    ('Cloud Computing Fundamentals', 'Get started with the basics of cloud computing.', '03:45:00', 7, 900, 180000, 5),
    ('Mobile App Development with React Native', 'Build mobile apps using React Native framework.', '08:15:00', 8, 1600, 320000, 4),
    ('Introduction to Artificial Intelligence', 'Explore the foundations of artificial intelligence.', '04:30:00', 7, 1000, 250000, 6),
    ('Software Testing Techniques and Best Practices', 'Master software testing techniques and best practices.', '06:00:00', 8, 1200, 280000, 7);"""
    cursor.execute(qury_for_course)



    query_for_course_categoru = """INSERT INTO course_category (course_id, category_id)
VALUES
    (1, 1),
    (1, 5),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 3),
    (8, 4),
    (9, 6);"""
    cursor.execute(query_for_course_categoru)
    

    query_for_course_mentor = """INSERT INTO course_mentor (course_id, mentor_id)
VALUES
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
    (10, 10);"""
    cursor.execute(query_for_course_mentor)
    

    query_for_course_teacher = """INSERT INTO course_teacher (course_id, teacher_id)
VALUES
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
    (10, 10);"""
    cursor.execute(query_for_course_teacher)
    
    query_for_lesson = """INSERT INTO lesson (course_id, title, content)
VALUES
    (1, 'Introduction to Python', 'Lesson content for Introduction to Python.'),
    (1, 'Data Types and Variables', 'Lesson content for Data Types and Variables.'),
    (2, 'Introduction to Databases', 'Lesson content for Introduction to Databases.'),
    (2, 'Relational Database Design', 'Lesson content for Relational Database Design.'),
    (3, 'Introduction to Network Security', 'Lesson content for Introduction to Network Security.'),
    (3, 'Firewalls and Intrusion Detection Systems', 'Lesson content for Firewalls and Intrusion Detection Systems.'),
    (4, 'HTML Fundamentals', 'Lesson content for HTML Fundamentals.'),
    (4, 'CSS Styling', 'Lesson content for CSS Styling.'),
    (5, 'Data Analysis Basics', 'Lesson content for Data Analysis Basics.'),
    (5, 'Data Visualization Techniques', 'Lesson content for Data Visualization Techniques.'),
    (6, 'Ethical Hacking Fundamentals', 'Lesson content for Ethical Hacking Fundamentals.'),
    (6, 'Penetration Testing Methodologies', 'Lesson content for Penetration Testing Methodologies.'),
    (7, 'Introduction to Cloud Computing', 'Lesson content for Introduction to Cloud Computing.'),
    (7, 'Cloud Infrastructure Management', 'Lesson content for Cloud Infrastructure Management.'),
    (8, 'React Native Basics', 'Lesson content for React Native Basics.'),
    (8, 'Building Mobile Apps with React Native', 'Lesson content for Building Mobile Apps with React Native.'),
    (9, 'Introduction to Artificial Intelligence', 'Lesson content for Introduction to Artificial Intelligence.'),
    (9, 'Machine Learning Algorithms', 'Lesson content for Machine Learning Algorithms.'),
    (10, 'Software Testing Fundamentals', 'Lesson content for Software Testing Fundamentals.'),
    (10, 'Test Automation Techniques', 'Lesson content for Test Automation Techniques.');"""
    cursor.execute(query_for_lesson)
    
    
    query_for_exam = """INSERT INTO exam (title, description, course_id)
VALUES
    ('Python Basics Exam', 'An exam to test your understanding of Python basics.', 1),
    ('Database Concepts Exam', 'An exam to assess your knowledge of database concepts.', 2),
    ('Network Security Exam', 'An exam to evaluate your understanding of network security principles.', 3),
    ('HTML and CSS Exam', 'An exam to test your proficiency in HTML and CSS.', 4),
    ('Data Analysis Exam', 'An exam to assess your skills in data analysis.', 5),
    ('Ethical Hacking Exam', 'An exam to evaluate your knowledge of ethical hacking techniques.', 6),
    ('Cloud Computing Exam', 'An exam to test your understanding of cloud computing concepts.', 7),
    ('Mobile App Development Exam', 'An exam to assess your skills in mobile app development.', 8),
    ('Artificial Intelligence Exam', 'An exam to evaluate your understanding of artificial intelligence concepts.', 9),
    ('Software Testing Exam', 'An exam to assess your knowledge of software testing methodologies.', 10);"""
    cursor.execute(query_for_exam)
    


    query_for_question = """INSERT INTO question (exam_id, text, answer, explanation)
VALUES
    (1, 'What is the output of the following code? print(2 + 2)', '4', 'The code will output 4 because the addition operation adds 2 and 2 together.'),
    (1, 'What is the correct way to declare a variable in Python?', 'b) x = 5', 'The correct way to declare a variable in Python is by using the format: variable_name = value.'),
    (2, 'What is a primary key in a relational database?', 'c) A unique identifier for a record in a table', 'A primary key is a column or a set of columns that uniquely identifies each record in a table.'),
    (2, 'What is the purpose of a foreign key?', 'a) To establish a relationship between two tables', 'A foreign key is used to establish a relationship between two tables in a relational database.'),
    (3, 'What is the purpose of a firewall?', 'b) To protect a network from unauthorized access', 'A firewall is a network security device that monitors and controls incoming and outgoing network traffic based on predetermined security rules.'),
    (3, 'What is an intrusion detection system (IDS)?', 'a) A security technology that monitors network traffic for suspicious activity', 'An intrusion detection system (IDS) is a security technology that monitors network traffic for suspicious activity and alerts the system administrator.'),
    (4, 'What is the correct HTML tag for creating a hyperlink?', 'a) <a>', 'The <a> tag is used to create a hyperlink in HTML.'),
    (4, 'What is the purpose of CSS?', 'c) To add styles and layout to web documents', 'CSS (Cascading Style Sheets) is used to add styles and layout to web documents.'),
    (5, 'What is data analysis?', 'b) The process of inspecting, cleaning, transforming, and modeling data', 'Data analysis is the process of inspecting, cleaning, transforming, and modeling data to discover useful information and draw conclusions.'),
    (5, 'What is data visualization?', 'a) The representation of data in graphical or pictorial format', 'Data visualization is the representation of data in graphical or pictorial format to facilitate understanding and analysis.'),
    (6, 'What is ethical hacking?', 'c) The authorized practice of probing computer systems for security vulnerabilities', 'Ethical hacking is the authorized practice of probing computer systems for security vulnerabilities in order to identify and fix them.'),
    (6, 'What is penetration testing?', 'b) The process of simulating an attack on a computer system to evaluate its security', 'Penetration testing is the process of simulating an attack on a computer system to evaluate its security and identify vulnerabilities.'),
    (7, 'What is cloud computing?', 'a) The delivery of computing services over the internet', 'Cloud computing is the delivery of computing services, such as servers, storage, databases, networking, software, and analytics, over the internet.'),
    (7, 'What is cloud infrastructure?', 'b) The underlying hardware and software components that enable cloud computing', 'Cloud infrastructure refers to the underlying hardware and software components that enable cloud computing services.'),
    (8, 'What is React Native?', 'c) A framework for building mobile apps using JavaScript and React', 'React Native is a framework for building mobile applications using JavaScript and the React library.'),
    (8, 'What is the advantage of using React Native for mobile app development?', 'a) Cross-platform compatibility', 'One of the main advantages of using React Native for mobile app development is cross-platform compatibility, allowing developers to write code once and deploy it on multiple platforms.'),
    (9, 'What is artificial intelligence (AI)?', 'b) The simulation of human intelligence in machines', 'Artificial intelligence (AI) refers to the simulation of human intelligence in machines, enabling them to perform tasks that typically require human intelligence.'),
    (9, 'What are machine learning algorithms?', 'a) Algorithms that enable machines to learn from and make predictions or decisions based on data', 'Machine learning algorithms are algorithms that enable machines to learn from and make predictions or decisions based on data without being explicitly programmed.'),
    (10, 'What is software testing?', 'c) The process of evaluating software to ensure its quality and correctness', 'Software testing is the process of evaluating software to ensure its quality and correctness by identifying defects, bugs, or errors in the software.'),
    (10, 'What is test automation?', 'b) The use of software tools and scripts to control the execution of tests', 'Test automation is the use of software tools and scripts to control the execution of tests and compare the actual results with the expected results.');"""
    cursor.execute(query_for_question)
    

    query_for_enrollment = """INSERT INTO enrollment (customer_id, course_id, enrollment_date)
VALUES
    (1, 1, '2024-01-15'),
    (1, 2, '2024-01-20'),
    (2, 1, '2024-01-18'),
    (3, 2, '2024-01-22'),
    (4, 3, '2024-01-25');"""
    cursor.execute(query_for_enrollment)
    

    query_fro_payment = """INSERT INTO payment (enrollment_id, amount, payment_date, customer_id)
VALUES
    (1, 150000.00, '2024-01-16', 1),
    (2, 200000.50, '2024-01-21', 1),
    (3, 175000.00, '2024-01-19', 2),
    (4, 120000.00, '2024-01-23', 3),
    (5, 300000.75, '2024-01-26', 4)"""
    cursor.execute(query_fro_payment)


    connection_db.commit()
    print("INSERT 0 1")

