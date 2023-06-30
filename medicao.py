"""
Script utilizado para gerar os gráficos que estão no artigo.
"""

import BMH, shift, parcial
import matplotlib.pyplot as plt
import random
import time

iteracoes = 1000000
alfabeto = "abcdef"
tempos = []


def gerar_texto(tamanho):
    texto = ""
    for _ in range(tamanho):
        texto += random.choice(alfabeto)
    return texto


tam_padrao = 10
# Primeiro BMH
for tam_texto in range(100, iteracoes, 100):
    texto = gerar_texto(tam_texto)
    padrao = gerar_texto(tam_padrao)
    inicio = time.time()
    BMH.BMH(texto, padrao)
    tempos.append(time.time() - inicio)

x = [x for x in range(100, iteracoes, 100)]
y = tempos
print(tempos)
plt.plot(x, y)
plt.show()
