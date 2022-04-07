# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000434ba1/0000000000434ad6#problem
# O(nlogn+mlogm)
for _ in range(int(input())):
    __ = int(input())
    odds = []
    evens = []
    places = []
    numbers = map(int, input().split())
    for i in numbers:
        is_odd = i % 2
        places.append(is_odd)
        if is_odd:
            odds.append(i)
        else:
            evens.append(i)
    evens.sort()
    odds.sort(reverse=True)
    print('Case #' + str(_+1), end=': ')
    for idx, i in enumerate(places):
        places[idx] = str(odds.pop()) if i else str(evens.pop())
    print(' '.join(places))
