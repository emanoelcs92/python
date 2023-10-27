#Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem, utilizando um automóvel que faz 12 Km por litro. Para obter o #cálculo, o usuário deve fornecer o tempo gasto na viagem e a velocidade média durante ela. Desta forma, será possível obter a distância #percorrida com a fórmula DISTANCIA = TEMPO * VELOCIDADE. Tendo o valor na viagem, a distância percorrida e a quantidade de litros utilizada na viagem

tempo = float(input('Digite o tempo gasto na viagem: '))
velocidade = float(input('Digite a velocidade do veiculo: '))
distancia = tempo*velocidade
consulmo_por_litro = 12
litros_gastos = distancia/consulmo_por_litro
print(litros_gastos)
