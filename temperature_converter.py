# Esse exercicio recebe uma temperatura e uma medida e converte dependendo da recebida (F/C).
temperatura = float(input("Temperatura: ").replace(",","."))
medida = input("Insira para qual medida você quer converter (F/C): ").upper()

if medida == "F":
    resultado = temperatura * 9 / 5 + 32
    resposta = f"A conversão da medida de celsius para fahrenheit foi concluída. Seu resultado é {resultado:.2f}"
elif medida == "C":
    resultado = (temperatura - 32) * 5 / 9
    resposta = f"A conversão da medida de fahrenheit para celsius foi concluída. Seu resultado é {resultado:.2f}"
else:
    resposta = "ERROR 404 NOT FOUND"

print(resposta)