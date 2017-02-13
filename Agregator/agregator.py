#coding: utf-8

import json
import re
from bs4 import BeautifulSoup
from urllib2 import urlopen


zapros = raw_input('Введите запрос: ')       # 'raw_' for python 2
zapros_splitted = zapros.split(' ')


#online parsing 'http://www.mobile-review.com'
def find_mobile_review(perem):

    base_url = 'http://www.mobile-review.com'
    # html = open('MR.html').read()
    html = urlopen('http://www.mobile-review.com/review.shtml')
    soup = BeautifulSoup(html, 'lxml')

    links_list = []
    soup.findAll('div', class_='phonelist')
    for link in soup.findAll(href=re.compile(perem)):
        a = [(base_url + link.get('href'))]
        links_list.append(a)
    return links_list


def result_mobile_review():
    result_list = []

    for i in zapros_splitted:
        perem = str(i)
        result_list.append(find_mobile_review(perem))

    if len(result_list) > 1:
        finish_list = [x for x in result_list[1] if x in result_list[0]]
        if len(finish_list) >= 1:
            print ("\n".join(map(str, finish_list)))
        else:
            print('ERROR')
    else:
        finish_list = result_list
        print("\n".join(map(str, finish_list)))

    filename = 'result.json'

    with open(filename, 'w') as f:
        json.dump(finish_list, f)

# offline parsing 'https://wylsa.com/'

def find_wylsa(perem):

    html = open('wylsacom.html').read()
    #html = urlopen('https://wylsa.com/category/reviews/')
    soup = BeautifulSoup(html, 'lxml')

    links_list = []
    soup.findAll('div', class_='main')
    for link in soup.findAll(href=re.compile(perem)):
        a = [link.get('href')]
        links_list.append(a)
    return links_list


def result_wylsa():

    result_list = []

    for i in zapros_splitted:
        perem = str(i)
        result_list.append(find_wylsa(perem))

    if len(result_list) > 1:
        finish_list = [x for x in result_list[1] if x in result_list[0]]
        if len(finish_list) >= 1:
            print ("\n".join(map(str, finish_list)))
        else:
            print('ERROR')
    else:
        finish_list = result_list
        print("\n".join(map(str, finish_list)))
    filename = 'result.json'

    with open(filename, 'a') as f:
        json.dump(finish_list, f)


def main():
    result_mobile_review()
    result_wylsa()


if __name__ == '__main__':
    main()


