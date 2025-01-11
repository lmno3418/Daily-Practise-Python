# Create variables for different types (int, float, string, list) and perform operations.#
a = 5
b = 1.43
c = "ILU"
d = [1, 2, 3, "a", "b", "c"]

print(
    "Type of A\n",
    type(a),
    "Type of B\n",
    type(b),
    "Type of C\n",
    type(c),
    "Type of D\n",
    type(d),
)

print(a + a, a - a, a * a, a / a, a % a, a**a)
print(b + b, b - b, b * b, b / b, b % b, b**b)
print(c + c, c * 2, "I" in c, c[0:1])
print(d + d, d * 2, "I" in d, d[0:4])
