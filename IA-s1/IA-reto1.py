y = int(input("Enter a number for y: "))
x = int(input("Enter a number for x: "))
z = int(input("Enter a number for z: "))
numeros = [y, x, z]
mayor = max(y, x, z)
numeros_ordenados = sorted(numeros, reverse=False)
print("The largest number is:", mayor)
print("The numbers in descending order are:", numeros_ordenados)
