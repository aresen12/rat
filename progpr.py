url = "https://amdm.ru/akkordi/viktor_coi/95751/gruppa_krovi/"

sel = "#body > div.content-table > article > div.b-podbor > div:nth-child(2) > h1 > span:nth-child(1)"
import requests
respons = requests.get(url)
print (respons.status_code)
print(respons.text)
