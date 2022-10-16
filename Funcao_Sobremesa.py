def sobremesa(valor):
    if valor == 0:
        return 'nada'
    elif valor % 3 == 0 and valor % 5 == 0 and valor % 7 == 0:
        return 'Queijo e Goiabada e Rapadura'
    elif valor % 3 == 0 and valor % 5 == 0:
        return 'Queijo e Goiabada'
    elif valor % 3 == 0 and valor % 7 == 0:
        return 'Queijo e Rapadura'
    elif valor % 5 == 0 and valor % 7 == 0:
        return 'Goiabada e Rapadura'
    elif valor % 3 == 0:
        return 'Queijo'
    elif valor % 5 == 0:
        return 'Goiabada'
    elif valor % 7 == 0:
        return 'Rapadura'
    else:
        return 'nada'