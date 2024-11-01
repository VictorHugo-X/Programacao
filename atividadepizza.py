#Escreva um algoritmo que deverá realizar a funçao de  pedido de pizza que calcule o valor total de acordo com os ingredientes e o tamanho escolhido.
#Deverá apresentar as seguintes perguntas:
#- tamanho da pizza: pequena R$20,média-R$30,grande-R$40.
#o programa deverá perguntar se deseja adicionar ingredientes extras como:calabresa,mussarela,tomate,cebola,bacon.
#cada ingrediente extra tem o valor de R$ 5,00. por fim, se deseja beber algum refrigerante valor de R$8,00
pedidos = []
quantidadepedidos = 0
soma = 0
while True:
    nome = str(input("Olá boa noite,bem vindo a Pizzaria do Sr ekko.Qual será sua escolha de hoje? "))
    pizza = str(input("Escolha o tamanho da pizza (pequena, média, grande:"))
    if pizza == "pequena":
       soma+=20
    if pizza == "media":
       soma +=30
    if pizza == "grande":
        soma += 40
    ingre = ['calabresa','mussarela','tomate','cebola','bacon']
    
    extra = input("Deseja adicionar um ingrediente extra temos (calabresa, mussarela, tomate, cebola, bacon)? (sim/não): ")
    if  extra == 'sim':
        ingrediente = int(input("Quantos ingredientes extras deseja adicionar? "))
        soma += ingrediente * 5
    refrigerante = input("Deseja beber um refrigerante? (sim/não):")
    if refrigerante == 'sim':
        soma += 8
    
    pedidos.append(soma)
    quantidadepedidos += 1
    print(f"Valor do pedido: R${soma:.2f}")

    continuar = input("Deseja fazer outro pedido? (sim/não): ")
    if continuar != 'sim':
        break

if pedidos:
    print(f"Pedido mais caro: R${max(pedidos):.2f}")
    print(f"Pedido mais baixo: R${min(pedidos):.2f}")
    print(f"Quantidade de pedidos realizados: {quantidadepedidos}")
else:
    print("Nenhum pedido foi realizado.")

