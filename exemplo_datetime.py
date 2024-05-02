import datetime

# 1. Obter data e hora atual
agora = datetime.datetime.now()
print(agora)

# 2. Criar uma data específica
data_especifica = datetime.datetime(2024, 4, 29)
print(data_especifica)

# 3. Formatar uma data como string
data_formatada = agora.strftime("%Y-%m-%d %H:%M:%S")
print(data_formatada)

# 4. Adicionar dias a uma data
data_futura = agora + datetime.timedelta(days=7)
print(data_futura)

# 5. Subtrair datas para encontrar a diferença 
outra_data = datetime.datetime(2024, 3, 15)
diferenca = agora - outra_data
print(f"Diferença das datas: {diferenca}")

# 6. Extrair componenetes individuais de uma data
ano = agora.year
mes = agora.month
dia = agora.day
hora = agora.hour
segundo = agora.second
print(f"Ano:{ano} , Mês: {mes}, Dia: {dia}, Hora: {hora}, Segundo: {segundo}")

# 7. Comparar datas
data1 = datetime.datetime(2024, 4, 29)
data2 = datetime.datetime(2024, 5, 1)
if data1 < data2:
    print("data1 é antes do data2")

# 8. Converter uma string em um objeto do datetime
data_str = "2024-12-25"
data_obj = datetime.datetime.strptime(data_str, "%Y-%m-%d")
print(f"Data convertida: {data_obj}")
