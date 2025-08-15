frase = input("Digite uma frase: ")
vogais = "aeiouAEIOU"
contador = 0

for i in frase:
    if i in vogais:
        contador += 1

print(f"A frase tem {contador} vogais.")
