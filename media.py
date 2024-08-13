#cálculo de media: esse programa deve receber quatro notas e retornar uma média
def remove_comma(n: str):
    return n.replace(",",".")

nota_1 = float(remove_comma(input("Nota 1: ")))
nota_2 = float(remove_comma(input("Nota 2: ")))
nota_3 = float(remove_comma(input("Nota 3: ")))
nota_4 = float(remove_comma(input("Nota 4: ")))
media = (nota_1 + nota_2 + nota_3 + nota_4) / 4
print(f"O seu resultado de média é de {media:.2f}.")

if media >= 7.0:
    print("Parabéns (Congratulations). Você está aprovade no Duda's Curso.")
else:
    print("Ora ora, parece que você faltou a algumas aulas, não? Mais sorte na próxima.")