''' 
as funções são utilizadas para modular o código, ou seja, dividi-lo em partes menores, que podem ser reutilizadas.

estrutura:

def nome_funcao(param1, param2):
   faz algo
   return valor

   exemplos:
   ''' 
#funcao1
def calcularareadotriangulo(base, altura):
    area = (base * altura ) / 2
    return area

#funcao2

def login(usuario, senha):
    if usuario == "adm" and senha == '123':
     return True
    else:
     return False 

#chamar a funca
#print(login("samantha", "123"))
#print(area(22, 10))
