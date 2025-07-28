# Importe a biblioteca datetime e crie uma função chamada data_atual que exiba a data e a
# hora atual no formato "Dia/Mês/Ano Hora:Minuto:Segundo".
# Dica: Utilize datetime.datetime.now() para obter a data e hora atual.

import datetime

def data_atual():
    agora = datetime.datetime.now()
    hora_formatada = agora.strftime("%H:%M:%S")
    print("Hora atual:", hora_formatada)

data_atual()