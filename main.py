import requests

def getinfo():
    url = "https://restcountries.com/v3.1/all"
    data = requests.get(url)
    data = data.json()

    for element in data:
        print(element['region'], "-", element['translations']['spa']['common'], "-")
        if ("languages" in element):
            for value in element['languages'].values():
                print(value)


if __name__ == '__main__':
    getinfo()
