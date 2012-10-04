import heapq

def make_link(G, num, city1, city2, flight_duration,
              departure, arrival, cost):  
    # create links between two cities, links are flights.
    if city1 not in G:
        G[city1] = {}
    if city2 not in G[city1]:
        G[city1][city2] = {}
    G[city1][city2][num] = (cost, departure, arrival, flight_duration)
    return G

def create_connection_graph(data):
    G = {}
    for flight in data:
        (num, city1, city2, dept, arrv, cost) = flight
        dept = int(dept.replace(':', '', 1))
        deptmin = (dept/100)*60  + dept%100
        arrv = int(arrv.replace(':', '', 1))
        arrvmin  = (arrv/100)*60 + arrv%100
        durn = arrvmin - deptmin
        make_link(G, num, city1, city2, durn, deptmin, arrvmin, cost)            
    return G
                           
def find_best_flights(flights, origin, destination):
    # A dijkstra implementation
    G = create_connection_graph(flights)
    heap = []
    heapq.heappush(heap, (0,0,0,[],[origin]))
    paths = {origin:[origin]}
    while len(heap) != 0:
        (fcost, fdurn, farrv, flights, path) = heapq.heappop(heap)
        w = path[-1]
        if w == destination:
            return flights
        for x in G[w]:
            for flight in G[w][x]:
                (cost, dept, arrv, durn) = G[w][x][flight]
                if dept > farrv:
                    new_cost = cost + fcost
                    if fdurn == 0:
                        new_durn = arrv - dept
                    else:
                        new_durn = fdurn + (arrv - farrv)
                    new_path = path + [x]
                    new_flights = flights + [flight]
                    heapq.heappush(heap, (new_cost, new_durn, arrv,
                                          new_flights, new_path))
    return None

    


