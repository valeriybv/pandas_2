'''
Задание 2
Используйте файл keywords.csv.

Нужно написать гео-классификатор, который каждой строке сможет выставить географическую принадлежность определённому региону.
Т. е. если поисковый запрос содержит название города региона, то в столбце ‘region’ пишется название этого региона.
Если поисковый запрос не содержит названия города, то ставим ‘undefined’.

Правила распределения по регионам Центр, Северо-Запад и Дальний Восток:

geo_data = {

'Центр': ['москва', 'тула', 'ярославль'],

'Северо-Запад': ['петербург', 'псков', 'мурманск'],

'Дальний Восток': ['владивосток', 'сахалин', 'хабаровск']
}

Результат классификации запишите в отдельный столбец region.
'''
import pandas as pd


geodata = pd.read_csv('raw_data/keywords.csv')
print(geodata)

regions = {
'Центр': ['москва','порно','москвы','москве','москву','тула','тулы','туле','тулу','ярославль','ярославля','ярославлю','ярославле'],
'Северо-Запад': ['петербург','петербурга','петербургу','петербурге','Санкт-Петербург','Санкт-Петербурга','Санкт-Петербургу','Санкт-Петербурге', 'псков','пскова','пскову','пскове','мурманск','мурманска','мурманску','мурманске'],
'Дальний Восток': ['владивосток','владивостока','владивостоку','владивостоке', 'сахалин','сахалина','сахалину','сахалине', 'хабаровск','хабаровска','хабаровску','хабаровске']
}
print(geodata.info())

def check_city(keyword):
    for key in regions:
        for v in regions[key]:
            for city in v:
                if city in keyword:
                    return key

for idx, row in geodata.iterrows():
    if check_city(row['keyword']) is not None:
        geodata[idx, 'region'] = check_city(row['keyword'])
    else:
        geodata[idx, 'region'] = 'undefined'

print(geodata['region'].unique())