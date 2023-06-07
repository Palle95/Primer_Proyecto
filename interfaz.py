interfaz = open ("interfaz.txt", "w")


newwork.write("programa para ingresar datos")

nombre = input("ingresar aquí: ")
edad = int(input("ingresar edad aquí: "))

interfaz = open ("nterfaz.txt","r")
nombre = interfaz.read()
edad = interfaz.read()

print (nombre,edad)

interfaz.close()


