for x in range(2, 101):
  for y in range(2, x):
    if x % y == 0:
      break
  else:
    print(f"{x} é primo.")