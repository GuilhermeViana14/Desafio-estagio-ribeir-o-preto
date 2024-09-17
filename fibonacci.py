def Calculo_fibonacci(n):
    
    a, b = 0, 1
    while a<=n:
        if a == n:
            return true
        a, b = b, a + b
    return false 


def main():
    numero = int(input("Coloque seu numero: "))

    if Calculo_fibonacci(numero):
        print(f"o Numero {numero} pertence a senquencia de fibonacci.")
    else: 
        print(f"O Numero {numero} não pertence a sequencia de fibonacci.")
        
        
        
if __name__ == "__main__":
    main()