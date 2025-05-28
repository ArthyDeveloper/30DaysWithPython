"""
Below you’ll find some code with a number of errors. Try to go through the program line by line and fix the issues in the code. I’d encourage you to try running the program while you’re working on it, as reading the error messages is great practice for debugging your own programs.

hourly_wage = input("Please enter your hourly wage: ')

prnt("Hourly wage: ")
print(hourlywage)
print("Hours worked: ")
print(hours_worked)

hours_worked = input("How many hours did you work this week? ")
"""

"""
Erros detectados:

Input hours_worked estava no fim do script, após o print em que seu valor é usado.
Input de hourly_wage estava com uma aspas dupla e uma aspas simples.

Print de Hourly wage estava escrito errado.
Variável hourly_wage estava escrito errado em seu print.

"""

# Código corrigido:

hourly_wage = input("Please enter your hourly wage: ")
hours_worked = input("How many hours did you work this week? ")

print("Hourly wage: ")
print(hourly_wage)
print("Hours worked: ")
print(hours_worked)
