Collection = {1, 2, 2, 2, 3, 4, 4, "Hello", "World", "World"}

#print(Collection) #{'Hello', 1, 2, 3, 4, 'World'}

#print(len(Collection)) #6

# it will always provide output in inorder.

#collection = set("") #for empty set; syntex = to write the wright way of code.

#print(collection)
#print(type(collection))
Collection.add("kumar")
Collection.add(8)
Collection.add((1,2,3))

print(Collection)
print(len(Collection))

Collection.remove((1, 2, 3))
Collection.pop()
print(Collection)
print(len(Collection))