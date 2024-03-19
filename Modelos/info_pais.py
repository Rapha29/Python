import requests
from translate import Translator

while True:
    pais = input("Digite o país que deseja obter informações: ")
    url = f"https://restcountries.com/v3.1/name/{pais}?fullText=true"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()[0]

        print(f'País: {data["name"]["common"]}')
        print(f'Capital: {data["capital"][0]}')
        print(f'Moeda: {data["currencies"].keys()}')
        print(f'Idiomas: {data["languages"].keys()}')
        print(f'Fazem fronteira: {data["borders"]}')
        print(f'População: {data["population"]}')
    else:
        print("País não encontrado.")