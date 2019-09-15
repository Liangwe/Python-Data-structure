#python实现常用的数据结构
#author by Liangwei

#排序算法
'''
排序方法	平均时间	最好时间	最坏时间	 	 
冒泡排序(稳定)	O(n^2)	        O(n)	        O(n^2)
选择排序(不稳定)O(n^2)	        O(n^2)	        O(n^2)
插入排序(稳定)  O(n^2)	        O(n)	        O(n^2)
希尔排序(不稳定)O(n^1.25)
归并排序(稳定)	O(nlogn)	O(nlogn)	O(nlogn)
快速排序(不稳定)O(nlogn)	O(nlogn)	O(n^2)
堆排序(不稳定)	O(nlogn)	O(nlogn)	O(nlogn)
计数排序(稳定)  O(n)
桶排序(不稳定)	O(n)	        O(n)	        O(n)
基数排序(稳定)	O(n)	        O(n)	        O(n)

附：O(1) < O(logn) < O(n) < O(nlogn) < O(n^2) < O(n^3) < O(2^n) < O(n!) < O(n^n)
最快的排序算法是桶排序，但缺陷很大，所以快速排序用的较多
'''
import time
def bubbleSort(nums):
    '''冒泡排序 '''
    for i in range(len(nums) - 1): 
        for j in range(len(nums) - i - 1): # 已排好序的部分不用再次遍历
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j] 
    return nums

def selectionSort(nums):
    '''选择排序'''
    for i in range(len(nums) - 1):  # 遍历 len(nums)-1 次
        minIndex = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[minIndex]:  # 更新最小值索引
                minIndex = j  
        nums[i], nums[minIndex] = nums[minIndex], nums[i] # 把最小数交换到前面
    return nums

def insertionSort(nums):
    '''插入排序'''
    for i in range(len(nums) - 1):  # 遍历 len(nums)-1 次
        curNum, preIndex = nums[i+1], i  # curNum 保存当前待插入的数
        while preIndex >= 0 and curNum < nums[preIndex]: # 将比 curNum 大的元素向后移动
            nums[preIndex + 1] = nums[preIndex]
            preIndex -= 1
        nums[preIndex + 1] = curNum  # 待插入的数的正确位置   
    return nums

def shellSort(nums):
    '''希尔排序'''
    lens = len(nums)
    gap = 1  
    while gap < lens // 3:
        gap = gap * 3 + 1  # 动态定义间隔序列
    while gap > 0:
        for i in range(gap, lens):
            curNum, preIndex = nums[i], i - gap  # curNum 保存当前待插入的数
            while preIndex >= 0 and curNum < nums[preIndex]:
                nums[preIndex + gap] = nums[preIndex] # 将比 curNum 大的元素向后移动
                preIndex -= gap
            nums[preIndex + gap] = curNum  # 待插入的数的正确位置
        gap //= 3  # 下一个动态间隔
    return nums

def mergeSort(nums):
    '''归并排序'''
    def merge(left, right):
        result = []  
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result = result + left[i:] + right[j:] # 剩余的元素直接添加到末尾
        return result
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = mergeSort(nums[:mid])
    right = mergeSort(nums[mid:])
    return merge(left, right)

def quickSort(nums):  # 这种写法的平均空间复杂度为 O(nlogn)
    '''快速排序'''
    if len(nums) <= 1:
        return nums
    pivot = nums[0]  # 基准值
    left = [nums[i] for i in range(1, len(nums)) if nums[i] < pivot] 
    right = [nums[i] for i in range(1, len(nums)) if nums[i] >= pivot]
    return quickSort(left) + [pivot] + quickSort(right)

def heapSort(nums):
    '''堆排序'''
    # 调整堆
    def adjustHeap(nums, i, size):
        # 非叶子结点的左右两个孩子
        lchild = 2 * i + 1
        rchild = 2 * i + 2
        # 在当前结点、左孩子、右孩子中找到最大元素的索引
        largest = i 
        if lchild < size and nums[lchild] > nums[largest]: 
            largest = lchild 
        if rchild < size and nums[rchild] > nums[largest]: 
            largest = rchild 
        # 如果最大元素的索引不是当前结点，把大的结点交换到上面，继续调整堆
        if largest != i: 
            nums[largest], nums[i] = nums[i], nums[largest] 
            # 第 2 个参数传入 largest 的索引是交换前大数字对应的索引
            # 交换后该索引对应的是小数字，应该把该小数字向下调整
            adjustHeap(nums, largest, size)
    # 建立堆
    def builtHeap(nums, size):
        for i in range(len(nums)//2)[::-1]: # 从倒数第一个非叶子结点开始建立大根堆
            adjustHeap(nums, i, size) # 对所有非叶子结点进行堆的调整
        # print(nums)  # 第一次建立好的大根堆
    # 堆排序 
    size = len(nums)
    builtHeap(nums, size) 
    for i in range(len(nums))[::-1]: 
        # 每次根结点都是最大的数，最大数放到后面
        nums[0], nums[i] = nums[i], nums[0] 
        # 交换完后还需要继续调整堆，只需调整根节点，此时数组的 size 不包括已经排序好的数
        adjustHeap(nums, 0, i) 
    return nums  # 由于每次大的都会放到后面，因此最后的 nums 是从小到大排列

def countingSort(nums):
    '''计数排序'''
    bucket = [0] * (max(nums) + 1) # 桶的个数
    for num in nums:  # 将元素值作为键值存储在桶中，记录其出现的次数
        bucket[num] += 1
    i = 0  # nums 的索引
    for j in range(len(bucket)):
        while bucket[j] > 0:
            nums[i] = j
            bucket[j] -= 1
            i += 1
    return nums

def bucketSort(nums, defaultBucketSize = 5):
    '''桶排序'''
    maxVal, minVal = max(nums), min(nums)
    bucketSize = defaultBucketSize  # 如果没有指定桶的大小，则默认为5
    bucketCount = (maxVal - minVal) // bucketSize + 1  # 数据分为 bucketCount 组
    buckets = []  # 二维桶
    for i in range(bucketCount):
        buckets.append([])
    # 利用函数映射将各个数据放入对应的桶中
    for num in nums:
        buckets[(num - minVal) // bucketSize].append(num)
    nums.clear()  # 清空 nums
    # 对每一个二维桶中的元素进行排序
    for bucket in buckets:
        insertionSort(bucket)  # 假设使用插入排序
        nums.extend(bucket)    # 将排序好的桶依次放入到 nums 中
    return nums

def radixSort(nums):
    '''基数排序'''
    mod = 10
    div = 1
    mostBit = len(str(max(nums)))  # 最大数的位数决定了外循环多少次
    buckets = [[] for row in range(mod)] # 构造 mod 个空桶
    while mostBit:
        for num in nums:  # 将数据放入对应的桶中
            buckets[num // div % mod].append(num)
        i = 0  # nums 的索引
        for bucket in buckets:  # 将数据收集起来
            while bucket:
                nums[i] = bucket.pop(0) # 依次取出
                i += 1
        div *= 10
        mostBit -= 1
    return nums

data_test = [23,1,53,654,54,16,65,3,155,506,10, 164, 234, 31, 3, 54,46,654,315]
print('跟在结果后面的是运行时长(s)')
print('冒泡排序：')
start = time.time()
print(bubbleSort(data_test))
end = time.time()
print(end-start)
print()

print('选择排序：')
start = time.time()
print(selectionSort(data_test))
end = time.time()
print(end-start)
print()

print('插入排序：')
start = time.time()
print(insertionSort(data_test))
end = time.time()
print(end-start)
print()

print('希尔排序：')
start = time.time()
print(shellSort(data_test))
end = time.time()
print(end-start)
print()

print('归并排序：')
start = time.time()
print(mergeSort(data_test))
end = time.time()
print(end-start)
print()

print('快速排序：')
start = time.time()
print(quickSort(data_test))
end = time.time()
print(end-start)
print()

print('堆排序：')
start = time.time()
print(heapSort(data_test))
end = time.time()
print(end-start)
print()

print('计数排序：')
start = time.time()
print(countingSort(data_test))
end = time.time()
print(end-start)
print()

print('桶排序：')
start = time.time()
print(bucketSort(data_test))
end = time.time()
print(end-start)
print()

print('基数排序：')
start = time.time()
print(radixSort(data_test))
end = time.time()
print(end-start)


