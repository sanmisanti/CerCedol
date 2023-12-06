import requests
from bs4 import BeautifulSoup
from IPython.display import HTML
import requests
import json

url = "https://www.cedol.org.ar/indices-logisticos.html"
resp = requests.get(url).text

html_obtenido = requests.get(url)
soup = BeautifulSoup(html_obtenido.text, "html.parser")

tabla = soup.find("table", {"class": "table d-content__text_indices"})
body = tabla.find("tbody")

active_rows = body.select("tr")

data = {}
curr_year = ""
for tr in active_rows:
    if tr.get("class"):
        dataYear = tr.find("td").text
        # print(dataYear)
        curr_year = dataYear
    else:
        datos_por_mes = tr.find_all("td")
        # print(datos_por_mes)
        # print("curr_year", curr_year)
        # valorMensual = {datos_por_mes[0].text : datos_por_mes[4].text}
        data[datos_por_mes[0].text + "-" +
             dataYear[dataYear.find(" ") + 1:]] = datos_por_mes[4].text
json_data = json.dumps(data, ensure_ascii=False, indent=4)
json_data = json.loads(json_data)


def getData(mes, año):
    key = f"{mes}-{año}"
    return float(json_data.get(key).replace(".", "").replace(",", "."))


Mes = "Abril"
Año = "2014"
cedol = getData(Mes, Año)
print(f'CEDOL al {Mes}/{Año}: {cedol}')
