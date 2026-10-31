from datetime import date
from utils import add
from utils import average

print("Name: Umme Atiqua Jahin")
print("Today's date:", date.today())

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    total = add(num1, num2)
    mean = average(num1, num2)

    print(f"Result: {num1} + {num2} = {total}")
    print(f"The sum of {num1} and {num2} is {total}.")
    print(f"The average of {num1} and {num2} is {mean}.")

except ValueError:
    print("Error: Please enter valid numbers.")