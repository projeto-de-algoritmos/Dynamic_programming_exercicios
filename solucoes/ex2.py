def numeros_digitos_unicos_contador(n):
    if n == 0:
        return 1 

    resultado = 10  
    digitos_unicos = 9

    for i in range(2, n + 1):
        digitos_unicos *= (11 - i)  
        resultado += digitos_unicos

    return resultado

n = 1
quantidade = numeros_digitos_unicos_contador(n)
print(quantidade)
