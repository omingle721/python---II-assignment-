# Opening file in write mode and writing data
file = open("sample.txt", "w")
file.write("Hello, this is the first line.\n")
file.write("Python file handling demonstration.\n")
file.close()

# Opening file in read mode and reading contents
file = open("sample.txt", "r")
print("File Content:")
print(file.read())
file.close()

# Opening file in append mode and adding more content
file = open("sample.txt", "a")
file.write("This line is appended to the file.\n")
file.close()

# Reading file again to verify appended content
file = open("sample.txt", "r")
print("\nUpdated File Content:")
print(file.read())
file.close()