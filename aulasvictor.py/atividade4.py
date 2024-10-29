soma = 0
ponto = 0
for i in range(1,101):
 num = int(input("informe um numero:"))
if 10 <= num <= 20:
        soma += 1
else:
        ponto += 1
        print("numero intervalo 10,20",soma)
        print("numero fora do intervalo",ponto)
        