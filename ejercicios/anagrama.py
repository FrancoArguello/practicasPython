'''
* Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 '''

def anagrama(p1, p2):
    palabra1= list()
    palabra2 = list()
    long1 = len(p1)
    long2 =len(p2)
    
    if long1 == long2 and p1!=p2:  #verificamos si tienen misma cantidad de letras y si son la misma palabra o no
        for i in p1:
            i = i.upper()
            palabra1.append(i)
        for j in p2:
            j = j.upper()
            palabra2.append(j)

        palabra1.sort()
        palabra2.sort()
        print(palabra1,palabra2)
        
        if palabra1 == palabra2:
            print("las palabras ingresadas son anagramas")
        else:
            print("las palabras ingresadas no son un anagrama")
       
            
    else:
        print("las palabras ingresadas no son anagramas")
        

anagrama("amor", "roma")


print("\n\n Otra opcion")

#otra opcion
def anagrama2( p1, p2):
    if p1.lower() == p2.lower():
        return {"son la misma palabra, no son anagramas entre si"}
    return sorted(p1.lower()) == sorted(p2.lower())    
#la funcion sorted() nos va a devolver una lista temporal ordenada, no nos modifica el valor definivo como si lo hace el metodo .sort()
    
print(anagrama2("amor", "amor")) #lo ponemos en un print para capturar el valor del return