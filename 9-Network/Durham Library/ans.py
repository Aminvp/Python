import requests

def process(url):
    response = requests.get(url, verify=False)
    
    if response.status_code != 200:
        return 'Bad Query'

    library = response.json()
    library = list(library)

    if library == []:
        return "I can't recognize it"

    for lib in library:
        cat = lib["category"]
        if cat != lib["category"]:
            return "I can't recognize it"
    return cat
    


print(process('quera-ir./math'))