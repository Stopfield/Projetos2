texto = 'lblalblanbla'
dis = 'blaz'
cont = 0  # variavel que indica a posição que devemos começar a compareação na lista texto
veri = 0  # variavel que indica quantos caracteres iguais as strings tem
num = 0  # numero de vezes que a palavra apareceu


def ultimo(cha, st):
    '''essa função analisa o ultimo caractere da da string e de acordo com o resultado ela decide quantos indices vai pular'''
    n = len(
        st
    )  # caso o caracter procurado seja igual ao ultimo ou não tenha na palavra, retornamos o tamanho da string
    for i in range(
        len(st) - 1
    ):  # caso o caracter não seja o ultimo e ele exista na palavra, retornamos um valor que dempedera da posição dele
        if cha == st[i]:
            n = len(st) - (1 + i)
    return n


def compara(texto, palavra, trecho):  # compara caractere até achar um incompativel
    '''Essa função analisa o trecho do texto com a palavra procurada para ver se são iguais'''
    tamanho = len(palavra)
    cont = 0
    while cont < tamanho:
        if palavra[cont] != texto[trecho + cont]:
            return False
        cont += 1
        if trecho + cont >= len(texto):
            return False
    return True


def BMH(texto, palavra):
    '''Essa função principal é responsavel ordenar os trechos para serem analisados '''
    tamanho = len(texto)  # tamanho do texto analisado
    cont = 0
    ocorrencia = 0
    indice = len(palavra) - 1  # tamanho da plavra
    while cont < tamanho:  # faz analises enqunado uma palavra tiver indice para se analisada
        if compara(texto, palavra, cont):
            ocorrencia += 1
        if cont + indice < len(texto):
            cont += ultimo(texto[cont + indice], palavra)
        else:
            cont = tamanho  # caso o resto do texto não tenha caracteres o sufuciente para serem analisados a função encerra
    return ocorrencia


print(BMH(texto, dis))
