from datetime import date, time, datetime, timedelta

def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%Y %H:%M:%S'))
    print(data_atual.strftime('%c'))
    print(data_atual.weekday())
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
    print(tupla[data_atual.weekday()])
    data_criada = datetime(2022, 6, 20, 15, 30, 20)
    print(data_criada.strftime('%c'))
    data_string = '01/01/2021 12:20:22'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')   
    print(data_convertida)
    nova_data = data_convertida - timedelta(days= 365, hours=2, minutes=15)
    print(nova_data)
def trabalhando_com_date():
    data_atual = date.today()
    data_atual_str = data_atual.strftime('%d/%m/%Y')
    print(type(data_atual))
    print(data_atual_str)
    print(type(data_atual_str))

def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    horario_str = horario.strftime('%H:%M:%S')
    print(horario_str)

if __name__ == '__main__': #aqui irá mostrar os valores na tela
    trabalhando_com_time()
    trabalhando_com_datetime()
