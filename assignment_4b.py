with open('output.txt', 'at') as file:
  a = input("Enter text to write to the file: ")
  file.write(a + "\n")
  print("Data successfully written to output.txt.")
  b = input("\nEnter text to append to the file:")
  file.write(b)
  print("Data successfully appended")

with open('output.txt', 'rt') as file:
  data = file.read()
  print("\nFinal output of output.txt:" ,"\n" + data)