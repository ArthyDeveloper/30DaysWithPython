"""
 Try to use the is operator or the id function to investigate the difference between this:

numbers = [1, 2, 3, 4]
new_numbers = numbers + [5]

And this:

numbers = [1, 2, 3, 4]
numbers.append(5)

Are new_numbers and numbers the same thing? What about numbers before and after we append 5?
"""

numbers = [1, 2, 3, 4]
new_numbers = numbers + [5]

numbers = [1, 2, 3, 4]
numbers.append(5)

print(
  f"Usando is: {numbers is new_numbers}\n"
  f"Usando id:\nnumbers id: {id(numbers)}\nnew_numbers id: {id(new_numbers)}"
)