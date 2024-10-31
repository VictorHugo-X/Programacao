#Escreva um algoritmo que deverá realizar a funçao de  pedido de pizza que calcule o valor total de acordo com os ingredientes e o tamanho escolhido.
#Deverá apresentar as seguintes perguntas:
#- tamanho da pizza: pequena R$20,média-R$30,grande-R$40.
#o programa deverá perguntar se deseja adicionar ingredientes extras como:calabresa,mussarela,tomate,cebola,bacon.
#cada ingrediente extra tem o valor de R$ 5,00. por fim, se deseja beber algum refrigerante valor de R$8,00
soma = 0
pizza = str(input("Qual tamanho da pizza que voce gostaria?"))
if pizza == "pequena":
       soma+=20
if pizza == "media":
       soma +=30
if pizza == "grande":
     soma += 40
ingre = ['calabresa','mussarela','tomate','cebola','bacon']
for i in range(1): 
 extra = str(input("Deseja adicionar algum ingrediente extra?"))
 if extra == "calabresa":
      print ('calabresa')
      soma += 5
 if extra == "mussarela":
      print('mussarela')
      soma += 5
 if extra == "tomate":
      print('tomate')
      soma += 5
 if extra == "cebola":
      print('cebola')
      soma += 5
 if extra == "bacon":
      print('bacon')
      soma += 5
bebida = str(input("Deseja beber um refri?"))
if bebida == 'sim':
    soma += 8
    print(soma)
