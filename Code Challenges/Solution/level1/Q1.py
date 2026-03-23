a = 2
b = 4
print(f"a: {a}, b: {b}")
a, b = b, a
print(f"a: {a}, b: {b}")
a += b
b = a - b
a -= b
print(f"a: {a}, b: {b}")

