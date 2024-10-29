def gerarFibonacci():
    a,b=0,1
    fibonacciSequence=[]

    while a <= 700:
       fibonacciSequence.append(a)
       a, b = b, a + b
    return fibonacciSequence
resultado = gerarFibonacci()
print(resultado)
