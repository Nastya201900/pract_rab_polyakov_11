WMAX = 15
W = [6, 4, 3, 2, 5]  # вес
P = [5, 3, 1, 3, 6]  # стоимость

print("Вместимость рюкзака ", WMAX)
print("Имеющиеся предметы (вес, стоимость):")
for pair in zip(W, P):
    print(pair, end=" ")
print("\n")

NStones = len(P)

T = []
for i in range(NStones):
    T.append([0] * (WMAX + 1))
for w in range(W[0], WMAX + 1):
    T[0][w] = P[0]


def showTable(P, T):
    print("   ", end="");
    for w in range(WMAX + 1):
        print("{:3d}".format(w), end="")
    print("\n---", end="")
    for i in range(WMAX + 1):
        print("---", end="")
    print()
    for i in range(NStones):
        print("{:2d}:".format(P[i]), end="");
        for w in range(WMAX + 1):
            print("{:3d}".format(T[i][w]), end="")
        print()
    print()


for i in range(1, NStones):
    for w in range(1, WMAX + 1):
        t0 = T[i - 1][w]
        if w >= W[i]:
            t1 = T[i - 1][w - W[i]] + P[i]
            T[i][w] = max(t0, t1)
        else:
            T[i][w] = t0

showTable(P, T)

print("Оптимальное решение: w =", T[NStones - 1][WMAX])
print("Берем предметы (вес, стоимость): ");
i = NStones - 1
w = WMAX
p0 = T[NStones - 1][WMAX]
while p0 > 0:
    while i >= 0 and T[i][w] == p0:
        i -= 1
    if i < 0:
        print((w, p0))
        break;
    print((W[i + 1], P[i + 1]), ' ', end="");
    p0 -= P[i + 1]
    w -= W[i + 1]
