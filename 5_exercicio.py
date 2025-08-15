texto = input("Digite uma palavra ou frase: ")

texto_limpo = texto.replace(" ", "").lower()

invertido = ""

for i in texto_limpo:
    invertido = i + invertido

if texto_limpo == invertido:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")
