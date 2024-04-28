import datetime
import os
from time import sleep

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

nome_do_usuario = input(f'''{saudacao}! Qual o seu nome?
Digite seu nome: ''').capitalize()
senha = input(f'''Olá {nome_do_usuario}, vamos criar uma senha?
Digite a senha: ''')
os.system('clear')

menu = input(f'''Bem-vindo(a) {nome_do_usuario}!
[1]Cadastrar taxas
[2]Incluir nova venda
[3]Excluir venda (em desenvolvimento)
[4]Fechar caixa
Selecione uma opção: ''')

if menu == '1':
    print('Você selecinou a opção CADASTRAR TAXAS')
    sleep(1)
    numero_de_operadoras = int(input('Digite o número de operadoras que você quer cadastrar: '))
    contador_de_taxas = 0
    while contador_de_taxas < numero_de_operadoras:
        operadora = input(f'Digite o nome da operadora {contador_de_taxas + 1}: ')
        taxa = float(input('Digite a porcentagem da taxa (apenas numeros): '))
        contador_de_taxas += 1
