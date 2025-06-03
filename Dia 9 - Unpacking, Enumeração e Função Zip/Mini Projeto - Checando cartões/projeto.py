x = 5893804115457289
x = str(x)

check_char, x = x[-1], x[:len(x)-1]
x = x[::-1]

sum = 0
for char in x:
  if int(char) % 2 == 0 and (int(char)*2) <= 9:
    sum += int(char)*2
  elif int(char) % 2 == 0 and (int(char)*2) > 9:
    sum += (int(char)*2) - 9

sum += int(check_char)

if sum % 10 == 0:
  print("Número válido.")
else:
  print("Número inválido.")