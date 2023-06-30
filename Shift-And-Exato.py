def dicionario(palavra):
    """
    Função que cria um dicionario, com todas as letras da palavra, e um lista com as ocorrencias delas
    Essa função gera a nossa máscara! Verifica onde ocorre as letras no padrão, e cria-se um array
    de "bits" com essas ocorrências.
    Parameters:
        palavra (str): O padrão.
    Returns:
        mat (dict): A máscara. Para cada letra, uma array de "bits".
    """
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


def bit(ocorrencias, recorrencias):
    """
    Realiza o "bit-shift and", ou seja, atualiza o nosso R, de acordo com a regra.
    Aqui pegamos o ocorrencias do caracter, quais posições ele ocupa na string atual, e quais posições ele ocupa no dicionario
    Parameters:
        ocorrencias (list): O nosso array de bits R'
        recorrencias (list): O array de bits de um caracter na máscara
    Returns:
        (list): Uma lista que contém o valor do último bit de R' - para verificar o casamento;
                e contém uma lista com o novo R'.
    """
    # Começa do último índice - de trás pra frente
    indice = len(recorrencias) - 1
    resultado = []  # Nosso bit array
    encontrada = 0
    # checamos se o ultimo caractere tambem tem como posição o ultimo no dicionario
    if ocorrencias[indice] and recorrencias[indice]:
        encontrada = 1  # numero de palavras encontradas após checagem do ultimo bit
        ocorrencias[indice] = False
    indice -= 1  # como já checamos o ultimo decrementamos
    # Aqui ocorre o bit-shift pra direita
    # ocorrencias >> 1
    while indice >= 0:  # começamos e ordem decrecente para podemos alterar os valores do indice da frente, se não ele seria zerado
        if ocorrencias[indice] and recorrencias[indice]:
            # caso o caracter esteja batendo com suas posições no dicionario, então increntamos a proxima posição
            ocorrencias[indice + 1] = True
        ocorrencias[indice] = False
        indice -= 1
        # decrementamos pois esta posição já passou por analise
    resultado.append(encontrada)
    resultado.append(ocorrencias)
    return resultado  # essa lista retorna uma lista atualizada de valores boleanos após a checagem e o numero de palavras encontradas

lista_ocorrencias = []
def compara(palavra, texto):
    # primeiro criamos um dicionario com todos os caracteres da plavra e suas recorrencias nela
    # O dicionário é a máscara!
    mascara = dicionario(palavra)
    tamanho = len(palavra)
    # O array de bits - O nosso 'R'
    R = [False for x in range(tamanho)]
    ocorrencias = 0
    for j, i in enumerate(texto):
        # O primeiro bit sempre é 1 - nesse caso, True
        R[0] = True
        print(R, i)
        # Se o R existir na máscara
        if mascara.get(i):
            # bit(Nosso R atual, bitarray do caracter na máscara)
            retorno = bit(R, mascara[i])
            R = retorno[1]
            if retorno[0]:
                lista_ocorrencias.append(j)
            print(f"R: {retorno}")
            ocorrencias += retorno[0]
        else:
            # Reseta o R
            R = [False for x in range(tamanho)]
    return ocorrencias


if __name__ == "__main__":
    palavra = 'la'
    texto = 'lalabla'
    print(compara(palavra, texto))
    print(lista_ocorrencias)
