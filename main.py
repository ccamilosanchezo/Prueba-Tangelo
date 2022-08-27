import requests
import time
import pandas as pd

from encrypt import sha1
from managedatabase import managedatabase


def getLanguages(element):
    lang = ""
    if "languages" in element:
        for value in element['languages'].values():
            if lang != "":
                lang = lang + ", "
            lang = lang + value
    return lang


def times(dataframe):
    print("El tiempo total fue de: %s ms" % dataframe['Time'].sum())
    print("El tiempo promedio fue de: %s ms" % dataframe['Time'].mean())
    print("El tiempo mínimo fue de %s ms" % dataframe['Time'].min())
    print("El tiempo máximo fue de: %s ms" % dataframe['Time'].max())


def getinfo():
    url = "https://restcountries.com/v3.1/all"
    data = requests.get(url)
    data = data.json()
    table = pd.DataFrame(columns=['Region', 'City Name', 'Language', 'Time'])
    for element in data:
        timeini = time.time()
        language = getLanguages(element)
        dict = {
            'Region': [element['region']],
            'City Name': [element['translations']['spa']['common']],
            'Language': [sha1(language)],
            'Time': (time.time()-timeini)*1000
        }
        table=pd.concat([table, pd.DataFrame(data=dict)], ignore_index = True, axis = 0)
    times(table)
    managedatabase(table)


if __name__ == '__main__':
    getinfo()