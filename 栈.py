#python实现常用的数据结构
#author by Liangwei

#栈

class Stack(object):
    """栈"""
    
    # 初始化栈为空列表
    def __init__(self):
        self.items = []
        
    def clearstack(self):
        self.items.clear()
        
    # 判断栈是否为空，返回布尔值
    def is_empty(self):
        return self.items == []

    # 返回栈顶元素 
    def gettop(self):
        if self.is_empty():  #一定要进行此步骤，否则会出现数组越界报错，下Pop同
            return '栈为空，无法进行你的操作'
        else:
            return self.items[-1]

    # 返回栈的大小
    def size(self):
        return len(self.items)

    # 把新的元素堆进栈里面
    def push(self, item):
        self.items.append(item)

    # 把栈顶元素丢出去,并且返回丢掉的数值
    def Pop(self):
        if self.is_empty():
            return '栈为空，无法进行你的操作'
        else:
            return self.items.pop()


if __name__ == "__main__":
    
    # 初始化一个栈对象
    my_stack = Stack()

    my_stack.push('p')
    my_stack.push('y')
    
    print (my_stack.size())
    print (my_stack.gettop())
    print (my_stack.Pop())
    my_stack.clearstack()  
    print (my_stack.gettop())
    print (my_stack.is_empty())
    my_stack.push('p')
    my_stack.push('y')
    my_stack.push('t')
    my_stack.push('h')
    my_stack.push('o')
    my_stack.push('n')
    print (my_stack.size())
    print (my_stack.Pop())
    print (my_stack.size())
    print (my_stack.is_empty())
    
