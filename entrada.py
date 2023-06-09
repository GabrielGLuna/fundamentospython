num_a = int(input("Ingresa un numero : "))
num_b = int(input("Ingresa otro numero : "))

print(num_a + num_b)

name = input("Ingresa tu nombre : ")
age = int(input("Ingresa tu edad : "))
city = input("Ingresa tu viudad/pueblo : ")

#String Format
""""
Holaa, soy name, tengo age años y vivo en cit
"""
greeting ="Hola soy {}, tengo {} años y vivo en {}"

print(greeting.format(name,age,city))

greeting_2 =f"Holaa, soy {name},tengo {age} años y vivo en {city}"
print(greeting_2)