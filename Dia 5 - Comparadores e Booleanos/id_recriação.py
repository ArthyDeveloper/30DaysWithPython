"""
Try to approximate the behaviour of the is operator using ==. Remember we have the id function for finding the memory address for a given value, and we can compare memory addresses to check for identity.
"""

x = 123
y = 123

if type(x) == type(y) and len(str(x)) == len(str(y)) and id(x) == id(y) and x == y:
  print("São iguais.")
else:
  print("Não são iguais.")