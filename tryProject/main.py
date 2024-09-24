#Try & Except & Else & Finally
from datetime import date
import random

quantidadeTeste = 0

#Define o número da sorte
numeroSorte = random.uniform(1, 100)
print(numeroSorte)

#Número da sorte e tratamento
while True:
    numero = input("Insira um número de 1 à 100: ")
    try:
        if "," in numero:
            print("Para especificar números decimais, utilize ponto '.'")
        numero = float(numero)
        if 1 <= numero <= 100:
            print(f"Número válido: {numero}")
            break
        else:
            print("O número deve estar entre 1 e 100.")
    except ValueError:
        print("Erro: Entrada inválida.")
    except:
        print("Erro não mapeado.")
    finally:
        print("-------")
        quantidadeTeste += 1
        dataAtual = date.today()
        print(f"Log {dataAtual} Tentativa de Input: {quantidadeTeste}")
        if numero == numeroSorte:
            print(f"Parabéns, você acertou o número da sorte é: {numeroSorte}")
        else:
            print("Não foi dessa vez!")
        print("-------")

