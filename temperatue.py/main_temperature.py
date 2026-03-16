from temperature.celsius_to_fahrenheit import convert as ctof
from temperature.fahrenheit_to_celsius import convert as ftoc

choice = input("Enter conversion type (1: C to F, 2: F to C): ")

if choice == "1":
    c = float(input("Enter temperature in Celsius: "))
    print("Temperature in Fahrenheit:", ctof(c))

elif choice == "2":
    f = float(input("Enter temperature in Fahrenheit: "))
    print("Temperature in Celsius:", ftoc(f))

else:
    print("Invalid choice")