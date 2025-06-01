"""
Print the list, [1, 2, 3, 4, 5], in the format 1 | 2 | 3 | 4 | 5 using the join method. Remember that you can only join collections of strings, so you’re going to need to do some initial processing of the list of numbers.
"""

lista = [1, 2, 3, 4, 5]

for x in lista:
  lista = ("| ").join(lista)
print(lista)