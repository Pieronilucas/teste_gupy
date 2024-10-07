def soma(indice):    
    soma = 0
    k = 1
    while k < indice:
        k += 1
        soma += k
    return soma

indice = 12
resultado = soma(indice)
print(resultado)