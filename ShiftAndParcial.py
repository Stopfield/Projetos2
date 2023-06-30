palavra = 'lala'
texto = 'lalal2la'



def dicionario(palavra):  # função que cria um dicionario, com todas a s letras da palavra, e um lista com as ocorrencias delas
    '''essa função analisa cada caractre da palavra e adiciona uma lsita com quais posições ela ocupa'''
    mat = {}
    for i in palavra:
        ocorrencia = []
        for j in palavra:  # ele pega um caractere da palavra a compara com todas as outras
            if i == j:
                # as que forem iguais ele marca True na posição
                ocorrencia.append(True)
            else:
                ocorrencia.append(False)  # se não ele marca false
        mat[i] = ocorrencia

    return mat




def bit(ocorrencias, recorrencias):  # aqui pegamos o ocorrencias do caracter, quais posições ele ocupa, na string atual, e quis posições ele ocupa no dicionario
    '''Essa função é responsavel por checar as se os caracteres estão nas devidadas posições da palavra'''
    cont = len(recorrencias) - 1
    resultado = []
    encontrada = 0
    tipo = 0
    # checamos se o ultimo caracter tambem tem como popsição o ultimo no dicionario
    if ocorrencias[cont] and recorrencias[cont]:
        encontrada = 1  # numero de palavras encontradas após checagem do ultimo bit
        tipo = ocorrencias[cont]
    elif ocorrencias[cont] > 1:  # caso o ultimo seja o defeituroso
        encontrada = 1  # numero de palavras encontradas após checagem do ultimo bit
        # retiramos um marcador dele para ser um parcial e adicionamos a resposta
        tipo = ocorrencias[cont] - 1
    ocorrencias[cont] = 0
    cont -= 1  # como já checamos o ultimo decrementamos
    while cont >= 0:  # começamos e ordem decrecente para podemos alterar os valores do indice da frente, se não ele seria zerado
        if ocorrencias[cont] and recorrencias[cont]:
            # caso o caracter esteja batendo com suas posições no dicionario, então increntamos a proxima posição
            ocorrencias[cont+1] = ocorrencias[cont]
        elif (ocorrencias[cont] > 0):
            ocorrencias[cont+1] = ocorrencias[cont] - 1
        ocorrencias[cont] = 0
        cont -= 1
        # decrementamos pois esta posição já passou por analise
    resultado.append(encontrada)
    resultado.append(ocorrencias)
    resultado.append(tipo)
    return resultado  # essa lista retorna uma lista atualizada de valores boleanos após a checagem e o numero de palavras encontradas




def compara(palavra, texto):
    '''a função mais seleciona cada caractere do texto para passar por analise'''
    # essa resposta recebe o numero de ocorrencias as posições e o tipo de cada uma
    resposta = [0]
    # primeiro criamos um dicionario com todos os caracteres da plavra e suas recorrencias nela
    dicio = dicionario(palavra)
    tamanho = len(palavra)
    cLidos = 1  # essa variavel, retorna o numero de caracteres lidos no texto
    teste = [0 for x in range(tamanho)]
    ocorrencias = []  # posições das ocorrencias
    tipos = []  # tipos (parcial, exato)
    for i in texto:
        teste[0] = 2
        print(teste, i)
        if dicio.get(i):  # procura o caractere no dicionario
            # caso ele exista então usamos a função para saber quais posições ele ocupa
            retorno = bit(teste, dicio[i])
            # aqui retornamos os estados de confirmação da palavra quais indices ainda podem conter a apalavra
            teste = retorno[1]
            # aqui incrementamos caso uma palavra tenha sido encontrada
            resposta[0] += retorno[0]
            if retorno[0] == 1:
                ocorrencias.append(cLidos - tamanho)  # assim que uma palavra é
                tipos.append(retorno[2])
        else:  # caso o caractere não esteja no dicionario então comparamos ele a uma lista vazia ao adicionarmos ele mas uma lista vazia ele decrementa os marcadores
            # tornado os exatos em parciais e os parciais em errados
            retorno = bit(teste, [False for x in range(len(teste))])
            teste = retorno[1]
            resposta[0] += retorno[0]
            if retorno[0] == 1:  # caso uma palavra seja adicionada
                # então acressentamos o indice do inicio dela em uma lista
                ocorrencias.append(cLidos - tamanho)
                tipos.append(retorno[2])  # e o tipo dela em outra
        cLidos += 1
    resposta.append(ocorrencias)  # aqui retornamos todos os indices
    resposta.append(tipos)  # e aqui todos os tipos
    return resposta  # essa lista contem um inteiro com o numero de ocorrencias, uma lista com seus indices, e outra com seus tipos


h = compara(palavra, texto)
tamanho = len(h[1])
cont = 0
print(f" foram encontados {h[0]} palavras no texto")

while cont < tamanho:
    if h[2][cont] == 1:
        tipo = "parcial"
    else:
        tipo = "exato"
    print(f"no indice {h[1][cont]} é {tipo}")
    cont += 1
