from datetime import datetime 
ahora = datetime.now()
print (ahora.year)
print(ahora.strftime("%A"))
fecha = datetime(2025, 10, 4)
print(fecha.strftime("%B"))
str_fecha = "19/05/09 10:00:00"
fecha_obj = datetime.strptime(str_fecha, '%d/%m/%y %H:%M:%S')
print(ahora - fecha_obj)