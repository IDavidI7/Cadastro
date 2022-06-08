#Primeiro fazer com que os nomes e as senhas sejam salvas na lista de nome e sennha.
#Se ao cadastrar ja estiver o nome outra pessoa cadastrada, erro de cadastro, e tentativa para inserir outro nome.
import os
nome = []
senha = []
while True:
    print('-'*40)
    print(f'{"Tela de cadastro":^40}')
    print('-' * 40)
    dados_nome=(input('Nome: '))
    while dados_nome in nome or dados_nome == '':
        dados_nome=(input('opção inválida ou nome já existente! Tente outro: ').strip())
    dados_senha=(input('Senha: ').strip())
    while dados_senha == '':
        dados_senha = input('opção inválida, digite uma senha: ')
    nome.append(dados_nome)
    senha.append(dados_senha)
    opcao = input('Cadastrar mais alguem? [S/N] ').strip().upper()
    while opcao != 'S' and opcao != 'N':
        opcao = input('Opção inválida! Cadastrar mais alguem? [S/N] ').strip().upper()
    if opcao == 'N':
        break
    os.system('cls||clear')
#Fazer com que o usuário consiga fazer o login depois de se cadastrar.
#3 tentativas.

nome_login = ''
senha_login = ''
print('-' * 40)
print(f'{"Login":^40}')
print('-' * 40)
for login in range(3):
    nome_login = input('Digite seu nome: ').strip()
    senha_login = input('Digite sua senha: ').strip()
    if nome_login not in nome or senha_login not in senha:
        print('Nome e/ou senha inválidos!')
    if nome_login in nome and senha_login in senha:
        print(f'Bem vindo {nome_login}!')
        break
if nome_login not in nome and senha_login not in senha:
    print('Você excedeu o número de tentativas, tente novamente mais tarde.')
