maiorp = 0
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
print(f"menor idade:{menori} anos")           
            