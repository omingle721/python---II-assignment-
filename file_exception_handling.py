filename = input("Enter the filename: ")

try:
    file = open(filename, "r")
    print("File opened successfully.")
    print(file.read())
    file.close()

except FileNotFoundError:
    print("Error: The file does not exist.")

except PermissionError:
    print("Error: Permission denied. Cannot read the file.")