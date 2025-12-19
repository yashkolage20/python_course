import os
file_name = "practise.txt"

if os.path.exists(file_name):
    print("File already exists.\n")
else:
  print("file does not exist.\n")

with open(file_name, "r") as file:
  line1 = file.readline()
  line2 = file.readline()
  print(f"Line1: {line1}")
  print(f"Line2: {line2}")