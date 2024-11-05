try:
    file = open("Seguranca.txt", 'r', encoding='utf-8')

    user = file.readline().strip('\n')
    senha = file.readline().strip('\n')
except FileNotFoundError:
    print("Arquivo não encontrado")

print("Usuário: ")
u_input = input().strip('\n')
print(u_input)

print("Senha: ")
u_senha = input().strip('\n')
print(u_senha)

if(u_input == user):
    if(senha == u_senha):
        print("Logado com sucesso")
    else:
        print("Senha incorreta")
else:
    print("Usuário inexistente")