from bs4 import BeautifulSoup as bs
import pandas as pd
import requests

FILE_NAME = "pars.csv"
r = requests.get('https://www.perekrestok.ru/cat/c/27/zavtrak')
print(r.status_code)
perek_soup = bs(r.text, 'html.parser')

result_list = {'category': [],'title': [], 'price': []}

category_names = perek_soup.find_all('h2', attrs={"class":"catalog-content-group__title"})
for cat in range(len(category_names)):
    parent_category = category_names[cat].find_parent('div')
    item_category_names = parent_category.find_all('div', class_='product-card-title__wrapper')
    for i in range(len(item_category_names)):
        sub_names = item_category_names[i].find_next_sibling('div', class_='product-card__control')
        price = sub_names.find('div', class_='price-new')
        if price != None:
            result_list['category'].append(category_names[cat].text)
            result_list['title'].append(item_category_names[i].text)
            result_list['price'].append(price.text)
            # print(category_names[cat].text ,item_category_names[i].text, price.text,)
        else:
            continue

df = pd.DataFrame(data=result_list)
df.to_csv(FILE_NAME)

print(df.shape)