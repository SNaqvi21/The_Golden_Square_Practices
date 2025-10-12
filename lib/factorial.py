def factorial(n):
    product = n
    print(f"at the start product is {product}")
    while n > 2:
        n -= 1
        print(f"we multiply {product} by {n}")
        product *= n
        print(f"we get {product}")

    return product

print(f"""
 Running: factorial(3)
Expected: 6
  Actual: {factorial(3)}
""")

print(f"""
 Running: factorial(4)
Expected: 24
  Actual: {factorial(4)}
""")

print(f"""
 Running: factorial(3)
Expected: 720
  Actual: {factorial(6)}
""")

print(f"""
 Running: factorial(3)
Expected: 5040
  Actual: {factorial(7)}
""")