dic={
    "aluno":'notas'
}

notas=[]

iteracao=1
while True:
    opc=int(input('Selecione a opção: \n1-Cadastrar Aluno \n2- Mostar alunos cadastrados \n3-Sair\n'))
    if opc==1:
        aluno=(input('Digite o nome do Aluno: '))
        n=int(input('Quantas notas você deseja cadastrar? '))
        for i in range(n):
            notas=[float(input(f'Digite a {i}ª nota: '))]
            notas.append(notas)
        iteracao+=1
        print(50 * '-' '\n')
        print(dic)
    elif opc==2:
        print('goat')
    elif opc==3:
        print(50 * '-')
    else:
         print('Opção inválida, tente novamente')

print(dic)