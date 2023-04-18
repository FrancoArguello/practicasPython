def palindromo(p1):
    palabra1= list()  
    aux =list() 
    
    for i in p1:
        palabra1.append(i)
        aux.append(i)
    
    aux.reverse()
    
 
    if aux == palabra1:
        print("es palindromo")
    else: 
        print("no es palindromo")
    
    
        
palindromo("pepe")