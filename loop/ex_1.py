n=int(input('Informe quantos números você quer calcular a média: '))
soma=0
interacao=1
while interacao <= n:
    numero=float(input('Informe um número: '))
    soma+=numero
    interacao+=1
print(f'A média dos números informados é igual a: {soma/n}')
