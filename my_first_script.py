import numpy as np

def nerdy_computation(x):
    """Returns the sum of the squares of the first x natural numbers using numpy."""
    total = 0
    for i in range(x + 1):  # x + 1 als je inclusief x wilt rekenen
        total += i**2
    return total

print("Hello MUDE! Let's compute something nerdy:")
result = nerdy_computation(10)
print(f"The sum of the squares of the first 10 natural numbers is {result}")