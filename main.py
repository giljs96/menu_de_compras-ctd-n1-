#dicionário com nome e valor dos lanches
lanches = {
    "hamburguer": 10.50,
    "cachorro quente": 8.50,
    "salgadinho": 6.80,
    "prato feito": 20.50,
}
#dicionário com nome e valor das bebidas
bebidas = {
    "água": 2.50,
    "refrigerante": 5.50,
    "refresco": 4.80,
    "suco": 7.50,
}
#dicionário com código e a forma de pagamento
forma_de_pagamento = {
    1: 'dinheiro',
    2: 'pix',
    3: 'cartão de débito',
    4: 'cartão de crédito',
}
#uma lista com os códigos que o programa possui
codigos = [1, 2, 3, 4]

print('*-*ESCOLHA SUA REFEIÇÃO*-*\n')
#uma lista que vai armazenar os valores de acordo com as escolhas do cliente, no final a soma retornará o valor total da compra
escolha_cliente = []

escolha_cont = True
while escolha_cont:
#estrutura de repetição onde o cliente escolherá qual produto deseja, de acordo com os códigos informados
#enquanto "continuacao" for verdadeiro, o comando estará rodando para a escolha do produto
#parte do código destinada a escolha do produto: o usuário deve inserir o código do produto de acordo com a tabela informada
    continuacao = True
    while continuacao:
        print(
            '***OPÇÕES DE LANCHE***\n1- hambúrguer -- R$10.50\n2- cachorro quente -- R$8.50\n3- salgadinho -- R$6.80 \n4- prato feito -- R$20.50')
        escolha_lanche = int(input('Digite o código do produto: '))
        valor_lanche = float(0)
        if escolha_lanche == 1:
            valor_lanche = 10.50
            nome_lanche = str('hambúrguer')
            continuacao = False
        elif escolha_lanche == 2:
            valor_lanche = 8.50
            nome_lanche = str('cachorro quente')
            continuacao = False
        elif escolha_lanche == 3:
            valor_lanche = 6.80
            nome_lanche = str('salgadinho')
            continuacao = False
        elif escolha_lanche == 4:
            valor_lanche = 20.50
            nome_lanche = str('prato feito')
            continuacao = False
        elif escolha_lanche not in codigos:
            print('---CÓDIGO INVÁLIDO---')

    #o usuário deve informar a quantidade de lanche que irá querer
    qtd_cont = True
    while qtd_cont:
        quantidade_lanche = int(input(f'Quantidade de {nome_lanche} que você deseja? '))
        if quantidade_lanche == 0:
            print('---QUANTIDADE INVÁLIDA! DIGITE NOVAMENTE---\n')
        else:
            print(f'{quantidade_lanche} unidade(s) de {nome_lanche}.\nValor total R${quantidade_lanche*valor_lanche:.2f}\n')
            escolha_cliente.append(valor_lanche*quantidade_lanche)
            qtd_cont = False
    valor_momento = sum(escolha_cliente)
    print(f'Por enquanto seu pedido está dando R${valor_momento:.2f}')

    #agora o usuário informará a bebida que deseja
    continuacao_bebida = True
    while continuacao_bebida:
        print('***OPÇÕES DE BEBIDA***\n1- água -- R$2,50\n2- refrigerante R$5,50\n3- refresco R$4,80\n4- suco R$7,50')
        escolha_bebida = int(input('Digite o código do produto: '))
        valor_bebida = float(0)
        if escolha_bebida == 1:
            valor_bebida = 2.50
            nome_bebida = str('água')
            continuacao_bebida = False
        elif escolha_bebida == 2:
            valor_bebida = 5.50
            nome_bebida = str('refrigerante')
            continuacao_bebida = False
        elif escolha_bebida == 3:
            valor_bebida = 4.80
            nome_bebida = str('refresco')
            continuacao_bebida = False
        elif escolha_bebida == 4:
            valor_bebida = 7.50
            nome_bebida = str('suco')
            continuacao_bebida = False
        elif escolha_bebida not in codigos:
            print('CÓDIGO INVÁLIDO')

    #quantidade de bebida
    qtd_cont_b = True
    while qtd_cont_b:
        quantidade_bebida = int(input(f'Quantidade de {nome_bebida} que você deseja? '))
        if quantidade_bebida == 0:
            print('QUANTIDADE INVÁLIDA! DIGITE NOVAMENTE\n')
        else:
            print(
                f'{quantidade_bebida} unidade(s) de {nome_bebida}.\nValor total R${quantidade_bebida * valor_bebida:.2f}\n')
            escolha_cliente.append(valor_bebida * quantidade_bebida)
            qtd_cont_b = False
    valor_total = sum(escolha_cliente)
    print(f'Valor total do pedido: R${valor_total:.2f}')

    qtd_cont_c = True
    while qtd_cont_c:
        if valor_total < 100:
            print('***ABAIXO DE R$100 NÃO HÁ A POSSIBILIDADE DE DESCONTO OU PARCELAMENTO***')
            qtd_cont_c = False  # condição para encerrar a repetição
        else:
            form_pagamento = int(input(f'***QUAL A FORMA DE PAGAMENTO?***\n1- DINHEIRO\n2- PIX\n3- DÉBITO\n4- CRÉDITO\n'))
            if form_pagamento == 4:
                if valor_total < 150:
                    print(f'Não há desconto para essa forma de pagamento!\n')
                    print(f'O valor de {valor_total:.2f} pode parcelado em 2 vezes\n2 Parcelas de R${(valor_total/2):.2f}')
                    qtd_cont_c = False
                else:
                    print(f'Não há desconto para essa forma de pagamento!\n')
                    print(f'O valor de {valor_total:.2f} pode parcelado no máximo em 3 vezes\n3 Parcelas de R${(valor_total/3):.2f}')
                    qtd_cont_c = False
            elif form_pagamento in [1, 2, 3]:
                print(f'R${valor_total:.2f}\nDesconto de 5% \n*** VALOR TOTAL DO PEDIDO => R${valor_total - (valor_total*5/100)}')
                qtd_cont_c = False
            else:
                print('***CÓDIGO INVÁLIDO***\nDIGITE NOVAMENTE\n')
    escolha_cont = False