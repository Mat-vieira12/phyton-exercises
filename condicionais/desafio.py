print('Por favor, informe o que você deseja calcular: ')
op1= print('1) Tensão')
op2= print('2) Resistência')
op3= print('3) Corrente')
conta=int(input(': '))
if conta==1:
    resistencia=float(input('Informe  a resistência: '))
    corrente=float(input('Informe a corrente: '))
    tensao=resistencia*corrente
    print(f'A tensão é igual a: {tensao} V')
elif conta==2:
    corrente=float(input('Por favor informe a corrente: '))
    tensao=float(input('Por favor informe a tensão: '))
    resistencia=tensao/corrente
    print(f'A resistência é igual a: {resistencia} Ω')
elif conta==3: 
    tensao=float(input('Por favor informe a tensão: '))
    resistencia=float(input('Informe  a resistência: '))
    corrente=tensao/resistencia
    print(f'A corrente é igual a: {corrente} V')
else:
    print('Por favor, informe uma opção válida')