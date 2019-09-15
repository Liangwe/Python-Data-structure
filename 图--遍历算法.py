#python实现常用的数据结构
#author by Liangwei

#图的遍历  深度优先（递归和堆栈）和广度优先

def BFS(graph, s):    #广度优先与二叉树的层序遍历类似
    '''广度优先'''
    queue = []
    result = []
    queue.append(s)
    seen = set()
    seen.add(s)
    while len(queue) > 0:
        vertex = queue.pop(0)
        nodes = graph[vertex]
        for node in nodes:
            if node not in seen:
                queue.append(node)
                seen.add(node)
        result.append(vertex)
    return result
        
def DFS(graph, s):    #深度优先与二叉树的先序遍历类似
    '''深度优先堆栈法'''
    result = []
    stack = []
    stack.append(s)
    seen = set()
    seen.add(s)
    while len(stack) > 0:
        vertex = stack.pop()
        nodes  = graph[vertex]
        for node in nodes:
            if node not in seen:
                stack.append(node)
                seen.add(node)
        result.append(vertex)
    return result

def DFS1(graph, s, queue=[]):
    '''深度优先递归法'''
    queue.append(s)
    for i in graph[s][::-1]:  #必须反向排序这个对应的列表，否则是广度优先遍历
        if i not in queue:
            DFS1(graph, i, queue)
    return queue


graph = {
        'a' : ['b', 'c'],
        'b' : ['a', 'c', 'd'],
        'c' : ['a','b', 'd','e'],
        'd' : ['b' , 'c', 'e', 'f'],
        'e' : ['c', 'd'],
        'f' : ['d']
        }
print('该图为：')
print(graph,'\n')
print('从a出发的广度优先搜索结果：')
print(BFS(graph, 'a'),'\n')
print('从a出发的深度优先搜索结果（堆栈）：')
print(DFS(graph, 'a'),'\n')
print('从a出发的深度优先搜索结果（递归）：')
print(DFS1(graph, 'a'))
