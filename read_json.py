import json

ficheiro = input()
try:
    with open(ficheiro, encoding='utf-8') as data:
        texto = json.load(data)
        print(texto)
except:
    print("Ocorreu um erro!")
finally:
    print("Processo concluido!")