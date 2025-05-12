import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from sympy import symbols, diff, solve

x_sym = symbols('x')
f_sym = x_sym**2
f_prime = diff(f_sym, x_sym)
critical_points = solve(f_prime, x_sym)

def f(x):
    return x**2 

a = float(input("Enter the starting x-value (a): "))
b = float(input("Enter the ending x-value (b): "))

area, _ = quad(f, a, b)

x = np.linspace(a - 1, b + 1, 500)
y = f(x)

plt.plot(x, y, label="y = f(x)")

x_fill = np.linspace(a, b, 500)
y_fill = f(x_fill)
plt.fill_between(x_fill, y_fill, color="lightblue", alpha=0.5, label=f"Area = {area:.2f}")

for cp in critical_points:
    if a - 1 <= cp <= b + 1:
        plt.scatter(cp, f(cp), color="red", zorder=5)
        plt.text(cp, f(cp), f"({cp:.2f}, {f(cp):.2f})", fontsize=8)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Area Under the Curve with Critical Points")
plt.legend()
plt.grid()

plt.show()