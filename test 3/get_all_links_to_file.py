from bs4 import BeautifulSoup as bs
import pandas as pd
import requests

r = requests.get('https://www.perekrestok.ru/cat')
# print(r.status_code)
perek_soup = bs(r.text, 'html.parser')

list_perek_links = list()
# list_all_links = list()
data = open('links_for_parse.txt', 'a', encoding='utf-8')

cat_links = perek_soup.find_all('a', attrs={"class":"sc-dQoVA fvoiIk"})
for a in cat_links:
    list_perek_links.append('https://www.perekrestok.ru' + a['href'])

for i in range(len(list_perek_links)):
    i_req = requests.get(list_perek_links[i])
    #print(r.status_code)
    link_i_soap = bs(i_req.text, 'html.parser')
    all_links_in_i_category = link_i_soap.find_all('a', attrs={"class":"sc-dQoVA dsEnQi products-slider__header"})
    for j in all_links_in_i_category:
        # list_all_links.append('https://www.perekrestok.ru' + j['href'])
        data.writelines('https://www.perekrestok.ru' + j['href'] + '\n')
#print(list_all_links, len(list_all_links))
data.close()




# r2 = requests.get(list_perek_links[14])
# print(r2.status_code)
# link_soap = bs(r2.text, 'html.parser')
# all_cat_links = link_soap.find_all('a', attrs={"class":"sc-dQoVA dsEnQi products-slider__header"})




# result_list = {'category': [],'title': [], 'price': []}

# category_names = perek_soup.find_all('h2', attrs={"class":"catalog-content-group__title"})
# for cat in range(len(category_names)):
#     parent_category = category_names[cat].find_parent('div')
#     item_category_names = parent_category.find_all('div', class_='product-card-title__wrapper')
#     for i in range(len(item_category_names)):
#         sub_names = item_category_names[i].find_next_sibling('div', class_='product-card__control')
#         price = sub_names.find('div', class_='price-new')
#         if price != None:
#             result_list['category'].append(category_names[cat].text)
#             result_list['title'].append(item_category_names[i].text)
#             result_list['price'].append(price.text)
#             # print(category_names[cat].text ,item_category_names[i].text, price.text,)
#         else:
#             continue

# df = pd.DataFrame(data=result_list)
# df.to_csv(FILE_NAME)

# print(df.shape)