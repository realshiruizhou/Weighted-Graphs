from math import pi, acos, sin, cos
from heapq import heappush, heappop
import sys
import time
city_id = {}
id_location = {}
edges = {}


def calcd(y1, x1, y2, x2):
    y1 = float(y1)
    x1 = float(x1)
    y2 = float(y2)
    x2 = float(x2)
    if y1 - y2 == 0 and x1 - x2 == 0:
        return 0.0
    r = 3958.76
    y1 *= pi/180.0
    x1 *= pi/180.0
    y2 *= pi/180.0
    x2 *= pi/180.0
    return acos(sin(y1)*sin(y2) + cos(y1)*cos(y2)*cos(x2-x1)) * r


def dijkstra(start, goal):
    fringe = list()
    visited = set()
    heappush(fringe, (0, 0, city_id[start]))
    while len(fringe) > 0:
        v = heappop(fringe)
        if v[2] in visited:
            continue
        visited.add(v[2])
        if v[2] == city_id[goal]:
            return v[1]
        (y1, x1) = id_location[v[2]]
        for a in edges[v[2]]:
            (y2, x2) = id_location[a]
            distance_parent = calcd(y1, x1, y2, x2)
            heappush(fringe, (v[1] + distance_parent, v[1] + distance_parent, a))


def a_star(start, goal):
    (y, x) = id_location[city_id[goal]]
    fringe = list()
    visited = set()
    heappush(fringe, (0, 0, city_id[start]))
    while len(fringe) > 0:
        v = heappop(fringe)
        if v[2] in visited:
            continue
        visited.add(v[2])
        if v[2] == city_id[goal]:
            return v[1]
        (y1, x1) = id_location[v[2]]
        for a in edges[v[2]]:
            (y2, x2) = id_location[a]
            if float(y) - float(y2) == 0 and float(x) - float(x2) == 0:
                distance_goal = 0
            else:
                distance_goal = calcd(y, x, y2, x2)
            distance_parent = calcd(y1, x1, y2, x2)
            heappush(fringe, (distance_goal + v[1] + distance_parent, v[1] + distance_parent, a))


file = open("rrNodeCity.txt")
for line in file:
    a = line.split()
    if len(a) == 3:
        name = a[1] + " " + a[2]
    else:
        name = a[1]
    city_id[name] = a[0]
file2 = open("rrNodes.txt")
for line2 in file2:
    b = line2.split()
    id_location[b[0]] = (b[1], b[2])
file3 = open("rrEdges.txt")
for line3 in file3:
    c = line3.split()
    if c[0] in edges:
        temp = edges[c[0]]
        temp.append(c[1])
        edges[c[0]] = temp
    else:
        edges[c[0]] = [c[1]]
    if c[1] in edges:
        temp = edges[c[1]]
        temp.append(c[0])
        edges[c[1]] = temp
    else:
        edges[c[1]] = [c[0]]
start = time.perf_counter()
d = dijkstra(sys.argv[1], sys.argv[2])
end = time.perf_counter()
print("Dijkstra: " + str(d) + " miles in " + str(end - start) + " seconds")
start2 = time.perf_counter()
d2 = a_star(sys.argv[1], sys.argv[2])
end2 = time.perf_counter()
print("A*: " + str(d2) + " miles in " + str(end2 - start2) + " seconds")
