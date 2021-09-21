# Cryptocurrencies
First we need to pull the data from coingecko.com

Imported CoinGeckoAPI from pycoingecko

Pulled with CoinGeckoAPI() naming as a cg

In cg.get_coins_market() stored list all supported coins price, market cap, volume, and market related data

All these data pulled by report as an array
```
report = cg.get_coins_markets(vs_currency='usd'
```
Now we can get market capitalization using this folloing code:
```
report[index]['market_cap'])
```
