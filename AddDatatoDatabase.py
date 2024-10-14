import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://fare-as-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "321654":
        {
            "name": "Aditya Pandey",
            "major": "Computer",
            "starting_year": 2023,
            "total_attendance": 7,
            "standing": "A",
            "year": 2,
            "last_attendance_time": "2022-10-13 00:54:34"
        },
    "852741":
        {
            "name": "Emly Blunt",
            "major": "Economics",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "C",
            "year":3,
            "last_attendance_time": "2022-10-13 00:54:34"
        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "B",
            "year": 4,
            "last_attendance_time": "2022-10-13 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)