bonus = 0
for i in range(2):
    nome = input("informe o nome: ")
    endereço = input("informe o local: ")
    compras = float(input("digite valor das compras: "))
    if (compras <= 50.000):
     bonus = compras * 1.10 
     print(' seu bonus é de',bonus)
     print(nome)
     print(endereço)
     print(compras)
else:
    bonus = compras  * 1.15
    print(' seu bonus é de',bonus)
    print(nome)
    print(endereço)
    print(compras)