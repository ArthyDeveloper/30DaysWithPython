"""
Below we've provided a list of tuples, where each tuple contains details about an employee of a shop: their name, the number of hours worked last week, and their hourly rate. Print how much each employee is due to be paid at the end of the week in a nice, readable format.

employees = [
  ("Rolf Smith", 35, 8.75),
  ("Anne Pun", 30, 12.50),
  ("Charlie Lee", 50, 15.50),
  ("Bob Smith", 20, 7.00)
]
"""

employees = [
  ("Rolf Smith", 35, 8.75),
  ("Anne Pun", 30, 12.50),
  ("Charlie Lee", 50, 15.50),
  ("Bob Smith", 20, 7.00)
]

for x in employees:
  print(f"{x[0]}: {x[1] * x[2]}")

"""
For the employees above, print out those who are earning an hourly wage above average.

Hint: you can use a for loop and two variables to keep track of the total wage and the number of employees. Then, use the two variables to calculate the average. Finally, add another loop that goes through the employees list again and prints out only those who have an hourly wage above the calculated average.
"""
media_por_hora = 0
for x in employees:
  media_por_hora += x[-1]

media_por_hora = media_por_hora/len(employees)

lista = []
for x in employees:
  if x[-1] > media_por_hora:
    lista.append(x)

print(f"Ganham mais que a média: {lista}")