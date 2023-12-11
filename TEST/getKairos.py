import requests
from bs4 import BeautifulSoup
import requests
import json
import re

urlIndex = "https://ar.kairosweb.com/"
response = requests.get(urlIndex)

responseHeaders = dict(response.headers)
responseHeadersFormated = json.dumps(responseHeaders, indent=4)

headerCFRAY = responseHeaders["CF-RAY"]

responseCookies = response.cookies

responseBody = response.text

# sesion = requests.Session()

soup = BeautifulSoup(responseBody, "html.parser")
scripts = soup.find_all("script")

for script in scripts:
    if script.string:
        match = re.search(
            r"window\['__CF\$cv\$params'\]=\{r:'(.*?)'", script.string)
        if match:
            parametro_r = match.group(1)
            print("parametro_r:", parametro_r)
