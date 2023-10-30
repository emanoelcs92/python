#Ler 5 notas e informar a média 

soma_notas = 0

for i in range(5):
    nota = float(input(f'Digite a {i+1}ª nota: '))
    soma_notas += nota
media = soma_notas / 5

