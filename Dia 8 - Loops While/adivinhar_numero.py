import random

playing = True
num_aleatorio = random.randint(1, 100)

while playing:
  escolha = int(input("Num: "))

  if escolha > num_aleatorio:
    print("Muito Alto!")
  elif escolha < num_aleatorio:
    print("Muito Baixo")
  elif escolha == num_aleatorio:
    print("Você acertou!")
    playing = False