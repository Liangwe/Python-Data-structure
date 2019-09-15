#python实现常用的数据结构
#author by Liangwei

#线性表
#线性表的链式表示

class Node(object):
    """节点"""

    def __init__(self, elem):
        self.elem = elem
        self.next = None  # 初始设置下一节点为空


# 下面创建单链表，并实现其应有的功能

class SingleLinkList(object):
    """单链表"""
    
    def __init__(self, node=None):  # 使用一个默认参数，在传入头结点时则接收，在没有传入时，就默认头结点为空
        self.__head = node
        
    def init_list(self, data):  # 按列表给出 data,初始化列表
        self.__head = Node(data[0])
        p = self.__head  # 指针指向头结点
        for i in data[1:]:
            p.next = Node(i)  # 确定指针指向下一个结点
            p = p.next  # 指针滑动向下一个位置
        
    def is_empty(self):
        '''判断链表是否为空'''
        return self.__head == None

    def length(self):
        '''链表长度'''
        cur = self.__head   # 遍历节点
        count =  0            #记录数量
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        '''遍历整个列表'''
        cur = self.__head
        while cur != None:
            print(cur.elem, end=' ')
            cur = cur.next
        print("\n")

    def addhead(self, item):
        '''链表头部添加元素'''
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        '''链表尾部添加元素'''
        node = Node(item)
        # 由于特殊情况当链表为空时没有next，所以在前面要做个判断
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        '''指定位置添加元素'''
        if pos <= 0:
                # 如果pos位置在0或者以前，那么都当做头插法来做
            self.addhead(item)
        elif pos > self.length() - 1:
            # 如果pos位置比原链表长，那么都当做尾插法来做
            self.append(item)
        else:
            per = self.__head
            count = 0
            while count < pos - 1:
                count += 1
                per = per.next
            # 当循环退出后，pre指向pos-1位置
            node = Node(item)
            node.next = per.next
            per.next = node

    def remove(self, item):
        '''删除节点'''
        cur = self.__head
        pre = None
        while cur != None:
            if cur.elem == item:
                # 先判断该节点是否是头结点
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        '''查找节点是否存在'''
        cur = self.__head
        while cur:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == "__main__":
    
    

    #测试案例
    ll = SingleLinkList()
    print(ll.is_empty())
    print(ll.length())
   
    ll.init_list([1,5,6,65])#传入数组
    ll.travel()         #遍历输出
    ll.append(2)        #插入尾部
    ll.travel()
    ll.addhead(999)     #插入头部
    ll.travel()
    ll.insert(-3, 110)  #如果位置比0小插入头部，比len大插入尾部
    ll.travel()
    ll.insert(99, 111)
    ll.travel()
    print(ll.is_empty())
    print(ll.length())
    ll.remove(111)
    ll.travel()
    print(ll.search(22))
    print(ll.search(65))
