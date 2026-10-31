from datetime import date
from utils import add

print("Name: Umme Atiqua Jahin")
print("Today's date:", date.today())

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    total = add(num1, num2)

    print(f"The sum of {num1} and {num2} is {total}.")

except ValueError:
    print("Error: Please enter valid numbers.")