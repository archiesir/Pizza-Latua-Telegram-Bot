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


# PARSE PRODUCTS:
# PIZZA
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


def get_pizza_by_title(title):
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
                rows = food.find('div', class_='row').find_all('span')
                price = rows[0].text
                gram = rows[1].text
            except:
                price = False
                gram = False
            try:
                picture = pizza_url + food.find('a').find('img').get('src')
            except:
                picture = False

            product = {
                'title': title,
                'comp': comp,
                'gram': gram,
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


# BURGER
def get_burger_titles():
    titles = []
    html = requests.get(burger_url).text

    soup = BeautifulSoup(html, 'lxml')
    food_col = soup.find('div', id="menu-good-77").find_all('div', class_='food-col')

    for food in food_col:
        try:
            title = food.find('span', class_='food-title').text
            titles.append(title)
        except:
            continue

    return titles


def get_burger_by_title(title):
    find_title = title
    html = requests.get(burger_url).text

    soup = BeautifulSoup(html, 'lxml')
    food_col = soup.find('div', id="menu-good-77").find_all('div', class_='food-col')

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


# DRINKS
def get_drinks_titles():
    titles = []
    html = requests.get(drinks_url).text

    soup = BeautifulSoup(html, 'lxml')
    food_col = soup.find('div', id="menu-good-2").find_all('div', class_='food-col')

    for food in food_col:
        try:
            title = food.find('span', class_='food-title').text
            titles.append(title)
        except:
            continue

    return titles


def get_drinks_by_title(title):
    find_title = title
    html = requests.get(drinks_url).text

    soup = BeautifulSoup(html, 'lxml')
    food_col = soup.find('div', id="menu-good-2").find_all('div', class_='food-col')

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


# PASTA
def get_pasta_titles():
    titles = []
    html = requests.get(pasta_url).text

    soup = BeautifulSoup(html, 'lxml')
    food_col = soup.find('div', id="menu-good-3").find_all('div', class_='food-col')

    for food in food_col:
        try:
            title = food.find('span', class_='food-title').text
            titles.append(title)
        except:
            continue

    return titles


def get_pasta_by_title(title):
    find_title = title
    html = requests.get(pasta_url).text

    soup = BeautifulSoup(html, 'lxml')
    food_col = soup.find('div', id="menu-good-3").find_all('div', class_='food-col')

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


# SALAD
def get_salad_titles():
    titles = []
    html = requests.get(salad_url).text

    soup = BeautifulSoup(html, 'lxml')
    food_col = soup.find('div', id="menu-good-4").find_all('div', class_='food-col')

    for food in food_col:
        try:
            title = food.find('span', class_='food-title').text
            titles.append(title)
        except:
            continue

    return titles


def get_salad_by_title(title):
    find_title = title
    html = requests.get(salad_url).text

    soup = BeautifulSoup(html, 'lxml')
    food_col = soup.find('div', id="menu-good-4").find_all('div', class_='food-col')

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


# SOUP
def get_soup_titles():
    titles = []
    html = requests.get(soup_url).text

    soup = BeautifulSoup(html, 'lxml')
    food_col = soup.find('div', id="menu-good-5").find_all('div', class_='food-col')

    for food in food_col:
        try:
            title = food.find('span', class_='food-title').text
            titles.append(title)
        except:
            continue

    return titles


def get_soup_by_title(title):
    find_title = title
    html = requests.get(soup_url).text

    soup = BeautifulSoup(html, 'lxml')
    food_col = soup.find('div', id="menu-good-5").find_all('div', class_='food-col')

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
                price = food.find('form', 'food-form').find('div', class_='row').find('span').text
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


# OTHERS
def get_others_titles():
    titles = []
    html = requests.get(others_url).text

    soup = BeautifulSoup(html, 'lxml')
    food_col = soup.find('div', id="menu-good-6").find_all('div', class_='food-col')

    for food in food_col:
        try:
            title = food.find('span', class_='food-title').text
            titles.append(title)
        except:
            continue

    return titles


def get_others_by_title(title):
    find_title = title
    html = requests.get(others_url).text

    soup = BeautifulSoup(html, 'lxml')
    food_col = soup.find('div', id="menu-good-6").find_all('div', class_='food-col')

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
