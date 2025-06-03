"""
Below is some simple data about characters from BoJack Horseman:

main_characters = [
  ("BoJack Horseman", "Will Arnett", "Horse"),
  ("Princess Carolyn", "Amy Sedaris", "Cat"),
  ("Diane Nguyen", "Alison Brie", "Human"),
  ("Mr. Peanutbutter", "Paul F. Tompkins", "Dog"),
  ("Todd Chavez", "Aaron Paul", "Human")
]

The data contains the character name, the voice actor or actress who plays them, and the species of the character.

Write a for loop that uses destructuring so that you can print each tuple in the following format:

BoJack Horseman is a horse voiced by Will Arnet.

Note that you're going to have to change the species information to lowercase when you print it. If you need a reminder on how to do this, we covered it in day 3 of the first week.
"""

main_characters = [
  ("BoJack Horseman", "Will Arnett", "Horse"),
  ("Princess Carolyn", "Amy Sedaris", "Cat"),
  ("Diane Nguyen", "Alison Brie", "Human"),
  ("Mr. Peanutbutter", "Paul F. Tompkins", "Dog"),
  ("Todd Chavez", "Aaron Paul", "Human")
]

for personagem, dublador, raca in main_characters:
  print(f"{personagem} is a {raca.lower()} voiced by {dublador}.")