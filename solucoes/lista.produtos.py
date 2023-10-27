# Criando listas de produtos:
import itertools

roupa = ["camiseta","blusao","regata"]
cores = ["preta","branca","cinza"]


combinacoes = list(itertools.product(roupa,cores))
print(combinacoes)
                   
