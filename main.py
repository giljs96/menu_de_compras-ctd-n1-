lanches = {
    "hamburguer": 10.50,
    "cachorro quente": 8.50,
    "salgadinho": 6.80,
    "prato feito": 20.50,
}
bebidas = {
    "água": 2.50,
    "refrigerante": 5.50,
    "refresco": 4.80,
    "suco": 7.50,
}
forma_de_pagamento = {
    1: 'dinheiro',
    2: 'pix',
    3: 'cartão de débito',
    4: 'cartão de crédito',
}

print('ESCOLHA SUA REFEIÇÃO!!!')
escolha_cliente = []
continuacao = True
while continuacao:
    print(
        'Opções de Produto\n1- hambúrguer -- R$10.50\n2- cachorro quente -- R$8.50\n3- salgadinho -- R$6.80 \n4- prato feito -- R$20.50')
    escolha_lanche = int(input('Digite o código do produto: '))
    valor_lanche = float(0)
    if escolha_lanche == 1:
        valor_lanche = 10.50
        nome_lanche = str('hambúrguer')
    elif escolha_lanche == 2:
        valor_lanche = 8.50
        nome_lanche = str('cachorro quente')
    elif escolha_lanche == 3:
        valor_lanche = 6.80
        nome_lanche = str('salgadinho')
    elif escolha_lanche == 4:
        valor_lanche = 20.50
        nome_lanche = str('prato feito')
    quantidade_lanche = int(input(f'Quantidade de {nome_lanche} que você deseja? '))
    saida = True
    while saida:
        if quantidade_lanche == 0:
            print('QUANTIDADE INVÁLIDA! DIGITE NOVAMENTE\n')
            quantidade_lanche = int(input(f'Quantidade de {nome_lanche} que você deseja? '))
        else:
            print(f'{quantidade_lanche} unidade(s) de {nome_lanche}.\nValor total R${quantidade_lanche*valor_lanche:.2f}\n')
            escolha_cliente.append(valor_lanche*quantidade_lanche)
            saida = False
    valor_momento = sum(escolha_cliente)
    print(f'Por enquanto seu pedido está dando R${valor_momento:.2f}')
    escolha = int(input('Digite 1 para prosseguir para as bebidas\nDigite 2 para pedir mais comida\nR: '))
    if escolha == 1:
        continuacao = False

continuacao_bebida = True
while continuacao_bebida:
    print('OPÇÕES DE BEBIDA\n1- água\n2- refrigerante\n3-refresco\n4-suco')
    escolha_bebida = int(input('Digite o código do produto: '))
    valor_bebida = float(0)
    if escolha_bebida == 1:
        valor_bebida = 2.50
        nome_bebida = str('água')
    elif escolha_bebida == 2:
        valor_bebida = 5.50
        nome_bebida = str('refrigerante')
    elif escolha_bebida == 3:
        valor_bebida = 4.80
        nome_bebida = str('refresco')
    elif escolha_bebida == 4:
        valor_bebida = 7.50
        nome_bebida = str('suco')
    quantidade_bebida = int(input(f'Quantidade de {nome_bebida} que você deseja? '))
    saida_bebida = True
    while saida_bebida:
        if quantidade_bebida == 0:
            print('QUANTIDADE INVÁLIDA! DIGITE NOVAMENTE\n')
            quantidade_bebida = int(input(f'Quantidade de {nome_bebida} que você deseja? '))
        else:
            print(
                f'{quantidade_bebida} unidade(s) de {nome_bebida}.\nValor total R${quantidade_bebida * valor_bebida:.2f}\n')
            escolha_cliente.append(valor_bebida * quantidade_bebida)
            saida_bebida = False
            valor_momento = sum(escolha_cliente)
            print(f'Valor parcial do pedido: R${valor_momento:.2f}')
        escolha = int(input('Digite 1 para finalizar o pedido\nDigite 2 para pedir mais bebida\nR: '))
        if escolha == 1:
            saida_bebida = False
    valor_total = valor_momento
    print(f'Valor total do pedido: R${valor_total:.2f}')
    continuacao_bebida = False
form_pagamento = int(input(f'***QUAL A FORMA DE PAGAMENTO?***\n1- DINHEIRO\n2- PIX\n3- DÉBITO\n4- CRÉDITO\n'))
if forma_de_pagamento == 4:
    print(f'Não há desconto para essa forma de pagamento!\n')
else:
    print(f'Desconto de 5%: R${valor_total - (valor_total*5/100)}')