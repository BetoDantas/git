usuário, passe = 'name', 'password'

print("\n\nSeja bem-vindo!")
login, senha, var = input("\nDigite seu Login: "), input("\nDigite sua senha: "), 0

if login != usuário and senha == passe:
    while login != usuário:
        print("\nLogin Inválido!")
        print("{} Tentativas restantes".format(3-var))
        login = input("Digite seu Login Novamente: ")
        var=var+1
        if var == 3:
            break

elif senha != passe and login == usuário:
    while senha != passe:
        print("\nSenha Inválida!")
        print("{} Tentativas restantes".format(3-var))
        senha = input("Digite sua Senha Novamente: ")
        var=var+1
        if var == 3:
            break

else:
    while login != usuário or senha != passe:
        print("\nLogin e Senha Inválidos")
        print("{} Tentativas restantes".format(3-var))
        login, senha = input("Digite seu Login Novamente: "), input("\nDigite sua senha Novamente: ")
        var=var+1
        if var == 3:
            break
if var<3:
    print("\nSeja Bem-Vindo Mestre !")
else:
    print("\nTente novamente outra vez...")