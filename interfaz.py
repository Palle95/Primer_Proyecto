interfaz = open ("interfaz.txt", "w")
interfaz.write("programa para ingresar datos \n")

nombre = input("ingresar su nombre aquí: \n")
edad = input("ingresar edad aquí: \n")

interfaz.write(nombre)
interfaz.write(edad)
interfaz.close()

