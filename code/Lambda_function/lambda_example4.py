import heapq
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))


portfolio = [
{'nazwa': 'IBM', 'udzialy': 100, 'cena': 91.1},
{'nazwa': 'AAPL', 'udzialy': 50, 'cena': 543.22},
{'nazwa': 'FB', 'udzialy': 200, 'cena': 21.09},
{'nazwa': 'HPQ', 'udzialy': 35, 'cena': 31.75},
{'nazwa': 'YHOO', 'udzialy': 45, 'cena': 16.35},
{'nazwa': 'ACME', 'udzialy': 75, 'cena': 115.65}
]

tanie = heapq.nsmallest(3, portfolio, key=lambda s: s['cena'])
drogie = heapq.nlargest(3, portfolio, key=lambda s: s['cena'])

print(tanie)
print(drogie)