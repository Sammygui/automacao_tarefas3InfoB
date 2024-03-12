'''
 crie um programa que recebe 2 numeros reais como entrada e um operador matematico.
 De acordo com o operador matemático fornecido o programa deve calcular e apresentar o resultado.
 '''

'''numero1 = float(input("insira o primeiro numero:"))

numero2 = float(input("insira o sefundo numero"))

op = input("insira operação matemática")

if op == '*' :
 resultado = numero1 *numero2

 
elif op == '/':
resultado = numero1 / numero2

elif op == '+':
resultado = numero1 + numero2

else op == '-'
resultado = numero1 - numero2

print("resultado é:" , resultado) '''



#Entrada
n1 = float(input("digite um numero"))
n2 = float(input("digite um numero"))
op = input("digite um operador")

#processamento

if op == '*' :
    resultado = n1 * n2
    print("resultado é:" , resultado) 
elif op == '+':
    resultado = n1 + n2
    print("resultado é:" , resultado)
elif op == '-':
    resultado = n1 - n2
    print("resultado é:" , resultado)
elif op == '/' :
    resultado = n1 / n2
    print("resultado é:" , resultado)
else:
    print ("invalido")