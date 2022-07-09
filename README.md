url = "https://amdm.ru/akkordi/sektor_gaza/173218/30_let/"
 
sel = "#body > div.content-table > article > div.b-podbor > div:nth-child(2) > h1 > span:nth-child(1)"
import request
respons = request.get(url)
print (respons.status_code)
print(respons.text)
