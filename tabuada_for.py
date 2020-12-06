valor = int(input('Digite um número para saber a tabuada: '))
c = 0
print('-' * 18)
print('Tabuada de {}'.format(valor))
print('-' * 18)
for c in range(1,11):
  print('{} X {} = {}'.format(c, valor, (c * valor)))
  c = c + 1
