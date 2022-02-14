import sys


def way(gr, st, fn):
    big = 10 ** 20
    #словарь dist, содержит в себе минимальное расстояние от начала до точки, которая является ключом словаря
    dist = dict()
    #parent - содержит в себе путь
    parent = dict()
    for i in gr.keys():
        dist[i] = big
    dist[st] = 0
    #nds - список вершин, которые подлежат проверке
    nds = [st]
    #parent - хранит путь
    parent[st] = -1
    #находим все минимальные от начала до точки
    while nds:
        #определение вершины, с наименьшим расстоянием от текущей
        mn_dist = big
        mn_node = None
        for i in nds:
            if dist[i] < mn_dist:
                mn_node, mn_dist = i, dist[i]
        nds.remove(mn_node)
        #пересматриваем минимальные расстояния от начала, но уже через самую близкую точку
        for to, ln in gr[mn_node]:
            if dist[to] > mn_dist + ln:
                parent[to] = mn_node
                dist[to] = mn_dist + ln
                if to not in nds:
                    nds.append(to)

    #находим ответ
    ret = []
    xx = fn
    while xx != -1:
        ret.append(xx)
        xx = parent[xx]
    ret.reverse()
    return ret



#ввод данных
inp =  [i.rstrip() for i in sys.stdin]
#отделение начала - s, конца - f, от введенных данных
s, f = [int(i) for i in inp[-1].split()]
inp.remove(inp[-1])
g = dict()
g.setdefault([])
#заполнение данных в словаре g - хранилище  
for i in inp:
    x, y, z = [int(j) for j in i.rstrip().split()]
    g[x].append((y, z))
    g[y].append((x, z))

print(*way(g, s, f), sep=', ')