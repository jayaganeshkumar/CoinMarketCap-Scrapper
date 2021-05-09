import requests
from bs4 import BeautifulSoup, NavigableString
from scrapy import Selector
import time
import csv
import datetime
from selenium import webdriver
driver = webdriver.Chrome(executable_path=r'D:\chromedriver.exe')


def between(cur, end):
    while cur and cur != end:
        if isinstance(cur, NavigableString):
            text = cur.strip()
            if len(text):
                yield text
        cur = cur.next_element


def get_coin():
    allrows = []
    r = requests.get('https://coinmarketcap.com/coins/')
    soup = BeautifulSoup(r.text, "html.parser")

    sel = Selector(text=soup.prettify())

    columns = ['S.No', 'Name', 'Symbol', 'URL']
    allrows.append(columns)

    cryptos = sel.xpath("//tr").extract()
    count = 1
    for crypto in cryptos[1:]:
        soup = BeautifulSoup(crypto, features='html.parser')
        rows = soup.find_all('td')
        rows = [tr.text.strip() for tr in rows]
        rows[2] = list((rows[2].split("\n")))
        rows[2].pop(1)
        rows[2].pop(1)
        rows[2] = [tr.strip() for tr in rows[2]]
        for i in rows[2]:
            if i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
                rows[2].remove(i)
        while("" in rows[2]):
            rows[2].remove("")
        for i in rows[2]:
            if i == "Buy":
                rows[2].remove(i)
        for a in soup.find_all('a', href=True, class_="cmc-link"):
            rows[2].append("https://coinmarketcap.com" + a['href'])
            break
        rows[2].insert(0, count)

        allrows.append(rows[2])

        count += 1

        if(count == 51):
            break

    with open("coins.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerows(allrows)


def get_coin_data(sym):
    with open("coins.csv", "r") as f:
        csv_reader = csv.reader(f, delimiter=",")
        lines = 1
        row_num = 1
        headers = ['Symbol', 'Name', 'WatchlistCount', '']
        csv_reader = list(csv_reader)
        for row in csv_reader:
            if len(row) == 0:
                csv_reader.remove(row)
        for i in range(1, 51):
            if (sym.upper()) in csv_reader[i]:
                row_num = i
                break
    driver.get(csv_reader[row_num][3])
    time.sleep(1.5)
    name = csv_reader[row_num][1]
    symbol = sym.upper()
    page_source = driver.page_source

    soup = BeautifulSoup(page_source, "html.parser")
    rank_det = soup.find_all('div', class_='cCqhlo')
    rank_det = [ele.text.strip() for ele in rank_det]
    rank_dets = rank_det[0].split()
    rank = rank_dets[1][:-6]
    watchlistcount = rank_dets[2]

    circules = soup.find_all('div', class_='supplyBlockPercentage___1g1SF')
    circules = [circule.text.strip() for circule in circules]
    circulation_percentage = circules[0]

    prices = soup.find_all('div', class_='priceValue___11gHJ')
    prices = [prices.text.strip() for prices in prices]
    price = prices[0]

    marketcaps = soup.find_all('div', class_='statsValue___2iaoZ')
    marketcaps = [marketcap.text.strip() for marketcap in marketcaps]
    valuebymarketcap = marketcaps[3]

    table = soup.find_all("td")
    tables1 = []
    for tab in table:
        tables = tab.find_all("span", class_="")
        tables1.append(tables)
    market_dominance = [ele.text.strip() for ele in tables1[5]][0]

    market_cap = [ele.text.strip() for ele in tables1[7]][0]

    athl = soup.find_all("small", class_="smallHeading___3DNdQ")
    athl = [ele.text.strip() for ele in athl]
    ath_date = athl[0][:12]
    atl_date = athl[1][:12]

    ath_price = [ele.text.strip() for ele in tables1[17]][0]
    atl_price = [ele.text.strip() for ele in tables1[18]][0]

    whatiscoin = ' '.join(text for text in between(soup.find('h2', text='What Is {} ({})?'.format(name, symbol)).next_sibling,
                                        soup.find('h3', text='Who Are the Founders of {}?'.format(name))))

    foundcoin = ' '.join(text for text in between(soup.find('h3', text='Who Are the Founders of {}?'.format(name)).next_sibling,
                                        soup.find('h4', text='What Makes {} Unique?'.format(name))))

    uniqueness = ' '.join(text for text in between(soup.find('h4', text='What Makes {} Unique?'.format(name)).next_sibling,
                                        soup.find(id='related-pages')))

    listlinks = soup.find_all("a", class_="modalLink___MQefI")
    listlinks = [ele['href'] for ele in listlinks]
    website_url = listlinks[0]

    res_arr = [symbol, name, watchlistcount, website_url, circulation_percentage, price, valuebymarketcap, market_dominance, rank,market_cap, ath_date, ath_price, atl_date, atl_price, whatiscoin, foundcoin, uniqueness]

    with open('coin_data_{}.csv'.format(str(time.strftime('%b-%d-%Y_%H%M', time.localtime()))),"w") as f:
        csvwriter = csv.writer(f)

        csvwriter.writerow(res_arr)

get_coin()
get_coin_data(input())
