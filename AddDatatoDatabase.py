import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import datetime

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://fare-as-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

data = {
    "321654": {
        "name": "Aditya Pandey",
        "major": "Computer",
        "starting_year": 2023,
        "total_attendance": 7,
        "standing": "A",
        "year": 2,
        "last_attendance_time": current_time
    },
    "852741": {
        "name": "Emly Blunt",
        "major": "Economics",
        "starting_year": 2021,
        "total_attendance": 12,
        "standing": "C",
        "year": 3,
        "last_attendance_time": current_time
    },
    "963852": {
        "name": "Elon Musk",
        "major": "Physics",
        "starting_year": 2020,
        "total_attendance": 7,
        "standing": "B",
        "year": 4,
        "last_attendance_time": current_time
    }
}

try:
    for student_id, student_data in data.items():
        ref.child(student_id).set(student_data)
    print("Data successfully added to the database.")
except Exception as e:
    print(f"An error occurred while adding data to the database: {e}")
