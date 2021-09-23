from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
report = cg.get_coins_markets(vs_currency='usd')