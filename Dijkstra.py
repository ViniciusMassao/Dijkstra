infinity = 999
maximum = 6
member = 1
nonmember = 0

class Grafo:
    def __init__(self, tam):
        #self.N = [[0]*N for x in range(N)]
        self.tam = tam
        self.mat = []
        self.v = []

    def printMatrix(self):
        for i in range(self.tam):
            print(self.mat[i])
        print("")
    
    def Dijkstra(self, start, goal):
        menorDist = 0
        novaDist = 0
        dc = 0
        dist = [0] * maximum
        perm = [0] * maximum
        caminho = [0] * maximum
        for i in range(maximum):
            perm[i] = nonmember
            dist[i] = infinity
        perm[start] = member
        dist[start] = 0
        atual = start
        k = atual
        while (atual != goal):
            menorDist = infinity
            dc = dist[atual]
            for i in range(maximum - 1):
                if(perm[i] == nonmember):
                    novaDist = dc + self.mat[atual][i]
                    if(novaDist < dist[i]):
                        dist[i] = novaDist
                        caminho[i] = atual
                    if(dist[i] < menorDist):
                        menorDist = dist[i]
                        k = i
            if(atual == k):
                print("CAMINHO NAO EXISTE")
                return
            atual = k
            perm[atual] = member
        print("RESULTADO: ")
        numCaminho = goal
        print(self.v[goal] + " <- ")
        while(numCaminho != start):
            print(self.v[caminho[numCaminho]], end = '')
            numCaminho = caminho[numCaminho]
            if(numCaminho != start):
                print(" <- ")
        print("")
        print("CUSTO: " + str(dist[goal]))

if __name__ == "__main__":
    N = 5
    g = Grafo(N)
    g.v.append("A")
    g.v.append("B")
    g.v.append("C")
    g.v.append("D")
    g.v.append("E")
    g.mat = [[infinity, 2, infinity, infinity, 10],
            [infinity, infinity, 3, infinity, 6],
            [infinity, infinity, infinity, 2, infinity],
            [infinity, infinity, infinity, infinity, infinity],
            [infinity, infinity, 8, 5, infinity]
            ]
    #g.printMatrix()
    start = g.v.index("A")
    goal = g.v.index("D")
    g.Dijkstra(start, goal)
    print()
    g.mat = [[infinity, 10, 5, infinity, infinity],
                [infinity, infinity, 2, 1, infinity],
                [infinity, 3, infinity, 9, 2],
                [infinity, infinity, infinity, infinity, 4],
                [7, infinity, infinity, 6, infinity]
                ]
    #g.printMatrix()
    start = g.v.index("D")
    goal = g.v.index("B")
    g.Dijkstra(start, goal)