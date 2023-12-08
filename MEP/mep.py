from bs4 import BeautifulSoup
from IPython.display import HTML
import json
import requests
import pandas as pd
from io import StringIO
import numpy as np

url = "https://mercados.ambito.com//dolarrava/mep/historico-general/2020-20-03/2023-12-07"
resp = requests.get(url).text

# print(resp)

df = pd.DataFrame(np.array(resp).tolist())

print(df)

# df_subset = df.iloc[:, :2]


# def consulta(fecha):
#     condicion = df_subset["indice_tiempo"] == fecha
#     data_filtrada = df_subset[condicion]
#     cer = data_filtrada["cer_diario"].iloc[0]
#     return cer


# fecha = "2023-10-27"
# cer = consulta("2023-10-27")
# print(f'CER al {fecha}: {cer}')
# # 149.129542
