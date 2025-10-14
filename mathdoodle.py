def multiply(*numbers):
    product = 1
    for i in numbers:
        product *= i
    return product


print(multiply(2, 3, 4))  # Outputs: 24
print(multiply(5, 6))     # Outputs: 30
print(multiply(7))        # Outputs: 7
