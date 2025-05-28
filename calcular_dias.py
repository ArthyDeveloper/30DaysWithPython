# Calculate and print the number of days, weeks, and months in 27 years. Don’t worry about leap years!

anos = int(input("Digite a quantidade de anos: "))

dias = anos*365
semanas = f"{(dias/7):.2f}"
meses = f"{(dias/30):.2f}"

print(
  f"Em {anos} anos, existem:\n"
  f"{dias} dias;\n"
  f"{semanas} semanas;\n"
  f"{meses} meses;\n"
)