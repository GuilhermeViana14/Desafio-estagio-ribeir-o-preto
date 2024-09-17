def verificar_letra_a(string):
    
    contador = string.lower().count('a')
    
    if contador > 0:
        print(f"a letra A aparece {contador} vezes na string.")
        
    else:
        print(f"A letra A nao foi encontrada na string.")
        
def main(): 
    
    string = input("Informe uma string: ")
    
    verificar_letra_a(string)
    
    
if __name__ == "__main__"
    main()