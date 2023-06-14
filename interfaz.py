interfaz = open ("interfaz.txt", "w")
interfaz.write("programa para ingresar datos")

nombre = input("ingresar su nombre aquí: ")
edad = input("ingresar edad aquí: ")

interfaz.write(nombre)
interfaz.write(edad)
interfaz.close()


