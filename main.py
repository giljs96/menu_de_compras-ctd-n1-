print('Opções de Produto\n1- hambúrguer -- R$10.50\n2- cachorro quente -- R$8.50\n3- salgadinho -- R$6.80 \n4- prato feito -- R$20.50')
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
print(f'O valor do {nome_lanche} é de {valor_lanche:.2f}')
print('Opções de Produto\n1- água\n2- refrigerante\n3-refresco\n4-suco')
escolha_bebida = int(input('Digite o código do produto '))
valor_bebida = 0