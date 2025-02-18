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

# Static inputs
num1 = 10
num2 = 25
num3 = 15

biggest = find_biggest(num1, num2, num3)
print("The biggest number is:", biggest)

# Alternative using max() function
def find_biggest_concise(num1, num2, num3):
    return max(num1, num2, num3)

biggest_concise = find_biggest_concise(num1, num2, num3)
print("The biggest number using max() is:", biggest_concise)
