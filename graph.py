#----importação das bibliotecas----#
import matplotlib.pyplot as plt
import numpy as np
#--------------config--------------#
fig = plt.figure()
fig.set_facecolor('lightblue') #cor
ax = fig.subplots()
ax.set_xlabel('Tempo (s)')
ax.set_title('Gráfico de Ordem da Reação')
#-------------variáveis------------#
x = []; y = []
#--------------inputs--------------#
inputs = int(input("Quantos inputs quer carregar?\n=> "))
for n in range(0, inputs): x.append(float(input(f"Digite X{n}\n=> ")))
for n in range(0, inputs): y.append(float(input(f"Digite Y{n}\n=> ")))
#x = [0, 50, 100, 200, 300]
#y = [0.01, 0.00787, 0.00649, 0.00481, 0.00380]
res = int(input("Ordem 1 ou 2?\n=> ")) #ordem da reação
if res == 1: 
    for n in range(0, inputs): y[n] = np.log(y[n]) #passa os valores para ln[A]
    ax.set_ylabel('ln[NO2]')
elif res == 2:
    for n in range(0, inputs): y[n] = 1/y[n] #passa os valores para 1/[A]
    ax.set_ylabel('1/[NO2]')
#--------------plotagem de gráfico--------------#
ax.plot(x, y)
plt.show()