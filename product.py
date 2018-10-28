# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

pizza_url = "http://pizza-latua.lp-seller.ru"
burger_url = "http://pizza-latua.lp-seller.ru/burgers.html"
drinks_url = "http://pizza-latua.lp-seller.ru/drinks.html"
pasta_url = "http://pizza-latua.lp-seller.ru/pasta.html"
salad_url = "http://pizza-latua.lp-seller.ru/salad.html"
soup_url = "http://pizza-latua.lp-seller.ru/vkysnij-sup.html"
others_url = "http://pizza-latua.lp-seller.ru/misc.html"


def get_html(url):
    r = requests.get(url)
    return r.text


def get_pizza_titles():
    titles = []
    html = requests.get(pizza_url).text

    soup = BeautifulSoup(html, 'lxml')
    food_col = soup.find('div', id="menu-good-1").find_all('div', class_='food-col')

    for food in food_col:
        try:
            title = food.find('span', class_='food-title').text
            titles.append(title)
        except:
            continue

    return titles


def get_pizza_product_by_title(title):
    find_title = title
    html = requests.get(pizza_url).text

    soup = BeautifulSoup(html, 'lxml')
    food_col = soup.find('div', id="menu-good-1").find_all('div', class_='food-col')

    for food in food_col:
        try:
            title = food.find('span', class_='food-title').text
        except:
            title = False

        if find_title == title:
            try:
                title = food.find('span', class_='food-title').text
            except:
                title = False
            try:
                comp = food.find('p', class_='food-sostav').text
            except:
                comp = False
            try:
                price = food.find('div', class_='row').find('span').text
            except:
                price = False
            try:
                picture = pizza_url + food.find('a').find('img').get('src')
            except:
                picture = False

            product = {
                'title': title,
                'comp': comp,
                'price': price,
                'picture': picture
            }
            return product
            break
    product = {
        'title': False,
        'comp': False,
        'price': False,
        'picture': False
    }
    return product
