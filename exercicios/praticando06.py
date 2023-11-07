#Criando um programa para facilitar a conversão de número decimal em bits


decimal = int(input('Digite o número decimal: ')) #variavel que receberá o numero decimal 

binario = bin(decimal) # convertendo para binário
binario = binario[2:] # removendo o prefixo 'ob' 
print(binario) # imprimindo o resultado
