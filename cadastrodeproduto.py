from operator import itemgetter

bd = {}
codigo = 0
while True:
  codigo = codigo + 1
  prod = []
  nome = input("Digite o nome do produto: ")
  prod.append(nome)
  preco = float(input("Digite o preço do produto: "))
  prod.append(preco)
  quantidade = int(input("Digite a quantidade do produto: "))
  prod.append(quantidade)
  bd.update({codigo:prod})
  cont = input("Deseja continuar? [S/N]")
  if cont in "Nn":
    break

lista_sub = []

print("\nProduto ---- Subtotal\n")

for codigo,prod in sorted(bd.items(),key=itemgetter(1)):
  subtotal = (prod[1] * prod[2])
  lista_sub.append(subtotal)
  print("{} ---- {:.2f}".format(prod[0],subtotal,))

total = sum(lista_sub)
print("\nO valor total é: ",total)
