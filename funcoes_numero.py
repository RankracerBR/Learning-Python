def eh_numero_armstrong(numero):
  digitos = len(str(numero))
  tp = numero 
  add_soma = 0
  while tp != 0:
  #pega o último dígito do número
    n = tp % 10 
  #procura pelo 'n' elevado a algum número
    add_soma += n**digitos
    tp = tp//10
  if add_soma == numero:
    return True
  else:
    return False