#Imprimir a tabuada do núm'ero 3 (3 x 1 = 1 - 3 x 10 = 30)

numero = int(input('Digite um número para tabuada: '))

for i in range(1,10):
    resultado = numero * i
    print(f'{numero} x {i} = {resultado}')
    print('----------')
