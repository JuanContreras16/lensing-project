#Juan José Contreras González

from datetime import datetime, timedelta
import re

pattern = re.compile(r'(.+ , )(\d{2}/\d{2}/\d{4}) (\d{2}:\d{2}:\d{2}) (a|p)\. m\.')

with open("Temperatura.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        coincidencia = pattern.search(linea)

        if coincidencia:
            datos = coincidencia.group(1)
            fecha = coincidencia.group(2)
            hora = coincidencia.group(3)
            med = coincidencia.group(4)

            fecha_hora = f"{fecha} {hora}"
            try:
                fecha_hora = datetime.strptime(fecha_hora, '%d/%m/%Y %H:%M:%S') 
            except ValueError:
                print("Cadena invalida:", fecha_hora)
                continue
            fecha_hora = fecha_hora + timedelta(hours=1)

            new_fecha = fecha_hora.strftime("%d/%m/%Y")
            new_hora = fecha_hora.strftime("%H:%M:%S")

            if fecha_hora.hour < 12:
                new_med = "a"
            else:
                new_med = "p"
            print(
                datos
                + new_fecha
                + " "
                + new_hora
                + " "
                + new_med
                + ". m."
            )
        else:
            print(linea.strip())