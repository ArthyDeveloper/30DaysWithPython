"""
Below you’ll find a short list of quotes:

quotes = [
  "'What a waste my life would be without all the beautiful mistakes I've made.'",
  "'A bend in the road is not the end of the road... Unless you fail to make the turn.'",
  "'The very essence of romance is uncertainty.'",
  "'We are not here to do what has already been done.'"
]

Each quote is a string, but each string actually contains quote characters at the start and end. Using slicing, extract the text from each string, without these extra quote marks, and print each quote.

You may also want to try a solution using strip.
"""

quotes = [
  "'What a waste my life would be without all the beautiful mistakes I've made.'",
  "'A bend in the road is not the end of the road... Unless you fail to make the turn.'",
  "'The very essence of romance is uncertainty.'",
  "'We are not here to do what has already been done.'"
]

lista = []

for x in quotes:
  lista.append(x[1:-1])

print(lista)