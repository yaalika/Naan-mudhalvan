class Student:
def __init__(self, name,
rollnumber, cgpa):
self.name = name
self.rollnumber = rollnumber
self.cgpa cgpa
 def sort_students (student_list):
# Sort the list of students based on CGPA in descending order
sorted students =
sorted(student_list, key=lambda
student: student.cgpa, reverse=True)
return sorted_students
# Example usage:
students = [ =
Student("Alice", 101, 3.8),
Student("Bob", 102, 3.9),
Student("Charlie", 103, 3.7),
Student("David", 104, 3.95),
]
sorted_students =
sort_students (students)
# Print the sorted list of students
 for student in sorted_students:
print(f"Name: {student.name}, Roll Number: {student.rollnumber}, CGPA:

{student.cgpa}")