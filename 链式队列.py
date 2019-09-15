#python实现常用的数据结构
#author by Liangwei

#链式队列

class Node(object):
    def __init__(self,value):
        self.data = value
        self.next = None
 
class Queue(object):
    def __init__(self):
        self.front = Node(None)
        self.rear = self.front

    #将新元素插入队尾
    def enQueue(self,element):
        n = Node(element)
        self.rear.next = n
        self.rear = n

    #删除队头元素
    #此处注意“队列”这种数据结构不能删除中间元素
    def deQueue(self):
        if self.is_empty():
            print('队空')
            return
        temp = self.front.next
        self.front.next = self.front.next.next
        if self.rear == temp:
            self.rear = self.front
        del temp
 
    def getHead(self):
        if self.is_empty():
            return '队空,无值输出'
        return self.front.next.data
 
    def is_empty(self):
        return self.rear == self.front

    #输出列
    def printQueue(self):
        cur = self.front.next
        while cur != None:
            print(cur.data)
            cur = cur.next

    #清空列
    def clear(self):
        while self.front.next != None:
            temp = self.front.next
            self.front.next = temp.next
        self.rear = self.front

    #列长
    def length(self):
        cur = self.front.next
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count
 
if __name__ == '__main__':

    
    queue = Queue()

    queue.enQueue('p')
    queue.enQueue('y')
    queue.enQueue('t')
    queue.enQueue('h')
    queue.enQueue('o')
    queue.enQueue('n')
    
    queue.printQueue()
    print()
    print(queue.is_empty())
    print(queue.length())
    print(queue.getHead())
    
    queue.deQueue()  
    print()
    queue.printQueue()
    print()
    print(queue.getHead())
    print()
    
    queue.clear()
    print(queue.length())
    print(queue.is_empty())
    print(queue.getHead())
