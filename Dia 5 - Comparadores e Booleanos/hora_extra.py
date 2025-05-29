"""
Write a program to determine whether an employee is owed any overtime. You should ask the user how many hours the employee worked this week, as well as the hourly wage for this employee.

If the employee worked more than 40 hours, you should print a message which says the employee is due some additional pay, as well as the amount due. The additional amount owed is 10% of the employees hourly wage for each hour worked over the 40 hours. In effect, the employees get paid 110% of their hourly wage for any overtime.
"""

horas_trabalhadas = float(input("Quantas horas você trabalhou: "))
ganho_por_hora = 7.59

if horas_trabalhadas > 40:
  juros = ganho_por_hora + (ganho_por_hora * 0.1)
  horas_extras = horas_trabalhadas - 40
  divida_empresa = horas_extras * juros
  print(
    f"Você trabalhou {horas_extras} horas extras.\n"
    f"A empresa te deve {divida_empresa}"
  )
elif horas_trabalhadas == 40:
  print("Tá tudo certo")
else:
  print("Tu tá é devendo hora.")