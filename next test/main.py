from bs4 import BeautifulSoup as bs
import pandas as pd
import requests

FILE_NAME = "pars.csv"
r = requests.get('https://www.perekrestok.ru/cat/c/27/zavtrak')
print(r.status_code)
perek_soup = bs(r.text, 'html.parser')
result_list = {'category': [],'title': [], 'price': []}

category_names = perek_soup.find_all('h2', attrs={"class":"catalog-content-group__title"})
print(len(category_names)) # категория под индексом 3 не имеет одну цену
for el in range(len(category_names)):
    if el == 3:
        continue
    patent_category = category_names[el].find_parent('div')
    item_category_names = patent_category.find_all('div', class_='product-card__title')
    item_category_prices = patent_category.find_all('div', class_='price-new')
    for item in range(len(item_category_names)):
        result_list['category'].append(category_names[el].text)
        result_list['title'].append(item_category_names[item].text)
        result_list['price'].append(item_category_prices[item].text)

df = pd.DataFrame(data=result_list)
df.to_csv(FILE_NAME)

