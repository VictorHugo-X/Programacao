'''soma = 0
for i in range(1,51):
    num = int(input("informe um valor: "))
    soma = soma + num
    media = soma / i
    print(media)'''    #atividade 1



'''soma = 0
for i in range(1,101):
    num = int(input("informe um numero: "))
    if soma < num:
       soma = num
print(soma)"'         #atividade2




''soma = 0
ponto = 0
for i in range(1,51):
    num = float(input("digite um numero: "))
    if num > 0:
        soma += num
        ponto += 1
    if ponto > 0:
        media = soma /i
        print ("soma dos numero positivos", soma)
        print ("media dos numeros positivos",media)'''    #ativade3
    


'''soma = 0
ponto = 0
for i in range(1,101):
 num = int(input("informe um numero:"))
if 10 <= num <= 20:
        soma += 1
else:
        ponto += 1
        print("numero intervalo 10,20",soma)
        print("numero fora do intervalo",ponto)'''   #atividade4


'''maiorp = 0
menorp = float("inf")
maiorA = 0
menorA = float("inf")
maiori = 0 
menori = float("inf")
for i in range (2):
    print(f"inferme um peso {i + 1}:")
    p = float(input("seu peso: "))
    i = float(input("sua idade: "))
    a = float(input("ponhe sua altura: "))
    if p > maiorp:
            maiorp = p
    if p < menorp:
            menorp = p
    if i > maiori:
            maiori + i
    if i < menori:
            menori = i    
    if a > maiorA:
            maiorA = a
    if a < menorA:
            menorA = a
print(f"maior peso:{maiorp} ")  
print(f"menor peso:{menorp} kg")
print(f"maior altura:{maiorA} m")  
print(f"menor altura:{menorA} m")
print(f"maior idade:{maiori} anos")
print(f"menor idade:{menori} anos") '''    #atividade5





'''soma = 0
valor = 0
for i in range(1,6):
    num = int(input("informe um numero: "))
    if  num <= 0:
         soma = soma + 1
else:
        valor = valor + 1
print("numeros negativos são:",soma)'''   #ativiade6