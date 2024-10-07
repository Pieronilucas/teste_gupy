def verifica_letra(frase):
    list= []
    for i in frase:
        if i.lower() == "a":
            list.append(i)
    return list

def entrada(entrada):
    list = verifica_letra(entrada)
    return list

    

try:
    entrada_user = input("Por favor, insira a frase a ser verificada: ")
    verificar_frase = all(i.isalpha() or i.isspace() for i in entrada_user)
    if verificar_frase:
        list = entrada(entrada_user)
        quantidade_a = len(list)
        if quantidade_a > 0:
            print(f"A quantidade 'A' na frase é de: {quantidade_a}")
        else:
            print("A frase não possui nenhuma letra 'A' ")
    else:
        print("Por favor, insira apenas letras e espaços na frase.")
except ValueError:
    print("erro inesperado.")