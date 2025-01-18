import random

ordem = int(input("Qual a ordem da matriz?"))
if ordem >= 2:
  while True:
    M = []
    for i in range(ordem):
      linha = []
      for j in range(ordem):
        num = random.randint(1,10)
        linha.append(num)
      M.append(linha)
    break
  
  dprincipal = []
  dsecundaria = []
  
  for i in range(ordem):
    for j in range(ordem):
      print(M[i][j], end=" ")
      if i == j:
        dprincipal.append(M[i][j])
      if i + j == ordem - 1:
        dsecundaria.append(M[i][j])
    print()
  maiorprincipal = max(dprincipal)
  menorsecundaria = min(dsecundaria)
  media = (maiorprincipal + menorsecundaria) / 2
  print("A média é: ", media)
else:
  print("A ordem deve ser maior que 2")
