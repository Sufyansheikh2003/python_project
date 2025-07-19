#List, Dictionary

Courses = ["HTML", "css", "Python", "PHP", "Java", "Wordpress", "MySql", "ASP.Net", "AI", "Graphic Designing"]
print(Courses[6])
print(Courses[-3])
print(Courses[-1])
#Print 2-6 Length
print(Courses[2:6])


#Lenght Of Course
print(f"Length Of Courses: {len(Courses)}")
Courses.append("Python")
print(Courses)
Courses.append("PHP")
print(Courses)
Courses.insert(6, "PWD")
print(Courses)
Courses.insert(9, "Data Analysis")
print(f"Length Of Courses: {len(Courses)}")
Courses.remove("HTML")
print(Courses)
print(Courses.pop())
print(Courses)
print(f"Length Of Courses: {len(Courses)}")
Courses.sort()
print(f"Ascending Order: {Courses}")
Courses.sort(reverse=True)
print(f"Descending Order: {Courses}")
Courses.extend(["Urdu", "IOT", "Net Working"])
print(f"After Adding: {Courses}")
print(f"Length Of Courses: {len(Courses)}")
Courses.clear()
print(f"Length Of Courses: {len(Courses)}")
print(Courses)


#Count