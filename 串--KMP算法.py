#python实现常用的数据结构
#author by Liangwei

#串  python中串较为简单故这里只说重要的串的模式匹配  
#串的KMP算法

def kmp(mom_string,son_string):
    
    # 传入一个母串和一个子串
    if type(mom_string) is not str or type(son_string) is not str:
        return '其中有不为字符串的'
    if len(son_string) == 0:
        return '子串为空'
    if len(mom_string) == 0:
        return '母串为空'
    
    #求next数组
    next = [-1]*len(son_string)
    if len(son_string)>1:
        next[1] = 0
        i,j = 1,0
        while i < len(son_string)-1:
            if j == -1 or son_string[i] == son_string[j]:
                i += 1
                j += 1
                next[i] = j
            else:
                j=next[j]
                
    # kmp框架
    m = s = 0                #母指针和子指针初始化为0
    while(s < len(son_string) and m < len(mom_string)):
        # 匹配成功,或者遍历完母串匹配失败退出
        if s == -1 or mom_string[m] == son_string[s]:
            m += 1
            s += 1
        else:
            s = next[s]
 
    if s == len(son_string):#匹配成功
        return m-s
    return '匹配失败'


# 测试
mom_string='ababababca'
son_string='babd'
print('母串为:' + str(mom_string))
print('子串为:' + str(son_string))
try:
    n=kmp(mom_string,son_string)+1
    print('子串出现在母串的第' + str(n) + '位')
except:
    print(kmp(mom_string,son_string))



