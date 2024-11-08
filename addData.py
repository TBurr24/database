import sqlite3


# Question class to represent each quiz question
class Question:
    def __init__(self, question_text, options, correct_answer):
        self.question_text = question_text
        self.options = options
        self.correct_answer = correct_answer
        self.user_answer = None  # To store the user's selected answer

    def check_answer(self):
        """Check if the user's answer is correct."""
        return self.user_answer == self.correct_answer

# Function to initialize the database and create tables for each course
def create_tables():
    conn = sqlite3.connect('quiz.db')
    c = conn.cursor()

    # Create tables for each course
    courses = ["DS3810", "DS3860", "BMGT3510", "DS3850"]
    for course in courses:
        c.execute(f'''
            CREATE TABLE IF NOT EXISTS {course} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question_text TEXT NOT NULL,
                option_1 TEXT NOT NULL,
                option_2 TEXT NOT NULL,
                option_3 TEXT NOT NULL,
                option_4 TEXT NOT NULL,
                correct_answer TEXT NOT NULL
            )
        ''')
    conn.commit()
    conn.close()

# Function to add a question to a specific table
def add_question(course, question_text, options, correct_answer):
    conn = sqlite3.connect('quiz.db')
    c = conn.cursor()
    c.execute(f'''
        INSERT INTO {course} (question_text, option_1, option_2, option_3, option_4, correct_answer)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (question_text, *options, correct_answer))
    conn.commit()
    conn.close()




if __name__ == "__main__":
    # Run the database setup only once
    create_tables()

    # Sample question addition (run once to add sample data)
    # add_question("DS3810", "What is data science?", ["Field of study", "Math concept", "Science fiction", "Not real"], "Field of study")

    # Launch GUI

# Adding questions for DS3810 (Programming Logic and Analytic Thinking)
add_question("DS3810", 
    "What is the purpose of a flowchart in programming?", 
    ["To test code", "To represent code structure visually", "To compile code", "To debug code"], 
    "To represent code structure visually")

add_question("DS3810", 
    "Which symbol is typically used to represent a decision point in a flowchart?", 
    ["Circle", "Square", "Diamond", "Triangle"], 
    "Diamond")

add_question("DS3810", 
    "What is pseudocode?", 
    ["A programming language", "An informal high-level description of a program", "A type of compiler", "A debugging tool"], 
    "An informal high-level description of a program")

add_question("DS3810", 
    "In a logical operation, what is the result of 'True AND False'?", 
    ["True", "False", "1", "Undefined"], 
    "False")

add_question("DS3810", 
    "Which of these is NOT a characteristic of an algorithm?", 
    ["It is finite", "It has clear steps", "It always requires complex logic", "It produces an output"], 
    "It always requires complex logic")

add_question("DS3810", 
    "What type of loop repeats as long as a specific condition is true?", 
    ["For loop", "While loop", "Do-while loop", "Repeat-until loop"], 
    "While loop")

add_question("DS3810", 
    "What is the purpose of an 'if' statement in programming?", 
    ["To create variables", "To make decisions based on conditions", "To execute code repeatedly", "To declare functions"], 
    "To make decisions based on conditions")

add_question("DS3810", 
    "Which logic gate returns true only if both inputs are true?", 
    ["AND gate", "OR gate", "XOR gate", "NOT gate"], 
    "AND gate")

add_question("DS3810", 
    "In programming, what is a function?", 
    ["A special type of variable", "A reusable block of code that performs a specific task", "A command to end the program", "A logical operator"], 
    "A reusable block of code that performs a specific task")

add_question("DS3810", 
    "What is debugging?", 
    ["Running the program", "Finding and fixing errors in code", "Compiling code", "Creating a flowchart"], 
    "Finding and fixing errors in code")
# Adding questions for DS3860 (Introduction to Business Database Management)
add_question("DS3860", 
    "What is the primary purpose of a database management system (DBMS)?", 
    ["To store data in tables only", "To retrieve and manage data efficiently", "To analyze data trends", "To visualize data"], 
    "To retrieve and manage data efficiently")

add_question("DS3860", 
    "Which of the following is an example of a relational database?", 
    ["MongoDB", "Microsoft Excel", "MySQL", "Apache Spark"], 
    "MySQL")

add_question("DS3860", 
    "What is a primary key in a database table?", 
    ["A unique identifier for each record", "A reference to another table", "A type of data type", "A column that can have duplicate values"], 
    "A unique identifier for each record")

add_question("DS3860", 
    "What SQL command is used to retrieve data from a database?", 
    ["INSERT", "DELETE", "SELECT", "UPDATE"], 
    "SELECT")

add_question("DS3860", 
    "Which of the following is NOT a type of database relationship?", 
    ["One-to-one", "One-to-many", "Many-to-one", "Primary-to-secondary"], 
    "Primary-to-secondary")

add_question("DS3860", 
    "In database design, what is normalization?", 
    ["A process to speed up queries", "A process to remove redundancies and improve data structure", "A process to back up data", "A type of indexing"], 
    "A process to remove redundancies and improve data structure")

add_question("DS3860", 
    "What does SQL stand for?", 
    ["Structured Question Language", "Structured Query Language", "System Query Language", "Sequential Query Language"], 
    "Structured Query Language")

add_question("DS3860", 
    "Which SQL clause is used to filter results based on specific conditions?", 
    ["WHERE", "GROUP BY", "ORDER BY", "HAVING"], 
    "WHERE")
add_question("DS3860", 
    "What is the purpose of a foreign key in a database?", 
    ["To uniquely identify each record in a table", "To enforce relationships between tables", "To index the table", "To define data types"], 
    "To enforce relationships between tables")

add_question("DS3860", 
    "What type of database is optimized for large-scale data analysis?", 
    ["Transactional database", "Relational database", "Data warehouse", "Flat file database"], 
    "Data warehouse")
# Adding questions for BMGT3510 (Management and Organizational Behavior)
add_question("BMGT3510", 
    "What is the primary focus of organizational behavior as a field of study?", 
    ["Understanding individual financial performance", "Understanding human behavior in organizational settings", "Understanding global markets", "Understanding organizational profits"], 
    "Understanding human behavior in organizational settings")

add_question("BMGT3510", 
    "Which of the following is a key function of management?", 
    ["Investing", "Organizing", "Marketing", "Competing"], 
    "Organizing")

add_question("BMGT3510", 
    "Who is known as the father of scientific management?", 
    ["Elton Mayo", "Henri Fayol", "Frederick Taylor", "Max Weber"], 
    "Frederick Taylor")

add_question("BMGT3510", 
    "What does Maslow's Hierarchy of Needs model suggest?", 
    ["All needs must be satisfied at once", "Basic needs must be met before higher-level needs", "Social needs are the highest priority", "Only self-actualization is important"], 
    "Basic needs must be met before higher-level needs")

add_question("BMGT3510", 
    "Which of the following is an example of intrinsic motivation?", 
    ["Receiving a bonus", "Getting praise from a manager", "Feeling personally satisfied with one's work", "Being promoted"], 
    "Feeling personally satisfied with one's work")

add_question("BMGT3510", 
    "What is a common characteristic of a transformational leader?", 
    ["Focuses only on profits", "Ignores employee input", "Inspires and motivates followers", "Focuses on routine tasks"], 
    "Inspires and motivates followers")

add_question("BMGT3510", 
    "What term describes a person’s belief in their capability to perform a task?", 
    ["Self-esteem", "Self-efficacy", "Motivation", "Self-actualization"], 
    "Self-efficacy")

add_question("BMGT3510", 
    "Which conflict management style aims for a win-win situation?", 
    ["Competing", "Avoiding", "Compromising", "Collaborating"], 
    "Collaborating")

add_question("BMGT3510", 
    "What is 'organizational culture'?", 
    ["A set of financial goals for the organization", "A set of shared values, beliefs, and norms within an organization", "The organizational structure", "The official company slogan"], 
    "A set of shared values, beliefs, and norms within an organization")

add_question("BMGT3510", 
    "In Herzberg’s Two-Factor Theory, which of the following is considered a hygiene factor?", 
    ["Achievement", "Recognition", "Salary", "Personal growth"], 
    "Salary")
# Adding questions for DS3850 (Introduction to Python)
add_question("DS3850", 
    "What is the correct file extension for Python files?", 
    [".py", ".python", ".pyt", ".pt"], 
    ".py")

add_question("DS3850", 
    "Which of the following is the correct syntax to output 'Hello, World!' in Python?", 
    ["echo 'Hello, World!'", "print('Hello, World!')", "printf('Hello, World!')", "System.out.println('Hello, World!')"], 
    "print('Hello, World!')")

add_question("DS3850", 
    "What is the result of 3 ** 2 in Python?", 
    ["6", "9", "8", "5"], 
    "9")

add_question("DS3850", 
    "What keyword is used to define a function in Python?", 
    ["function", "def", "func", "define"], 
    "def")

add_question("DS3850", 
    "Which of the following data types is immutable in Python?", 
    ["List", "Dictionary", "Tuple", "Set"], 
    "Tuple")

add_question("DS3850", 
    "What is the output of the following code: print(type(5))?", 
    ["<class 'int'>", "<class 'str'>", "<class 'float'>", "<class 'bool'>"], 
    "<class 'int'>")

add_question("DS3850", 
    "Which of the following can be used to create a comment in Python?", 
    ["//", "#", "<!-- -->", "/* */"], 
    "#")

add_question("DS3850", 
    "What will the following code output: print(10 % 3)?", 
    ["3", "1", "0", "2"], 
    "1")

add_question("DS3850", 
    "What is the purpose of the 'len' function in Python?", 
    ["To return the type of a variable", "To print a variable", "To find the length of an object", "To add two numbers"], 
    "To find the length of an object")

add_question("DS3850", 
    "Which of the following methods is used to add an item to the end of a list in Python?", 
    ["add()", "append()", "insert()", "extend()"], 
    "append()")
