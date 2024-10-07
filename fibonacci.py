def fibonacci(num):
    sequencia = [0, 1]
    
    while True:
        proxima_seq = sequencia[-1] + sequencia[-2]
        #verifica loop
        if proxima_seq > num:
            break
        sequencia.append(proxima_seq)

    return sequencia

def fibonacci_ou_nao(number):
    if number < 0:
        return False
    sequencia_fib = fibonacci(number)
    return number in sequencia_fib

try:
    entrada_user = int(input("Informe um número: "))
    
    if fibonacci_ou_nao(entrada_user):
        print(f"O número {entrada_user} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {entrada_user} não pertence à sequência de Fibonacci.")
except ValueError:
    print("Por favor, insira um número válido.")
