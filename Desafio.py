#Questão 1

def pertence_fibonacci(numero):
    fibonacci = [0, 1]
    while fibonacci[-1] < numero:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    if numero in fibonacci:
        return f"O número {numero} pertence à sequência de Fibonacci."
    else:
        return f"O número {numero} não pertence à sequência de Fibonacci."

numero_informado = int(input("Informe um número: "))
resultado = pertence_fibonacci(numero_informado)
print(resultado)


#Questão 2

def contar_a(string):
    quantidade = string.lower().count('a')
    return f"A letra 'a' aparece {quantidade} vez(es) na string."

string_informada = input("Informe uma string: ")
resultado = contar_a(string_informada)
print(resultado)
