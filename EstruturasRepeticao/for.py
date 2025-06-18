# exemplo de funcionamento de um FOR
texto = input("Digite qualquer frase: ")
vogais = "AEIOU"

for letra in texto:
    if letra.upper() in vogais:
        print(letra, end = "")

# nesse exemplo o FOR faz com que a string seja percorrida printando somente as vogais 