nome = str(input("informe seu nome:"))
victor = len(nome)
if victor > 3:
   idade = int(input("informe sua idade: "))
   if idade > 0 and idade < 150:
        salario = float(input("informe seu salario. "))
        if salario > 0:
            sexo = str(input("informe seu sexo:"))
            if sexo == "m" or sexo =="f":
                civil = str(input("informe seu estado civil: "))
                if civil == "solteiro" or civil == "casado"  or civil == "viuvo" or civil == "deixado":
                    print("valido")
                else:
                    print("invalido")