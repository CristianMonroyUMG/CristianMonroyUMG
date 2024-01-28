hora_str = input("Ingresa la hora en formato HH:MM:SS: ")

hora, minutos, segundos = map(int, hora_str.split(':'))
segundos_totales = hora * 3600 + minutos * 60 + segundos

print("Han transcurrido ",segundos_totales," segundos desde la medianoche.")
