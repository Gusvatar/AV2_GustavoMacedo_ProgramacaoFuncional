import os

read_file = lambda file_name: {line.split()[0]: line.split()[1] for line in open(file_name, "r").readlines()} if os.path.exists(file_name) else {}

write_to_file = lambda file_name, login, senha: open(file_name, "a").writelines(f"{login} {senha}\n")

cadastrar_login = lambda file_name: (lambda login, senha: write_to_file(file_name, login, senha))(input("Digite seu login: "), input("Digite sua senha: "))

validar_login = lambda file_name: (lambda logins, user_login, user_pass: print("SUCESSO") if user_login in logins and logins[user_login] == user_pass else print("FRACASSO"))(read_file(file_name), input("Digite seu login: "), input("Digite sua senha: "))

telaLogin = lambda: (lambda choice: cadastrar_login("logins.txt") if choice == "I" else validar_login("logins.txt") if choice == "II" else print("Opção inválida"))(input("Escolha uma opção:\n(I) Cadastrar login\n(II) Fazer login\n"))

telaLogin()
