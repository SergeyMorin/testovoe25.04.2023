from bs4 import BeautifulSoup as bs
import pandas as pd

FILE_NAME = FILE_NAME = "test.csv"
html_file = open("zavtrak.html", 'r', encoding='utf-8')
html_data = html_file.read()
perek_soup = bs(html_data)
result_list = {'category': [],'title': [], 'price': []}
category_names = perek_soup.find_all('h2', attrs={"class":"catalog-content-group__title"}) # тут поиск всех категорий 
for el in range(len(category_names)):
    patent_category = category_names[el].find_parent('div')
    item_category_names = patent_category.find_all('div', class_='product-card__title')
    item_category_prices = patent_category.find_all('div', class_='price-new')
    for item in range(len(item_category_names)):
        # print(category_names[el].text, item_category_names[item].text, item_category_prices[item].text)
        result_list['category'].append(category_names[el].text)
        result_list['title'].append(item_category_names[item].text)
        result_list['price'].append(item_category_prices[item].text)
print(result_list)

df = pd.DataFrame(data=result_list)
df.to_csv(FILE_NAME)

print(df.head(n=10))
