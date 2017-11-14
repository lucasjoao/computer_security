# -*- coding: utf-8 -*-
from lxml import html
import requests
import pandas as pd
import matplotlib.ticker
import matplotlib.pyplot as plt
import numpy
import sys

###############################################################################
# programa somente funciona com python 2, por isso possui o seguinte check:
if sys.version_info[0] >= 3:
    raise Exception("Executar com Python 2.")
###############################################################################

###############################################################################
# um dict para cada coin que possuira todos os dados coletados
LTC = {'marketcap': [], 'price': [], 'volume': []}
MONA = {'marketcap': [], 'price': [], 'volume': []}
DOGE = {'marketcap': [], 'price': [], 'volume': []}
NEO = {'marketcap': [], 'price': [], 'volume': []}
XEM = {'marketcap': [], 'price': [], 'volume': []}
STEEM = {'marketcap': [], 'price': [], 'volume': []}
XMR = {'marketcap': [], 'price': [], 'volume': []}
BCN = {'marketcap': [], 'price': [], 'volume': []}
BTC = {'marketcap': [], 'price': [], 'volume': []}

# dict que associa os dicts declarados previamente com os seus respectivos ids
# utilizados no site https://coinmarketcap.com/
ALTCOINS = {'id-litecoin': LTC,
            'id-monacoin': MONA,
            'id-dogecoin': DOGE,
            'id-neo': NEO,
            'id-nem': XEM,
            'id-steem': STEEM,
            'id-monero': XMR,
            'id-bytecoin-bcn': BCN,
            'id-bitcoin': BTC}
###############################################################################

###############################################################################
# inicio do parser que acessa os dados historicos em https://coinmarketcap.com/
# e pega os valores desejados para que alimente os dicts ja declarados

# todas as urls que possuem dados historicos do ultimo ano
urls = []
urls.append('https://coinmarketcap.com/historical/20171112/')
urls.append('https://coinmarketcap.com/historical/20171105/')
urls.append('https://coinmarketcap.com/historical/20171029/')
urls.append('https://coinmarketcap.com/historical/20171022/')
urls.append('https://coinmarketcap.com/historical/20171015/')
urls.append('https://coinmarketcap.com/historical/20171008/')
urls.append('https://coinmarketcap.com/historical/20171001/')
urls.append('https://coinmarketcap.com/historical/20170924/')
urls.append('https://coinmarketcap.com/historical/20170917/')
urls.append('https://coinmarketcap.com/historical/20170910/')
urls.append('https://coinmarketcap.com/historical/20170903/')
urls.append('https://coinmarketcap.com/historical/20170827/')
urls.append('https://coinmarketcap.com/historical/20170820/')
urls.append('https://coinmarketcap.com/historical/20170813/')
urls.append('https://coinmarketcap.com/historical/20170806/')
urls.append('https://coinmarketcap.com/historical/20170730/')
urls.append('https://coinmarketcap.com/historical/20170723/')
urls.append('https://coinmarketcap.com/historical/20170716/')
urls.append('https://coinmarketcap.com/historical/20170709/')
urls.append('https://coinmarketcap.com/historical/20170702/')
urls.append('https://coinmarketcap.com/historical/20170625/')
urls.append('https://coinmarketcap.com/historical/20170618/')
urls.append('https://coinmarketcap.com/historical/20170611/')
urls.append('https://coinmarketcap.com/historical/20170604/')
urls.append('https://coinmarketcap.com/historical/20170528/')
urls.append('https://coinmarketcap.com/historical/20170521/')
urls.append('https://coinmarketcap.com/historical/20170514/')
urls.append('https://coinmarketcap.com/historical/20170507/')
urls.append('https://coinmarketcap.com/historical/20170430/')
urls.append('https://coinmarketcap.com/historical/20170423/')
urls.append('https://coinmarketcap.com/historical/20170416/')
urls.append('https://coinmarketcap.com/historical/20170409/')
urls.append('https://coinmarketcap.com/historical/20170402/')
urls.append('https://coinmarketcap.com/historical/20170326/')
urls.append('https://coinmarketcap.com/historical/20170319/')
urls.append('https://coinmarketcap.com/historical/20170312/')
urls.append('https://coinmarketcap.com/historical/20170305/')
urls.append('https://coinmarketcap.com/historical/20170226/')
urls.append('https://coinmarketcap.com/historical/20170219/')
urls.append('https://coinmarketcap.com/historical/20170212/')
urls.append('https://coinmarketcap.com/historical/20170205/')
urls.append('https://coinmarketcap.com/historical/20170129/')
urls.append('https://coinmarketcap.com/historical/20170122/')
urls.append('https://coinmarketcap.com/historical/20170115/')
urls.append('https://coinmarketcap.com/historical/20170108/')
urls.append('https://coinmarketcap.com/historical/20170101/')
urls.append('https://coinmarketcap.com/historical/20161225/')
urls.append('https://coinmarketcap.com/historical/20161218/')
urls.append('https://coinmarketcap.com/historical/20161211/')
urls.append('https://coinmarketcap.com/historical/20161204/')
urls.append('https://coinmarketcap.com/historical/20161127/')
urls.append('https://coinmarketcap.com/historical/20161120/')
urls.append('https://coinmarketcap.com/historical/20161113/')

for url in urls:
    page = requests.get(url)
    tree = html.fromstring(page.content)

    for idcoin, coin in ALTCOINS.iteritems():
        # xpath e utilizado para acessar o conteudo html
        tr = '//tr[@id="{}"]'.format(idcoin)

        td_class = '//td[@class="no-wrap market-cap text-right"]/text()'
        cap = tree.xpath(''.join((tr, td_class)))
        clean_cap = float(cap[0].strip().replace('$', '').replace(',', ''))

        a_price = '//a[@class="price"]/text()'
        price = tree.xpath(''.join((tr, a_price)))
        clean_price = float(price[0].replace('$', ''))

        a_volume = '//a[@class="volume"]/@data-usd'
        volume = tree.xpath(''.join((tr, a_volume)))
        clean_volume = round(float(volume[0].replace('$', '').replace(',', '')),
                             2)

        # valores que alimentam as listas dentro dos dicts sao ja sao limpos no
        # momento da extracao
        coin['marketcap'].append(clean_cap)
        coin['price'].append(clean_price)
        coin['volume'].append(clean_volume)
###############################################################################

###############################################################################
# dicts auxiliares para serem utilizados nos calculos estatisticos

MARKETCAP = {'LTC': LTC['marketcap'],
             'MONA': MONA['marketcap'],
             'DOGE': DOGE['marketcap'],
             'NEO': NEO['marketcap'],
             'XEM': XEM['marketcap'],
             'STEEM': STEEM['marketcap'],
             'XMR': XMR['marketcap'],
             'BCN': BCN['marketcap'],
             'BTC': BTC['marketcap']}

PRICE = {'LTC': LTC['price'], 'MONA': MONA['price'], 'DOGE': DOGE['price'],
         'NEO': NEO['price'], 'XEM': XEM['price'], 'STEEM': STEEM['price'],
         'XMR': XMR['price'], 'BCN': BCN['price'], 'BTC': BTC['price']}

VOLUME = {'LTC': LTC['volume'], 'MONA': MONA['volume'], 'DOGE': DOGE['volume'],
          'NEO': NEO['volume'], 'XEM': XEM['volume'], 'STEEM': STEEM['volume'],
          'XMR': XMR['volume'], 'BCN': BCN['volume'], 'BTC': BTC['volume']}
###############################################################################

###############################################################################
# calculo e plotagem dos coeficientes de correlacao por pearson para market
# cap, volume e preco

fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(pd.DataFrame(data=MARKETCAP).corr(), vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = numpy.arange(0, 9, 1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(MARKETCAP.keys())
ax.set_yticklabels(MARKETCAP.keys())
plt.title(u'Correlação por Pearson do market cap no último ano')
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(pd.DataFrame(data=PRICE).corr(), vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = numpy.arange(0, 9, 1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(PRICE.keys())
ax.set_yticklabels(PRICE.keys())
plt.title(u'Correlação por Pearson do preço no último ano')
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(pd.DataFrame(data=VOLUME).corr(), vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = numpy.arange(0, 9, 1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(VOLUME.keys())
ax.set_yticklabels(VOLUME.keys())
plt.title(u'Correlação por Pearson do volume de transação no último ano')
plt.show()
###############################################################################

###############################################################################
# valores do bitcoin so foram utilizados em uma comparacao geral, agora nao
# sao mais necessarios
del MARKETCAP['BTC']
del PRICE['BTC']
del VOLUME['BTC']
###############################################################################

###############################################################################
# calculo e plotagem das medias do market cap, preço e volume

fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.plot(pd.DataFrame(data=MARKETCAP).mean())
y_formatter = matplotlib.ticker.FormatStrFormatter('$%1.2f')
ax.yaxis.set_major_formatter(y_formatter)
ax.grid(True)
plt.title(u'Média em dólares do market cap no último ano')
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.plot(pd.DataFrame(data=PRICE).mean())
y_formatter = matplotlib.ticker.FormatStrFormatter('$%1.2f')
ax.yaxis.set_major_formatter(y_formatter)
ax.grid(True)
plt.title(u'Média em dólares do preço no último ano')
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.plot(pd.DataFrame(data=VOLUME).mean())
y_formatter = matplotlib.ticker.FormatStrFormatter('$%1.2f')
ax.yaxis.set_major_formatter(y_formatter)
ax.grid(True)
plt.title(u'Média em dólares do volume de transação no último ano')
plt.show()
###############################################################################

###############################################################################
# calculo e plotagem dos desvios padroes do market cap, preço e volume

fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.plot(pd.DataFrame(data=MARKETCAP).std())
y_formatter = matplotlib.ticker.FormatStrFormatter('$%1.2f')
ax.yaxis.set_major_formatter(y_formatter)
ax.grid(True)
plt.title(u'Desvio padrão do market cap no último ano')
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.plot(pd.DataFrame(data=PRICE).std())
y_formatter = matplotlib.ticker.FormatStrFormatter('$%1.2f')
ax.yaxis.set_major_formatter(y_formatter)
ax.grid(True)
plt.title(u'Desvio padrão do preço no último ano')
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.plot(pd.DataFrame(data=VOLUME).std())
y_formatter = matplotlib.ticker.FormatStrFormatter('$%1.2f')
ax.yaxis.set_major_formatter(y_formatter)
ax.grid(True)
plt.title(u'Desvio padrão do volume de transação no último ano')
plt.show()
###############################################################################

###############################################################################
# calculo e plotagem dos coeficientes de correlacao por pearson entre market
# cap, volume e preco de cada altcoin analisada

fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(pd.DataFrame(data=LTC).corr(), vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = numpy.arange(0, 3, 1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(LTC.keys())
ax.set_yticklabels(LTC.keys())
plt.title(u'Correlação por Pearson do market cap, preço e volume do LTC')
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(pd.DataFrame(data=MONA).corr(), vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = numpy.arange(0, 3, 1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(MONA.keys())
ax.set_yticklabels(MONA.keys())
plt.title(u'Correlação por Pearson do market cap, preço e volume do MONA')
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(pd.DataFrame(data=DOGE).corr(), vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = numpy.arange(0, 3, 1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(DOGE.keys())
ax.set_yticklabels(DOGE.keys())
plt.title(u'Correlação por Pearson do market cap, preço e volume do DOGE')
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(pd.DataFrame(data=NEO).corr(), vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = numpy.arange(0, 3, 1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(NEO.keys())
ax.set_yticklabels(NEO.keys())
plt.title(u'Correlação por Pearson do market cap, preço e volume do NEO')
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(pd.DataFrame(data=XEM).corr(), vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = numpy.arange(0, 3, 1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(XEM.keys())
ax.set_yticklabels(XEM.keys())
plt.title(u'Correlação por Pearson do market cap, preço e volume do XEM')
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(pd.DataFrame(data=STEEM).corr(), vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = numpy.arange(0, 3, 1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(STEEM.keys())
ax.set_yticklabels(STEEM.keys())
plt.title(u'Correlação por Pearson do market cap, preço e volume do STEEM')
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(pd.DataFrame(data=XMR).corr(), vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = numpy.arange(0, 3, 1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(XMR.keys())
ax.set_yticklabels(XMR.keys())
plt.title(u'Correlação por Pearson do market cap, preço e volume do XMR')
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(pd.DataFrame(data=BCN).corr(), vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = numpy.arange(0, 3, 1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(BCN.keys())
ax.set_yticklabels(BCN.keys())
plt.title(u'Correlação por Pearson do market cap, preço e volume do BCN')
plt.show()
###############################################################################
