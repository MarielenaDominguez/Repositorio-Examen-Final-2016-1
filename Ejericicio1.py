def es_primo(n):
    tipo = "primo"
    a=[]
    for i in range (1,n+1):
        if n % i == 0:
            a.append(i)
    if len(a) > 2:
        tipo = "compuesto"
    return tipo
p=[]
for n in range (1,10):
    if es_primo(n) == "primo":
        p.append(n)

print ("El número de primos entre 1 y 1000 es", len(p))
    