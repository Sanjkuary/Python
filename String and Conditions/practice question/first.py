#programe for asking user their 3 movies and puting all in list.

movies = []

mov1 = input("Enter first movie name :")
mov2 = input("Enter second movie name :")
mov3 = input("Enter third movie name :")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)

#second method to write the same code

movies = []

movies.append(input("enter first name: "))
movies.append(input("enter second name: "))
movies.append(input("enter third name: "))

print(movies)