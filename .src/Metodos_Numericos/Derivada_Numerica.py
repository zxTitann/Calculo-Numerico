#Criando arquivo para implementar a aproximação numérica da derivada
def derive(f, x): #Inserindo a função e o ponto que queremos derivar
    h = 1e-6 #Definindo o tamanho do passo. o 1e-6 é 0.000001 onde o 1e-3 seria 0.001 e o 1e-2 seria 0.01
    resultado = (f(x + h) - f(x - h)) / (2 * h) #Definindo a derivada
    return resultado, h


#Testando a funcao
resultado, h = derive(lambda x: x**2, 2)
print("///////////////////////////")
print(f"Derivada de x^2 em x=2: {resultado}")
print(f"Tamanho do passo: {h}")
print("///////////////////////////")