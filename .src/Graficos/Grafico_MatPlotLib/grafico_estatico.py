import matplotlib.pyplot as plt #importando a biblioteca
x = [1, 2, 3, 4, 5]   #definindo o eixo x
y = [5, 10, 15, 20, 25]   #definindo o eixo y
plt.plot(x, y, label="Linha sera que é mesmo?")   #definindo a linha e o label da mesma 
plt.scatter(x, y, color="blue", label="Pontos e é ponto memo?") #definindo os pontos
plt.title("Gráfico Estático testando eeeeeeeeee") #definindo o título
plt.legend() #definindo a legenda
plt.show() #mostrando o gráfico