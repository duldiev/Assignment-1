<h3>Cryptocurrencies<h3/><br/>
First we need to pull the data from coingecko.com<br/>
Imported CoinGeckoAPI from pycoingecko<br/>
Pulled with CoinGeckoAPI() naming as a cg<br/>
In cg.get_coins_market() stored list all supported coins price, market cap, volume, and market related data<br/>
All these data pulled by report as an array
```
report = cg.get_coins_markets(vs_currency='usd'
```
Now we can get market capitalization using this folloing code:
```
report[_]['market_cap'])
```
