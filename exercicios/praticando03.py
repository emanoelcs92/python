#Calcular a média de um aluno que cursou a disciplina de Programação I, a partir da leitura das notas M1, M2 e M3; passando por um cálculo da média aritmética. Após a média calculada, devemos anunciar se o aluno foi aprovado, reprovado ou pegou exame
#- Se a média estiver entre 0.0 e 4.0, o aluno está reprovado
#- Se a média estiver entre 4.1 e 6.0, o aluno pegou exame
#- Se a média for maior do que 6.0, o aluno está aprovado
#- Se o aluno pegou exame, deve ser lida a nota do exame. Se a nota do exame for maior do que 6.0, está aprovado, senão; está reprovado

m1 = float(input('Digite a nota da unidade I: '))
m2 = float(input('Digite a nota da unidade II: '))
m3 = float(input('Digite a nota da unidade III: '))
media = (m1+m2+m3)/3

if media >= 0.0 and media <= 4.0:
    print('Aluno Reprovado!')
elif media >= 4.1 and media <= 6.0:
    print('Pegou exame!')
    nota_do_exame = float(input('Digite a nota do exame: '))
    if nota_do_exame > 6.0:
        print('Aluno aprovado!')
    else:
        print('Aluno reprovado!')
else:
    print('Aluno Aprovado!')

