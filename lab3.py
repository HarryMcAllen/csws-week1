import numbers

print("The first three items in the list are:")
cubes = [x**3 for x in range(1,11)[-3:]]
print(cubes)

letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]
print(letters)
    
for i in range (0,len(letters),2):
    print(letters[i])

for i in range (1,len(letters),2):
 print(letters[i])