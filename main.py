from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
report = cg.get_coins_markets(vs_currency='usd')

n = int(input('Enter: '))
list = []
for _ in range(n):
    list.append((int(report[_]['market_cap']), report[_]['name']))

def bubbleSort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

bubbleSort(list)

for i in range(n):
    print(i + 1, '-', list[i][1], list[i][0])