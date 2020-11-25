a = set('abacate')
b = set('abacaxi')

print(a)
print(b)

print(a-b,'diferença')
print(a|b,'união')
print(a&b,'intercessão')
print(a^b,'diferença simetrica')

# DICIONARIOS

pessoa={'nome':'Joao','idade':25,'cidade':'São Paulo'}
print(pessoa['nome'])
print(pessoa['idade'])
pessoa['pais'] = 'Brasil'
print(pessoa['pais'])
print(pessoa.keys())
print(pessoa.values())


lista=[12,-2,4,8,29,45,78,36,-17,2,12,8,3,3,-52]

print(max(lista),'minimo')
print(min(lista),'maximo')
# entender ocorrencia
n = 0
media = 0
i = 0

while i <= len(lista):
    n = lista[i]
    print(n)
    media  = media + n
    i += 1
print('a media da lista é ',media/i)