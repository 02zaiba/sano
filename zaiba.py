def find_biggest(num1, num2, num3):
    """
    Finds the biggest of three numbers.

    Args:
        num1: The first number.
        num2: The second number.
        num3: The third number.

    Returns:
        The largest of the three numbers.
    """

    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

# Get input from the user (optional, you can also hardcode values)
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))

    biggest = find_biggest(num1, num2, num3)
    print("The biggest number is:", biggest)

except ValueError:
    print("Invalid input. Please enter numbers only.")



#  Alternative using the max() function (more concise):

def find_biggest_concise(num1, num2, num3):
  return max(num1, num2, num3)

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))

    biggest = find_biggest_concise(num1, num2, num3)
    print("The biggest number is:", biggest)

except ValueError:
    print("Invalid input. Please enter numbers only.")
