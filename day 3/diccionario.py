diccionario = {"c1": 10, "c2": 20 }
print(diccionario['c1'])

diccionario['c3'] = 30
print(diccionario)

dic = {"c1": ["a","b","c"], "c2": ["d","e","f"]}

print(dic['c2'][1].upper())

print(dic.keys()) # trae las llaver
print(dic.values()) # trae los valores
print(dic.items()) # trae todo (?tuplas)