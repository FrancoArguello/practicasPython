#calcular la serie fibonacci

def serie_fibonacci(num):
    a= 0
    b=1
    c=0
    serie= [0]
    for i in range(num+1):
        if c > num: 
            return serie
        else:
            serie.append(b)
            #a, b= b, a+b #no se xq si lo pongo de otra forma da mal y asi da bien
            c=a+b
            a=b
            b=c

print(serie_fibonacci(100))
