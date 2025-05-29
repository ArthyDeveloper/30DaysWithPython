"""
Ask the user to enter a number. Tell the user whether the number is positive, negative, or zero.
"""

num = float(input("Número: "))

if num > 0:
  print(f"O número {num} é maior que 0.")
elif num < 0:
  print(f"O número {num} é menor que 0.")
else:
  print(f"É 0, não sei o que você esperava.")