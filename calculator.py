# Ask the user for input
num1 = float(input("Enter first number:"))
operator = input("Enter operator (+, -, *, /, %, **): ")
num2 = float(input("Enter second number:"))

# Perform calculation
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
   result = num1 * num2
elif operator == "/":
    if num2 != 0:
      result = num1 / num2
else:
    result = "Error: Division by zero"
elif operator == "%":
    result = num1 % num2
elif operator == "**":
    result = num1 ** num2
else:
    result = "invalid operator"

# Print the result
print("Result:", result)
