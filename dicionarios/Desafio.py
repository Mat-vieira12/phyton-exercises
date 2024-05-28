produtos={}
print('Bem vindo à lista de compras')
cont=0
while True:
    cont+=1
    adicionar=input('Deseja adicionar um item? Y/n ')
    if adicionar.upper()=='N':
        break
    else:
        produto=input(f'Informe o produto: ')
        valor=float(input(f'Informe o valor: '))
        quant=int(input(f'Informe a quantidade: '))
        produtos.update({cont:[produto, valor, quant]})
total=0

print(50 * '-')
print('Carrinho de Compras')
print(50 * '-')

for cod, prod in produtos.items():
    subtotal = prod[1] * prod[2]
    print(f'{prod[0]} - R$ {prod[1]:.2f} - {prod[2]} un - R$ {subtotal:.2f}')
    total+= subtotal

print(50 * '-')
print(f'Total da compra: R$ {total:.2f}')
print(50 * '-')
