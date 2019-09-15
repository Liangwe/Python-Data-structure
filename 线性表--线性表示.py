#python实现常用的数据结构
#author by Liangwei

#线性表
#线性表的顺序表示
class Lnode(object):
    """节点"""
    
    def __init__(self,last):#线性表定义
        self.data = [None for i in range(100)]
        self.last = last  #线性表长度


# 1.初始化建立空的线性表
def MakeEmpty(num):
  PtrL = Lnode(num)
  return PtrL

# 2.查找给定值的位置
def Find(x, L):
  i =0
  while(i <= L.last and L.data[i] != x):
    i+=1
  if(i> L.last):
    return False  #不符合要求输出False
  else:
    return i


# 3.插入（在第i(0<=i<=n)位置上插入一个值为x的新元素）
def Insert(x,i,L):
  if i<0 or i>L.last:
    print("位置不合理")
    return
  else:
    for j in range(L.last,i-1,-1):
      L.data[j+1] = L.data[j]
    L.data[i] = x
    L.last+=1
  return

# 4.删除第i(0<=i<=n-1)个位置上的元素
def Delete(i,L):
  if i<0 or i>=L.last:
    print("不存在该元素")
    return
  else:
    for j in range(i,L.last-1):
      L.data[j] = L.data[j+1]
    L.last -=1
    return


# 1、测试建立空的线性表
s = MakeEmpty(10)
print(s.data[0:s.last])
print(s.last)

# 2、测试查找函数
num = [0,1,2,3,4,5,6,7,8,9]
L = Lnode(10)
for i in range(10):
  L.data[i] = num[i]
print("建立新的线性表")
print(L.data[0:L.last])
print("查找元素2")
print("下标为：")
print(Find(2,L)) #此2非彼2，这里是第二个数的意思 不是数组下标
print("查找元素12")
print("下标为：")
print(Find(12,L)) 

# 3、测试插入函数
print("在位序3插入元素6")
Insert(6,3,L)
print(L.data[0:L.last])

# 4、测试删除函数
print("删除位序5的元素")
Delete(5,L)
print(L.data[0:L.last])
