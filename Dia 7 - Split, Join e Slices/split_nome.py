"""
Ask the user to enter their given name and surname in response to a single prompt. Use split to extract the names, and then assign each name to a different variable. For this exercise, you can assume that the user has a single given name and a single surname.
"""

nome = input("Seu nome: ")

nome = nome.split(" ")

nome, sobrenome = nome[0], nome[1]

print(nome, sobrenome)