import requests 
import pandas as pd

url = "https://servicodados.ibge.gov.br/api/v1/localidades/municipios"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    codigos_municipios = []
    
    for municipio in data:
        codigo = municipio['id']
        codigos_municipios.append(codigo) 
else:
    print("Falha ao obter os dados. Código de status:", response.status_code)

df = pd.DataFrame() 
df['municipios_ibge'] = codigos_municipios
df.to_csv('../src/codigos_municipios.csv', header = True, sep = ',', index = False) 
