def calcular_horario_llegada(hora_salida:int, minuto_salida:int, segundo_salida:int, duracion_horas:int, duracion_minutos:int, duracion_segundos:int):

    if hora_salida+duracion_horas > 23:
        hora = hora_salida+duracion_horas-24
    else:
        hora= hora_salida+duracion_horas
    
    if minuto_salida+duracion_minutos > 60:
        minuto = minuto_salida+duracion_minutos-60
        hora += 1
        if hora >23:
            hora -= 24
    else:
        minuto= minuto_salida+duracion_minutos
    
    if segundo_salida+duracion_segundos > 60:
        segundo = segundo_salida+duracion_segundos-60
        minuto += 1
        if minuto > 60:
            minuto = 0
            hora+=1
    else:
        segundo= segundo_salida+duracion_segundos
    return str(hora)+":"+str(minuto)+":"+str(segundo)