#WHILE

i=1
num=7
while i <=10:
    print(f"{ num } * { i } = { num * i }")
    i += 1
else:
    print("ciclo terminado")
    #Ciclo infinito
    while True:
        break

    #El for recorre iterables
    #un interable es algo que se puede recorrer

    #for vriable in iterable:
    my_string = "Hola"

    for letra in my_string:
        print(letra, end=", ")
        print()

        lista = ["uno", "dos" , "tres", "cuatro"]
        for item in lista:
            print(item)

            #function range
            #range(end)
            for i in range(10):
               print(i, end=', ')
            print()
            #range(in1, end)
            for i in range(10,20):
                print(i, end=', ')
            print()
            #range(in1, end)
            for i in range(10,20,2):
                print(i, end=', ')
            print()