def get_birthday():
    dia = input('Dia: ')
    mês = input('Mês: ')
    ano = input('Ano: ')
    resposta = input(f'Você nasceu no dia {dia} de {mês} de {ano}. Correto?(SIM/NAO): ')

    if resposta.lower() == "sim":
        print("Obrigada por confirmar. Em breve você será redirecionado.")
    elif resposta.lower() == "nao":
        print("Desculpa, pode me dizer novamente?")
        get_birthday()
    else:
        print("Resposta incorreta. Reiniciando o programa.")
        get_birthday()

get_birthday()