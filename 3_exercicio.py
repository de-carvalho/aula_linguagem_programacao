frase = input("Digite uma frase: ")

carac1 = input("Digite o caractere para ser substituido: ")
carac2 = input("Digite um novo caractere: ")

contador = 0
nova_frase = ""

for i in frase:
    if i.lower() == carac1.lower():
        nova_frase += carac2
        contador += 1
    else:
        nova_frase += i

print(f"frase modificado: {nova_frase}")
print(f"Quantidade de substituições: {contador}")
