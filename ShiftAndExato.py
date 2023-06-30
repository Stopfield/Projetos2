palavra = 'lala'
texto = 'lalala'

def dicionario(palavra):  # função que cria um dicionario, com todas a s letras da palavra, e um lista com as ocorrencias delas
    '''essa função analisa cada caractre da palavra e adiciona uma lsita com quais posições ela ocupa'''
    mat = {}
    for i in palavra:
        ocorrencia = []
        for j in palavra:
            if i == j:
                ocorrencia.append(True)
            else:
                ocorrencia.append(False)
        mat[i] = ocorrencia

    return mat


def bit(ocorrencias, recorrencias):  # aqui pegamos o ocorrencias do caracter, quais posições ele ocupa, na string atual, e quis posições ele ocupa no dicionario
    '''Essa função é responsavel por checar as se os caracteres estão nas devidadas posições da palavra'''
    cont = len(recorrencias) - 1
    resultado = []
    encontrada = 0
    # checamos se o ultimo caracter tambem tem como popsição o ultimo no dicionario
    if ocorrencias[cont] and recorrencias[cont]:
        encontrada = 1  # numero de palavras encontradas após checagem do ultimo bit
        ocorrencias[cont] = False
    cont -= 1  # como já checamos o ultimo decrementamos
    while cont >= 0:  # começamos e ordem decrecente para podemos alterar os valores do indice da frente, se não ele seria zerado
        if ocorrencias[cont] and recorrencias[cont]:
            # caso o caracter esteja batendo com suas posições no dicionario, então increntamos a proxima posição
            ocorrencias[cont+1] = True
        ocorrencias[cont] = False
        cont -= 1
        # decrementamos pois esta posição já passou por analise
    resultado.append(encontrada)
    resultado.append(ocorrencias)
    return resultado  # essa lista retorna uma lista atualizada de valores boleanos após a checagem e o numero de palavras encontradas


def compara(palavra, texto):
    '''a função mais seleciona cada caractere do texto para passar por analise'''
    # primeiro criamos um dicionario com todos os caracteres da plavra e suas recorrencias nela
    dicio = dicionario(palavra)
    tamanho = len(palavra)
    teste = [False for x in range(tamanho)]
    ocorrencias = 0
    for i in texto:
        teste[0] = True
        print(teste, i)
        if dicio.get(i):
            retorno = bit(teste, dicio[i])
            teste = retorno[1]
            ocorrencias += retorno[0]
        else:
            teste = [False for x in range(tamanho)]
    return ocorrencias


print(compara(palavra, texto))
