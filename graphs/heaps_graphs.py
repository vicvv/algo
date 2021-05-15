'''
There are n cities connected by m flights. Each flight starts from city 
u and arrives at v with a price w.

Now given all the cities and flights, together with starting city src and 
the destination dst, your task is to find the cheapest price from src to dst with 
up to k stops. If there is no such route, output -1.
'''


import collections
import heapq
def findCheapestPrice(n, flights, src, dst, stops):
    dic = collections.defaultdict(dict)
    for start, destination, cost in flights:
        dic[start][destination] = cost
    print(dic)
    heap = [(0, src, stops + 1)]
    
    while heap:
        cost, current, stops = heapq.heappop(heap)
        print(stops)
        if current == dst:
            return cost
        if stops > 0:
            if current not in dic:
                continue
            for i in dic[current]:
                heapq.heappush(heap, (cost + dic[current][i], i, stops - 1))
    return -1

n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0 
dst = 2 
k = 1
print(findCheapestPrice(n, flights, src, dst, k))