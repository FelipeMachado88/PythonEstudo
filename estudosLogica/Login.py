senha = input ("Digite sua senha: ")
if (senha == "admin"):
    print("Olá, Administrador!")
elif (senha == "usuario"):
    print("Olá, usuário!")
else:
    print("Acesso negado. Verifique sua senha e tente novamente.")