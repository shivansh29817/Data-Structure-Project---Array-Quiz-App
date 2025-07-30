import random

questions = [
    {
        "id": 1,
        "question": "What does the OS do?",
        "options": ["Manages hardware", "Provides user interface", "Manages files", "All of the above"],
        "answer": "All of the above"
    },
    {
        "id": 2,
        "question": "What is a deadlock?",
        "options": ["A type of memory", "A condition where processes wait forever", "An error", "A CPU state"],
        "answer": "A condition where processes wait forever"
    },
    {
        "id": 3,
        "question": "Which SQL command is used to retrieve data?",
        "options": ["GET", "SELECT", "FETCH", "RETRIEVE"],
        "answer": "SELECT"
    },
    {
        "id": 4,
        "question": "What is normalization in DBMS?",
        "options": ["Backing up data", "Reducing redundancy", "Adding keys", "Deleting data"],
        "answer": "Reducing redundancy"
    },
    {
        "id": 5,
        "question": "What is the default port for HTTP?",
        "options": ["80", "21", "443", "8080"],
        "answer": "80"
    },
    {
        "id": 6,
        "question": "Which of these is a NoSQL database?",
        "options": ["MySQL", "PostgreSQL", "MongoDB", "SQLite"],
        "answer": "MongoDB"
    },
    {
        "id": 7,
        "question": "What is virtual memory?",
        "options": ["ROM", "Hard disk used as RAM", "RAM used as cache", "A flash drive"],
        "answer": "Hard disk used as RAM"
    },
    {
        "id": 8,
        "question": "Which protocol is used to send emails?",
        "options": ["SMTP", "HTTP", "FTP", "SNMP"],
        "answer": "SMTP"
    },
    {
        "id": 9,
        "question": "Which one is not a type of Operating System?",
        "options": ["Batch", "Time-sharing", "Real-time", "Compiler"],
        "answer": "Compiler"
    },
    {
        "id": 10,
        "question": "Which key uniquely identifies a record in a table?",
        "options": ["Foreign key", "Candidate key", "Primary key", "Composite key"],
        "answer": "Primary key"
    },
    {
        "id": 11,
        "question": "In OS, a process in waiting state waits for?",
        "options": ["CPU", "I/O resource", "RAM", "Cache"],
        "answer": "I/O resource"
    },
    {
        "id": 12,
        "question": "Which of these is a Linux command?",
        "options": ["mkdir", "makefolder", "dircreate", "fileopen"],
        "answer": "mkdir"
    },
    {
        "id": 13,
        "question": "Which layer of OSI model encrypts data?",
        "options": ["Presentation", "Session", "Network", "Data Link"],
        "answer": "Presentation"
    },
    {
        "id": 14,
        "question": "Which of the following is an ACID property in DBMS?",
        "options": ["Atomicity", "Accuracy", "Access", "Association"],
        "answer": "Atomicity"
    },
    {
        "id": 15,
        "question": "What is the full form of DBMS?",
        "options": ["Database Model System", "Database Management System", "Data Management Software", "Disk-Based Model Storage"],
        "answer": "Database Management System"
    }
]

# Optional: keep random fetch function if needed
def get_fixed_questions():
    return questions[:15]  # First 15 questions

