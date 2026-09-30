import math

x = 5.75
fractional, integral = math.modf(x)

print("Fractional part:", fractional)  # Output: 0.75
print("Integer part:", integral)        # Output: 5.0
