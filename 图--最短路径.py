#python实现常用的数据结构
#author by Liangwei

#图  最短路径问题，包含dijkstra、Floyd两种算法

inf = float('inf')
matrix_distance = [[0,1,12,inf,inf,inf],
                   [inf,0,9,3,inf,inf],
                   [inf,inf,0,inf,5,inf],
                   [inf,inf,4,0,13,15],
                   [inf,inf,inf,inf,0,4],
                   [inf,inf,inf,inf,inf,0]]

def dijkstra(matrix_distance, source_node):
    inf = float('inf')
    # init the source node distance to others
    dis = matrix_distance[source_node]
    node_nums = len(dis)
    flag = [0 for i in range(node_nums)]
    flag[source_node] = 1    
    for i in range(node_nums-1):
        min = inf
        #find the min node from the source node
        for j in range(node_nums):  #比较相邻节点的最短路径
            if flag[j] == 0 and dis[j] < min:
                min = dis[j]
                u = j
                
        flag[u] = 1  #访问过的置为1
        #update the dis 
        for v in range(node_nums):
            if flag[v] == 0 and matrix_distance[u][v] < inf:
                if dis[v] > dis[u] + matrix_distance[u][v]:
                    dis[v] = dis[u] + matrix_distance[u][v]                                 
    return dis

def Floyd(dis):   
    #min (Dis(i,j) , Dis(i,k) + Dis(k,j) )
    nums_vertex = len(dis[0])
    for k in range(nums_vertex):
        for i in range(nums_vertex):
            for j in range(nums_vertex):
                if dis[i][j] > dis[i][k] + dis[k][j]:
                    dis[i][j] = dis[i][k] + dis[k][j]
    return dis

print('该有向图为：')
for i in matrix_distance:
    for j in i:
        print (j, end = '  ')
    print()
print()
print('从v1节点出发的到各个点的最短路径（dijkstra算法）')
print(dijkstra(matrix_distance, 0))
print('从每个点依次出发到各个点对应的所有最短路径（Floyd算法）')
print(Floyd(matrix_distance))
