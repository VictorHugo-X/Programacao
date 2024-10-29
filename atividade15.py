numero = int(input("informe um valor:"))
if numero > 1:
    for i in range(2, numero):
     if (numero % i) == 0:
        print(numero,"não é primo")
        break
    else:
         print(numero,"é primo.")
else:
    print(numero,"não e primo.")