Aluno=[]
nome=input('Digite o seu nome: ')
Aluno.append(nome)
iteracao=1
while iteracao<=4:
    nota=float(input(f'Digite a {iteracao}° nota: '))
    Aluno.append(nota)
    iteracao+=1

def calcularMedia(Aluno):
    media=sum (Aluno[1:])/4
    return media

m=calcularMedia(Aluno)
print(f'Sua média é {m} ')
if calcularMedia(Aluno)>=5:
    print('Você foi aprovado!')
else:
    print('Você foi reprovado!')