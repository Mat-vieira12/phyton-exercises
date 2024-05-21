nome=input('Olá, seja bem-vindo, por favor, digite seu nome: ')
iteracao=3
while iteracao>0:
    print(f'Você tem {iteracao} tentativas')
    senha=int(input('Digite sua senha: '))
    if senha!=123456:
        print('Senha incorreta')
        iteracao-=1
    else:
        print('Senha Correta')
        print(f'Olá, {nome}. Seja bem-vindo ao nosso banco!')
        break
    if iteracao==0:
        print('Sua senha foi bloqueada! Por favor, dirija-se a um de nossos caixas.')