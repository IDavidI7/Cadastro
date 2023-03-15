import os

class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password

class UserDatabase:
    def __init__(self):
        self.users = []

    def add_user(self, name, password):
        self.users.append(User(name, password))

    def is_valid_user(self, name, password):
        for user in self.users:
            if user.name == name and user.password == password:
                return True
        return False

def register_user(database):
    print('-'*40)
    print(f'{"Tela de cadastro":^40}')
    print('-' * 40)
    while True:
        name = input('Nome: ').strip()
        if name == '':
            print('Nome inválido!')
            continue
        if any(user.name == name for user in database.users):
            print('Nome já existente!')
            continue
        password = input('Senha: ').strip()
        if password == '':
            print('Senha inválida!')
            continue
        database.add_user(name, password)
        opcao = input('Cadastrar mais alguém? [S/N] ').strip().upper()
        while opcao != 'S' and opcao != 'N':
            opcao = input('Opção inválida! Cadastrar mais alguém? [S/N] ').strip().upper()
        if opcao == 'N':
            break
        os.system('cls||clear')

def login(database):
    print('-' * 40)
    print(f'{"Login":^40}')
    print('-' * 40)
    for _ in range(3):
        name = input('Digite seu nome: ').strip()
        password = input('Digite sua senha: ').strip()
        if database.is_valid_user(name, password):
            print(f'Bem-vindo, {name}!')
            return
        print('Nome e/ou senha inválidos!')
    print('Você excedeu o número de tentativas, tente novamente mais tarde.')

def main():
    database = UserDatabase()
    register_user(database)
    login(database)

if __name__ == '__main__':
    main()
