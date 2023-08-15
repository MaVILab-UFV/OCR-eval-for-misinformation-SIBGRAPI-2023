def getDadosDaRegex(regex):                                                             # Retorna os dados da regex
    regex = regex.split('-')
    indice = eval(regex[0])
    fonte = regex[1]
    tamanhoDaFonte = int(regex[2])
    corDaFonte = eval(regex[3])
    if regex[4] == 'True':
        sombra = True
    else:
        sombra = False
    if regex[5] != 'im1' and regex[5] != 'im2':                                         # O plano de fundo é uma cor sólida
        planoDeFundo = eval(regex[5])
    else:                                                                               # O plano de fundo é outra imagem
        planoDeFundo = regex[5]
    dimensoes = eval(regex[6])    
    if regex[7] == '':                                                                  # Ângulo negativo
        angulo = int(regex[8]) * -1
    else:                                                                               # Ângulo positivo
        angulo = int(regex[7])    
    return indice, fonte, tamanhoDaFonte, corDaFonte, sombra, planoDeFundo, dimensoes, angulo