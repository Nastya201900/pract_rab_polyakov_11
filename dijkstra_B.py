# coding: utf-8

INF = 30000
ASCII = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

F = open("dijkstra.dat")
N = int(F.readline())

W = []
for i in range(N):
  Wi = list(map(int,F.readline().split()))
  for j in range(N):
    if Wi[j] < 0: Wi[j] = INF
  W.append( Wi )
F.close()

print("Весовая матрица графа: " )
for j in range(N):
  print("%4s" % ASCII[j], end="")
print("\n----", end="")
for j in range(N): print("----", end="")
print()

for i in range(N):
  for j in range(N):
    if W[i][j] == INF:
      print("   .", end="")
    else:
      print("%4d" % W[i][j], end="")
  print()

start = 0

selected = [False]*N
dist = [INF]*N
dist[start] = 0
V = start
minDist = 0
while minDist < INF:
  selected[V] = True
  # проверка маршрутов через вершину V
  for j in range(N):
    if dist[V] + W[V][j] < dist[j]:
      dist[j] = dist[V] + W[V][j]
    # поиск новой рабочей вершины dist[j] -> min
  minDist = INF
  for j in range(N):
    if not selected[j] and dist[j] < minDist:
      minDist = dist[j]
      V = j

print ( "\n      ", end="" )
for i in range(N):
  print( "{:>5s}".format(ASCII[i]), end="" )
print( "\n------", end="" )
for i in range(N):
  print ( "-----", end="" )
print ( " \ndist |", end="" )
for i in range(N):
  print ( "{:5d}".format(dist[i]), end="" )

print("\n");
print("Длина кратчайшего маршрута из вершины A в вершину",
      ASCII[N-1]  );
print( dist[N-1] )



