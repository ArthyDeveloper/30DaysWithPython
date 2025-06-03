"""
Investigate what happens when you try to zip two iterables of different lengths. For example, try to zip a list containing three items, and a tuples containing four items.
"""

x = ("a", "b", "c", "d")
y = (1, 2, 3)

for letra, numero in zip(x, y):
  print(letra, numero)