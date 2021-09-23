from src import *

n = int(input('Enter: '))

def func(x):
    list = []
    for _ in range(x):
        list.append((int(report[_]['market_cap']), report[_]['name']))

    for i in range(x):
        print(i + 1, '-', list[i][1], list[i][0])

func(n)