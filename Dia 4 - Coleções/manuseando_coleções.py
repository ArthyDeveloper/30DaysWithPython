"""
  Create a movies list containing a single tuple. The tuple should contain a movie title, the director’s name, the release year of the movie, and the movie’s budget.
  Use the input function to gather information about another movie. You need a title, director’s name, release year, and budget.
  Create a new tuple from the values you gathered using input. Make sure they’re in the same order as the tuple you wrote in the movies list.
  Use an f-string to print the movie name and release year by accessing your new movie tuple.
  Add the new movie tuple to the movies collection using append.
  Print both movies in the movies collection.
  Remove the first movie from movies. Use any method you like.
"""

movies = [
  ("Título", "Fulano", 2005, "R$10.000")
]

titulo = input("Título: ")
diretor = input("Diretor: ")
ano_filme = int(input("Ano do filme: "))
orçamento = input("Orçamento: ")

insert = (titulo, diretor, ano_filme, orçamento)

print(f"Filme 1: {movies[0][0]}, ano {movies[0][2]}")

movies.append(insert)
print(f"Filme 1: {movies[0][0]}, ano {movies[0][2]}")
print(f"Filme 2: {movies[1][0]}, ano {movies[1][2]}")

print(movies)
movies = movies.pop(-1)
print(movies)