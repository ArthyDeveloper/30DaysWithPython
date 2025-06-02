"""
Ask the user to enter a word, and then print out the length of the word. You should account for any excess whitespace in the user’s input, so you’re going to have to process the string before you find its length.

If you want to take this a little bit further, you an ask the user for a long piece of text. You can then tell them how many how many characters are in the text overall, and you can also provide them a word count.
"""

nome = "   teste      ".strip()
frase = "lorem ipsum dolor sit amet".strip()

charQtd = 0
for x in frase.split():
  charQtd += len(x)

print(
  f"Tamanho do nome: {len(nome)}\n"
  f"Tamanho da frase: {charQtd}"
)
