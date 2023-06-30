def ultimo(cha, st):
    """
    Encontra o valor de pulo no último caractere do padrão.
    Parameters:
        cha (str): Caractere do valor de pulo
        st (str): Padrão que vamos procurar no texto
    Returns:
        (int): Valor de pulo do caractere em questão
    """
    n = len(
        st
    )  # caso o caracter procurado seja igual ao ultimo ou não tenha na palavra, retornamos o tamanho da string
    for i in range(
        len(st) - 1
    ):  # caso o caracter não seja o ultimo e ele exista na palavra, retornamos um valor que dempedera da posição dele
        if cha == st[i]:
            n = len(st) - (1 + i)
    return n


def compara(texto, palavra, trecho):
    """
    Compara o padrão com o trecho.
    Parameters:
        texto (str): Texto no qual procuramos o padrão
        palavra (str): Padrão que vamos procurar no texto
        trecho (int): Índice que estamos no texto
    Returns:
        (bool): Se o padrão foi encontrado ou não
    """
    tamanho = len(palavra)
    cont = 0
    while cont < tamanho:
        if palavra[cont] != texto[trecho + cont]:
            return False
        cont += 1
    return True


def BMH(texto, palavra):
    """
    Função principal que executa o algoritmo BMH.
    Parameters:
        texto (str): Texto no qual procuramos o padrão
        palavra (str): Padrão que vamos procurar no texto
    Returns:
        Tuple[int, int]: Índice da ocorrência e Número de ocorrências
    """
    tamanho = len(texto)
    cont = 0
    num_ocorrencias = 0
    pos_ocorrencias = []
    indice = len(palavra) - 1
    while cont < tamanho:
        if compara(texto, palavra, cont):
            num_ocorrencias += 1
            pos_ocorrencias.append(cont)
        cont += ultimo(texto[cont + indice], palavra)
    return (num_ocorrencias, pos_ocorrencias)


if __name__ == "__main__":
    texto = 'lblalblanbla'
    dis = 'bla'
    cont = 0  # variavel que indica a posição que devemos começar a compareação na lista texto
    veri = 0  # variavel que indica quantos caracteres iguais as strings tem
    num = 0  # numero de vezes que a palavra apareceu

    print(BMH(texto, dis))
