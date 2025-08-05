import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="dbconnection"
)
db_info = con.cursor()
print(db_info)


print("---- User Input ----")

name = input("Enter your name: ")
guardian_name = input("Enter your guardian name: ")
father_name = input("Enter your father name: ")
address = input("Enter your address: ")

query = "INSERT INTO `student_info`(`Name`, `Guardian_Name`, `Father_Name`, `Address`) VALUES (%s, %s, %s, %s)"

value = (name, guardian_name, father_name, address)
run = db_info.execute(query, value)
con.commit()

print(f"{name }Data has been saved Successfully")
con.close()