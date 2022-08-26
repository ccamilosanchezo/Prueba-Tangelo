import requests
import pandas as pd

from encrypt import sha1

def getLanguages(element):
    lang = ""
    if "languages" in element:
        for value in element['languages'].values():
            if lang != "":
                lang = lang + ", "
            lang = lang + value
    return lang

def getinfo():
    url = "https://restcountries.com/v3.1/all"
    data = requests.get(url)
    data = data.json()
    table = pd.DataFrame(columns=['Region', 'City Name', 'Language', 'Time'])
    for element in data:
        language = getLanguages(element)
        dict = {
            'Region': [element['region']],
            'City Name': [element['translations']['spa']['common']],
            'Language': [sha1(language)]
        }
        table=pd.concat([table, pd.DataFrame(data=dict)], ignore_index = True, axis = 0)
    print(table)


if __name__ == '__main__':
    getinfo()
