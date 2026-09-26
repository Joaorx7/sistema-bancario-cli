print("BANCO VIRTUAL")

users = {
    "12345678900": {
        "nome": "João Gabriel",
        "pin": "1234",
        'saldo': 1500.00,
        'historico': [],
    }
}

def divisao():

    print("-------------------------------")

def login():
    while True:
        print("LOGIN")
        cpf_verify = input("Digite se cpf (sem ponto e traço): ")

        if not (cpf_verify.isdigit() and len(cpf_verify) == 11):
            print("CPF inválido! Digite apenas 11 números.")
            continue    

        password_verify = input("Digite seu PIN de 4 digitos: ")

        if not (password_verify.isdigit() and len(password_verify) == 4):
            print("PIN inválido! Digite apenas 4 números.")
            continue

        if cpf_verify in users:
            if password_verify == users[cpf_verify]["pin"]:
                "Acesso permitido"
                divisao()
                return cpf_verify
                break
            else:
                print("Senha invalida, tente novamente!")
        else:
            print("Usuario não cadastrado!")
            cadastro = input("Deseja se cadastrar? digite S ou N: ")
            divisao()
            cadastro = cadastro.upper()

            if cadastro == "S":
                print("Processo de Cadastro")

                nome = input("Digite seu nome: ")
                cpf = input("Digite seu CPF: ")

                if not (cpf.isdigit() and len(cpf) == 11):
                    print("CPF inválido! Digite apenas 11 números.")
                    continue 

                pin = input("Digite um PIN para o seu acesso: ")
                divisao()

                users[cpf] = {"nome": nome, "pin": pin, 'saldo': 0, 'historico': []}
                print("Conta criada com sucesso")
                print(("Acessando Menu inicial"))
                divisao()
                return cpf
                break

            else:
                quit()


cpf = login()


def consultarSaldo():
    print(f"O seu saldo é de {users[cpf]['saldo']}")
    divisao()

    if users[cpf]['historico'] == []:
        print("Você não tem historico de extrato")
        divisao()
    else:
        for transacao in users[cpf]['historico']:
            print(transacao)
        divisao()


def deposito():
    while True:
        try:
            deposito = float(input("Digite o valor que deseja depositar na conta: "))
            divisao()
            if deposito > 0:
                users[cpf]['saldo'] = users[cpf]['saldo'] + deposito
                users[cpf]['historico'].append(f"Deposito de R${deposito:.2f} confirmado")
                divisao()
                break

            else:
                print("Valor invalido, Tente novamente")
                divisao()

        except ValueError:

            print("Por favor, digite apenas valores válidos!")
            divisao()


def sacar():
    while True:
        try:
            valor_saque = float(input("Digite o valor que desejar sacar: "))

            divisao()

            if valor_saque > 0:
                if valor_saque <= users[cpf]['saldo'] and valor_saque > 0:
                    print("SAQUE REALIZADO COM SUCESSO")
                    divisao()
                    users[cpf]['saldo'] = users[cpf]['saldo'] - valor_saque
                    users[cpf]['historico'].append(f"Saque de R${valor_saque:.2f} confirmado")
                else:
                    print("Valor insuficiente, voltando pra tela inicial!")
                    divisao()

                break
            else:
                print("Valor invalido")
                divisao()
        except:
            print("Por favor, digite apenas valores válidos!")
            divisao()


def pix():
    while True:
        while True:
            cpf_destino = input("Digite o cpf de destino para realização do PIX (APENAS OS NUMEROS): ")
            if not (cpf_destino.isdigit() and len(cpf_destino) == 11):
                print("CPF invalido tente novamente")
                continue
            break

        divisao()

        if cpf_destino == cpf:
            print("Não é possivel realizar um PIX para si mesmo")
            break
        elif cpf_destino in users:
            try:
                valor_pix = float(input(f"Qual valor você deseja enviar para o cpf {cpf_destino}: "))
                divisao()
                if valor_pix <= users[cpf]['saldo'] and valor_pix > 0:
                    users[cpf_destino]['saldo'] = users[cpf_destino]['saldo'] + valor_pix
                    users[cpf_destino]['historico'].append(f"PIX recebido no valor de R${valor_pix:.2f}")
                    users[cpf]['saldo'] = users[cpf]['saldo'] - valor_pix
                    users[cpf]['historico'].append(f"PIX enviado no valor de R${valor_pix:.2f}")

                else:
                    print("Valor insuficiente ou invalido, voltando para o Menu inicial")
                    divisao()
                    
                break
            except ValueError:
                print("Insira um valor válido")
                divisao()

        else:
            print("CPF não encontrado, voltando para o Menu")
            divisao()


while True:

    print("MENU BANCO")
    divisao()
    print(
        "1 - Consultar Saldo e Extrato \n2 - Depositar \n3 - Sacar \n4 - Transferir(PIX) \n5 - Sair da Conta"
    )
    divisao()
    try:
        opcao = input("Digite a opção que deseja realizar: ")
        opcao = float(opcao)
        divisao()

        if opcao == 1:

            consultarSaldo()

        elif opcao == 2:

            deposito()

        elif opcao == 3:

            sacar()

        elif opcao == 4:

            pix()

        elif opcao == 5:
            print("Voltando pra tela de Login")
            divisao()
            cpf = login()

        else:
            print("Opção invalida, Tente novamente")
            divisao()

    except ValueError:

        print("Por favor, digite apenas números válidos!")
        divisao()