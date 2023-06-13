#importando de uma das milhares de bibliotecas do Python
import random

#Função que recebe os limites e garante que nenhum número se repita
def gerador_numero (limite_inferior, limite_superior):
    numeros_existentes = set()

# Função que é o executável do programa, trazendo o número a partir do momento que a tecla "X" é pressionada
    while True:
        numero = random.randint(limite_inferior, limite_superior)
        if numero not in numeros_existentes:
            numeros_existentes.add(numero)
            return numero

#Loop que garante a execução até que o usuário decida encerrar o programa
def main ():
    while True:
        tecla = input("Pressione a tecla 'X' para selecionar um número. Pressione qualquer outra tecla para sair:")
        if tecla.upper() == "X":
            numero_unico = gerador_numero(1, 79)
            print("O número selecionado é:", numero_unico)
        else:
            break

#Estrutura que permite tanto execução no main quanto em outro módulo
if __name__ == "__main__":
    main()