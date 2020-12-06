valor = int(input('Digite um número para saber a tabuada: '))
c = 1
n1=int(input("Número inicial: "))
n2=int(input("Número final: "))
print('-' * 18)
print('Tabuada de {}'.format(valor))
print('-' * 18)
print("Vou fazer a tabuada de {} começando em {} e terminando em {}: ".format(valor, n1, n2))
while(n1 <= n2):
  print('{} X {} = {}'.format(n1, valor, (n1 * valor)))
  n1 = n1 + 1