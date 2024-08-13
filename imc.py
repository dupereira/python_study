# cálculo de imc: esse programa deve receber um peso e uma altura e retornar para o usuário o valor do imc
peso = int(input("Peso: "))
altura = float(input("Altura: ").replace(",","."))
divisao = peso / (altura ** 2)
print(f"O resultado do seu cálculo de IMC é de {divisao:.2f}")