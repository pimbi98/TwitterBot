import requests



año = '2021' #Modificar anualmente
url = 'http://nolaborables.com.ar/api/v2/feriados/' + año + '?formato=mensual'
resp = requests.get(url)

feriados = resp.json()