dict = {
    "John" : 97.6,
    "Carol" : 79.9,
    "Mark" : 66.6
}
a = input("Enter the student's name: ")
if a in dict:
  print(f"{a}'s marks: {dict[a]}")
else:
  print("Student not found")