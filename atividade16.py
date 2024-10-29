mais = 0 
menos = 10
vmenos = 0
vmais = 0
for i in range(2):
    numero = int(input("digite seu numero: "))
    altura = float(input("digite sua altura: "))
    if altura > mais:
        mais = altura
        vmais = numero
    if altura < menos:
        menos = altura
        vmenos = numero
print(f"aluno mais alto",[mais],[vmais])
print(f"aluno mais baixo",[menos],[vmenos])