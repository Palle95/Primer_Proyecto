archivo = open ("archivo.txt","w")
archivo.write ('Porsche Carrera GT')
archivo.close()

archivo = open ('archivo.txt','r')
texto = archivo.read()
print(texto)
archivo.close()