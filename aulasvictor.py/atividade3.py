soma = 0
ponto = 0
for i in range(1,5):
    num = float(input("digite um numero: "))
    if num > 0:
        soma += num
        ponto += 1
    if ponto > 0:
        media = soma /i
        print ("soma dos numero positivos", soma)
        print ("media dos numeros positivos",media)
