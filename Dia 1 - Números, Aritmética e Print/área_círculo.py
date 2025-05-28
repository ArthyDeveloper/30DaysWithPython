# Calculate and print the area of a circle with a radius of 5 units. You can be as accurate as you like with the value of pi.
import math

pi = float(f"{math.pi:.5f}")
raio = float(input("Digite o raio do círculo: "))

print(f"A área do círculo é {pi*raio**2}")