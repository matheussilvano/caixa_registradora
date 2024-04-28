import datetime
import os
from time import sleep

print('Feito por Matheus Silvano')
sleep(1)
os.system('clear')

# Saudação por horário
horario = datetime.datetime.now().hour
manha = -1 < horario < 12
tarde = 11 < horario < 18
noite = 18 < horario < 24
if manha:
    saudacao = 'Bom dia'
elif tarde:
    saudacao = 'Boa tarde'
else:
    saudacao = 'Boa noite'

# Entrada do usuário
nome_do_usuario = input(f'''{saudacao}! Qual o seu nome?
Digite seu nome: ''').capitalize()
os.system('clear')

# Banco de dados
taxas_operadoras = []
vendas = []


while True:

    # Menu principal
    menu = input(f'''Bem-vindo(a) {nome_do_usuario}!
[1]Cadastrar taxas
[2]Incluir nova venda
[3]Fechar caixa
Selecione uma opção: ''')
    os.system('clear')

    # Cadastro de taxas - 1
    if menu == '1':
        print('Você selecinou a opção CADASTRAR TAXAS')
        sleep(1)
        numero_de_operadoras = (input('Digite o número de operadoras que você quer cadastrar: '))
        validar_numero_de_operadoras = numero_de_operadoras.isdigit()
        if validar_numero_de_operadoras:
            int_numero_de_operadoras = int(numero_de_operadoras)
            contador_de_taxas = 0
            while contador_de_taxas < int_numero_de_operadoras:
                operadora = input(f'Digite o nome da operadora {contador_de_taxas + 1}: ').upper()
                taxa = float(input('Digite a porcentagem da taxa (apenas numeros): '))
                taxas_operadoras.append((operadora, taxa))
                contador_de_taxas += 1
                print(f'Operadora {operadora} cadastrada! Taxa de {taxa}%')
                sleep(2)
                os.system('clear')
            print('Todas as operadoras foram cadastradas.')
            sleep(1)
            os.system('clear')
        else:
            print('Opção inválida.')
            sleep(2)
            os.system('clear')

    # Incluir venda - 2
    if menu == '2':
        print('Você selecinou a opção INCLUIR VENDA')
        sleep(1)
        print("Operadoras disponíveis:")
        for i, (operadora, _) in enumerate(taxas_operadoras, start=1):
            print(f"{i}. {operadora}")
        print(f"{len(taxas_operadoras) + 1}. Pix/Dinheiro")
        operadora_escolhida = int(input('Selecione a operadora da venda: '))
        if operadora_escolhida == len(taxas_operadoras) + 1:
            operadora_venda = 'Pix/Dinheiro'
            taxa = 0
        else:
            operadora_venda, taxa = taxas_operadoras[operadora_escolhida - 1]
        print(f'Você selecionou a operadora {operadora_venda}.')
        sleep(1)
        os.system('clear')
        valor_bruto = float(input('Digite o valor da venda (use "." para separar os centavos):'))
        valor_liquido = valor_bruto * (1 - taxa / 100)
        vendas.append((valor_bruto, taxa, valor_liquido))
        os.system('clear')
        print(f'Venda de R${valor_bruto} cadastrada!')
        sleep(0.5)
        print(f'Taxa da máquina: {taxa}%')
        sleep(0.5)
        print(f'Valor líquido: R${valor_liquido:.2f}')
        sleep(2)
        os.system('clear')

    # Fechar caixa - 3
    if menu == '3':
        total_bruto = sum(venda[0] for venda in vendas)
        total_liquido = sum(venda[2] for venda in vendas)
        print("Lista de vendas:")
        for i, venda in enumerate(vendas, start=1):
            valor_bruto, taxa, valor_liquido = venda
            print(f"Venda {i}:")
            print(f"  Valor Bruto: R${valor_bruto:.2f}")
            print(f"  Taxa da Máquina: {taxa}%")
            print(f"  Valor Líquido: R${valor_liquido:.2f}")
            sleep(0.3)
            os.system('clear')
        print(f'TOTAL BRUTO: {total_bruto}')
        print(f'LÍQUIDO À RECEBER: {total_liquido}')
        input('Pressione qualquer tecla para sair: ')
        os.system('clear')
    
