import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
def f(x):
    return x**2 

a = float(input("Enter the starting x-value (a): "))
b = float(input("Enter the ending x-value (b): "))

area, _ = quad(f, a, b)
print(f"The area under the curve from {a} to {b} is: {area}")

x = np.linspace(a - 1, b + 1, 500)
y = f(x)

plt.plot(x, y, label="y = f(x)")

x_fill = np.linspace(a, b, 500)
y_fill = f(x_fill)
plt.fill_between(x_fill, y_fill, color="lightblue", alpha=0.5, label=f"Area = {area:.2f}")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Area Under the Curve")
plt.legend()
plt.grid()

plt.show()