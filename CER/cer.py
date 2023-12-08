from bs4 import BeautifulSoup
from IPython.display import HTML
import json
import requests
import pandas as pd
from io import StringIO


def getCER(fecha):
    url = "https://infra.datos.gob.ar/catalog/sspm/dataset/94/distribution/94.2/download/cer-uva-uvi-diarios.csv"
    resp = requests.get(url).text

    df = pd.read_csv(StringIO(resp))

    df_subset = df.iloc[:, :2]
    condicion = df_subset["indice_tiempo"] == fecha
    data_filtrada = df_subset[condicion]
    cer = data_filtrada["cer_diario"].iloc[0]
    return cer


# fecha = "2023-10-27"
# cer = consulta("2023-10-27")
# print(f'CER al {fecha}: {cer}')
# 149.129542
