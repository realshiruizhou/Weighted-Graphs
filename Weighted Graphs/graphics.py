from math import pi, acos, sin, cos
from heapq import heappush, heappop
from tkinter import *
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
    root = Tk()
    root.geometry("1000x1000")
    c = Canvas(root, height=1000, width=1000)
    c.pack()
    for each in edges:
        for child in edges[each]:
            (e, f) = id_location[each]
            (g, h) = id_location[child]
            (e1, f1) = (float(e), float(f))
            (g1, h1) = (float(g), float(h))
            c.create_line((h1 + 150) * 10, 750 - (g1 * 10), (f1 + 150) * 10, 750 - (e1 * 10))
    c.update()
    (y, x) = id_location[city_id[goal]]
    fringe = list()
    visited = set()
    heappush(fringe, (0, 0, city_id[start], (y, x)))
    count = 0
    while len(fringe) > 0:
        v = heappop(fringe)
        if v[2] in visited:
            continue
        visited.add(v[2])
        count += 1
        (y1, x1) = id_location[v[2]]
        (y3, x3) = v[3]
        (a1, b1) = (float(x1), float(y1))
        (a2, b2) = (float(x3), float(y3))
        if v[1] != 0:
            c.create_line((a1 + 150) * 10, 750 - b1 * 10, (a2 + 150) * 10, 750 - b2 * 10, fill="red")
            if count == 1000:
                c.update()
                count = 0
        if v[2] == city_id[goal]:
            root.mainloop()
            return v[1]
        for a in edges[v[2]]:
            (y2, x2) = id_location[a]
            distance_parent = calcd(y1, x1, y2, x2) * 100
            heappush(fringe, (v[1] + distance_parent, v[1] + distance_parent, a, (y1, x1)))


def a_star(start, goal):
    root = Tk()
    root.geometry("1000x1000")
    c = Canvas(root, height=1000, width=1000)
    c.pack()
    for each in edges:
        for child in edges[each]:
            (e, f) = id_location[each]
            (g, h) = id_location[child]
            (e1, f1) = (float(e), float(f))
            (g1, h1) = (float(g), float(h))
            c.create_line((h1 + 150) * 10, 750 - (g1 * 10), (f1 + 150) * 10, 750 - (e1 * 10))
    c.update()
    (y, x) = id_location[city_id[goal]]
    fringe = list()
    visited = set()
    heappush(fringe, (0, 0, city_id[start], (y, x)))
    count = 0
    while len(fringe) > 0:
        v = heappop(fringe)
        if v[2] in visited:
            continue
        visited.add(v[2])
        count += 1
        (y1, x1) = id_location[v[2]]
        (y3, x3) = v[3]
        (a1, b1) = (float(x1), float(y1))
        (a2, b2) = (float(x3), float(y3))
        print("Parent " + y3 + ", " + x3)
        print("Child " + y1 + ", " + x1)
        if v[1] != 0:
            c.create_line((a2 + 150) * 10, 750 - (b2 * 10), (a1 + 150) * 10, 750 - (b1 * 10), fill="red")
            if count == 100:
                c.update()
                count = 0
        if v[2] == city_id[goal]:
            root.mainloop()
            return v[1]
        for a in edges[v[2]]:
            (y2, x2) = id_location[a]
            distance_goal = calcd(y, x, y2, x2)
            distance_parent = calcd(y1, x1, y2, x2)
            heappush(fringe, (distance_goal + v[1] + distance_parent, v[1] + distance_parent, a, (y1, x1)))


def create_map():
    root = Tk()
    root.geometry("1000x1000")
    c = Canvas(root, height=1000, width=1000)
    for each in edges:
        for child in edges[each]:
            (e, f) = id_location[each]
            (g, h) = id_location[child]
            (e1, f1) = (float(e), float(f))
            (g1, h1) = (float(g), float(h))
            c.create_line((h1 + 150) * 10, 750 - (g1 * 10), (f1 + 150) * 10, 750 - (e1 * 10))
    c.pack()
    root.mainloop()


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
# "Ciudad Juarez", "Montreal"
# "Albuquerque", "Las Vegas"
dijkstra("Columbus", "Dallas")
a_star("Columbus", "Dallas")
# create_map()
