# pip install firebase-admin
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase
creden = credentials.Certificate("/Users/muhammadmoiz/Desktop/MyPaython/employeekey.json")
firebase_admin.initialize_app(creden)

db = firestore.client()

print("Connection with Firebase database...")

# Collect user input
naam = input("Enter your name: ")
father_name = input("Enter your father name: ")
phone_number = int(input("Enter your phone: "))
adress = input("Enter your address: ")
english_marks = int(input("Enter your English marks: "))
urdu_marks = int(input("Enter your Urdu marks: "))
maths_marks = int(input("Enter your Maths marks: "))


total_marks = english_marks + urdu_marks + maths_marks
max_total = 300
percentage = round((total_marks / max_total) * 100, 2)

# Send data to Firestore
fetch_student = db.collection("student").document()
fetch_student.set({
    "name": naam,
    "fathername": father_name,
    "phone": phone_number,
    "address": adress,
    "englishmarks": english_marks,
    "urdumarks": urdu_marks,
    "mathsmarks": maths_marks,
    "total": total_marks,
    "percentage": percentage
})

print("Successfully inserted data into Firebase.")
