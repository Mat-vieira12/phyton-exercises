def calcularMedia(nota1,nota2,nota3,nota4):
    media=(nota1+nota2+nota3+nota4)/4
    return media

print('Calculadora de Média')
n1=float(input('Nota 1: '))
n2=float(input('Nota 2: '))
n3=float(input('Nota 3: '))
n4=float(input('Nota 4: '))

m=calcularMedia(n1,n2,n3,n4)
print(f'Sua média é {m} ')