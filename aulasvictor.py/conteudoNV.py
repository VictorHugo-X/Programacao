'''i = 0
while (i<3):
    i += 1
    nome = str(input("informe o nome: "))'''

# faça um programa que receba a idade altura e o peso de 25 pessoas e mostre:
#a quantidade de pessoas com idade superior a 50 anos
'''contador = 0
i = 0
while(i<25):
    i+=1
     idade = int(input("informe a idade: "))
     altura = float(input("informe altura: "))
     peso = float(input("informe o peso: "))
     if idade >50:
        contador += 1
print(contador)'''
 
 
 #atividade 1

'''n1 = 0
n3 = 0
n2 = 0
s = 0
i = 1
while(i>0):
    valor = int(input("informe um numero: "))
    if  valor>0 and valor<25:
             s = s + 1
    if  valor > 26 and valor< 50:
             n1 = n1 + 1
    if valor > 51 and valor < 75:
             n2 = n2 + 1
    if valor > 76 and valor < 100:
             n3 = n3 + 1
    if valor < 0:
        i=-1
    
print(" os numero tem:")
print(s,n1,n2,n3)'''



#atividade2
'''i = 0
joao = 0
jose = 0
maria = 0
meunego = 0
votoembranco = 0
votonulo = 0

while(i<2):
     num = int(input("informe um candidato :"))
     if  num == 1:
        jose += 1 
     if num == 2:
        joao += 1
     if num == 3:
        maria += 1
     if num == 4:
        meunego += 1
     if num == 5:
        votoembranco += 1
     if num == 6:
        votonulo += 1

     print('FAZ O L')
     i=7
     total = jose + joao + maria + meunego
print("o total de votos para josé",jose)
print("total de votos para joao",joao)
print("total de votos para maria ",maria)
print("total de votos para meunego",meunego)
print("total de votos brandos",votoembranco)
print("total de votos nulos",votonulo)'''





i = 0
rj = 0
bh = 0
sc = 0
while(i>1):
   cidade = str(input("informe: "))
   if cidade == 'rj':
     rj += 1
   if cidade == 'bh':
     bh += 1
   if cidade == 'sc':
     sc += 1
   if cidade == "fim":
     i=2
print("pessoas do rio é",rj)
print("pessoas  de belo horizonte e",bh)
print("pessoas de santa catarina e",sc)