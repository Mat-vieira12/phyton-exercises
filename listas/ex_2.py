numeros=[]
iteracao=1
while iteracao<=5:
    numero=int(input("Por favor, digite um número: "))
    iteracao+=1
    numeros.append(numero)
print(f'Lista: {numeros}')
print(f'A soma dos números é: {sum(numeros)}')
print(f'O maior número é: {max(numeros)}')
print(f'O menor número é: {min(numeros)}')
print(f'A média é de: {sum(numeros)/len(numeros)}')