# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
"""
排序算法稳定性：https://baike.baidu.com/item/%E6%8E%92%E5%BA%8F%E7%AE%97%E6%B3%95%E7%A8%B3%E5%AE%9A%E6%80%A7/9763250?fr=aladdin
"""
"""
时间复杂度：
    O(1) 代码在执行过程中没有任何循环
    O(n) 代码包含一个循环逻辑
    O(logn) nci执行的只是数据的一部分，我们的遍历越来越接近终点
    O(n2) 循环逻辑有两层
"""

"""
冒泡：依次比较两个相邻元素，若前一元素大于后一元素则交换，直至最后一个元素即为最大，然后重新从首元素开始重复同样的操作，..., （除了最后一个元素）
    如同水中的气泡，依次将最大或者最小元素气泡浮出水面， 每一趟都找出最大的元素
    算法复杂度：O(n^2), 稳定
    最好的时间复杂度是o(n)--当列表的初始状态是正序的时候， 最欢时候的事件复杂度是o(n^2), 所以平均事件复杂度是o(n^2)
    稳定性：冒泡排序就是把小的元素往前调或者把大的元素往后调，比较的是相邻两个元素，交换也是发生在这两个元素之间，所以，如果两个元素相等，就不会
        再交换，如果两个相等的元素没有相邻，那么即使通过前面的两两交换把两个相邻起来，这时候也不会交换，所以相同元素的前后顺序并没有改变，所以冒泡排序
        是一种稳定排序算法
        
        for i in range(len(nums)-1):
            for j in range(len(nums)-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        
"""


def bubbleSort(nums):
    for i in range(len(nums)-1):
        # flag = True
        for j in range(len(nums)-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                # flag = False
        # if flag:
        #     print("没有交换，说明列表已经有序，不需要再排序", nums, i)
        #     break

    print(nums)


"""
选择排序：首先初始化最小元素索引值为首元素，依次遍历待排序数列，若遇到小于该最小索引位置处的元素则刷新最小索引为该较小元素的位置，直至遇到尾元素，
        结束一次遍历，并将最小索引处元素与首元素交换；然后，初始化最小索引值为第二个待排序数列元素位置，同样的操作，
        可得到数列第二个元素即为次小元素；以此类推（第一次找出最小／最大的元素。存放在索引的开始位置，再从剩余未排序元素中寻找最小（大）元素，
        放到已排序的序列的末尾，直到全部待排序的元素个数为零， 
        算法复杂度：o(n^2), 交换次数比冒泡排序少多了，由于交换所需事件比比较所需CPU时间多，在n较小时候，选择排序比冒泡排序块
        稳定性：不稳定的排序算法， 在一趟选择中，如果一个元素比当前元素小，而该小元素又出现在一个和当前元素的后面， 那么交换后稳定性就破坏了，
               所以选择排序是一个不稳定的算算法
               比较拗口，举个例子，序列5 8 5 2 9， 我们知道第一遍选择第1个元素5会和2交换，那么原序列中2个5的相对前后顺序就被破坏了，
               所以选择排序不是一个稳定的排序算法。
"""


def subSelectSort(nums):
    for i in range(len(nums)):
        min_index = i
        for j in range(i+1, len(nums)):
            if nums[min_index] > nums[j]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    print(nums)


"""
https://blog.csdn.net/adusts/article/details/80882649
https://www.jianshu.com/p/2b2f1f79984e
快速排序：（类似于选择排序的定位思想）选一个基准元素，依次将剩余元素中小于该基准元素的值放置在其左侧，大于等于该基准元素的值放置在其右侧。，然后，取
        基准元素的前半部分和后半部分分别进行同样的处理；以此类推，直至各个子序列剩余一个元素时，排序完成（类比二叉树的思想，from up to down),
        快排是对冒泡排序的一种改进，基本思想：通过一趟排序把将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的数据要小， 然后按照此方法
        对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列，相对冒泡排序，他的交换是跳跃式的
        是一种分治思想，适合在数据集比较大的时候使用
        具体流程：
            设定一个分界值，通过该分界值将数据分成左右两部分
            将大于或者等于该分界值的数据集中到数组的右边，小于分界值的数据集中到数组的左边
            然后将左边和右边的数据独立排序，对于左侧的数据再选取一个分界值，右边类似...
            重复上述过程（递归定义），当左右两边的部分各数据排序完成后，整个数据的排序也就完成了
        时间复杂度 o(nlogn), 整个排序算法的时间复杂度与划分的趟数有关系，理想的情况下，时间复杂度为o(nlog2n), 最坏的情况为o(n2)
            平均时间复杂度是o(nlog2n), 是目前最好的一种内部排序方法，
            从空间性能上来看，尽管快速排序只需要一个元素的辅助空间，但快排需要一个栈空间来实现递归，空间负载度为o(log2n)
        稳定性：是不稳定的算法
"""


def quickSort(nums):
    """
    缺点：使用两个列表解析式，每次选取进行比较都需要遍历整个序列，递归影响性能
    :param nums:
    :return:
    """
    # 递归需要找到入口以及出口，start和end碰头了，说明只剩下一个一个数了，就不需要排序了
    if len(nums) < 2:
        return nums
    else:
        # 需要重复的过程
        mid = nums[0]
        left = [i for i in nums[1:] if i <= mid]
        right = [i for i in nums[1:] if i > mid]
    return quickSort(left) + [mid] + quickSort(right)


# def quick_sort(num1, num2):
#     list1 = num1.extend(num2)
#
#     def quick(l, left, right):
#         if left >= right:
#             return
#         start = left
#         end = right
#         ref = l[start]
#         while left < right:
#             while left < right and l[right] >= ref:
#                 right -= 1
#             l[right], l[left] = l[left], l[right]
#             while left < right and l[left] < ref:
#                 left += 1
#             l[right], l[left] = l[left], l[right]
#         quick(l, start, left-1)
#         quick(l, left+1, end)
#     quick(list1, 0, len(list1)-1)
#     return l
#
#
# if __name__ == '__main__':
#     l1 = [1, 3, 10, 4, 1]
#     l2 = [3, 7, 19, 10]
#     print(quick_sort(l1, l2))


# 原地排序方法(C风格）o(nlgn)
def quickSort2(nums, left, right):
    if left >= right:
        return
    start = left
    end = right
    ref = nums[left]
    while left < right:
        while left < right and nums[right] >= ref:
            right -= 1
        nums[right], nums[left] = nums[left], nums[right]
        while left < right and nums[left] < ref:
            left += 1
        nums[right], nums[left] = nums[left], nums[right]
    quickSort2(nums, start, left-1)
    quickSort2(nums, left+1, end)


"""
直接插入排序：数列前面部分看为有序， 依次将后面的无序数列元素插入到前面的有序数列中，初始状态有序数列仅为一个元素（首元素），将无序数列元素插入到有序
        数列的过程中，采用了逆序遍历有序数列，相对于顺序遍历会稍显繁琐，但当数列本身已经接近排序状态的时候效率会更高。算法适用于少量数据的排序，eg，量级小于千
        算法思路：
            设置监视哨， 将带插入记录的值付给r[0],
            设置开始查找的位置j
            在数组中开始搜索，搜索中将第j各元素后移直至r[0].key>=r[j].key为止
            将r[0]插入r[j+1]的位置上
        时间复杂度：o(n^2)
        稳定性: 稳定
    
"""


def insertSort(nums):
    sorted_list = [nums[0], ]

    for i in range(1, len(nums)):
        print(sorted_list)
        if nums[i] < sorted_list[0]:
            sorted_list.insert(0, nums[i])
        else:
            for j in range(len(sorted_list)-1):

                if sorted_list[j] < nums[i] <= sorted_list[j+1]:
                    sorted_list.insert(j+1, nums[i])
                    break
            else:
                sorted_list.append(nums[i])
    print(sorted_list)


# 正确的插入排序
def insertSort2(nums):
    # 默认为第一个元素为有序序列
    for i in range(1, len(nums)):
        # 后面改变了数组的内部结构，所以需要在这里拿出来值，否则会出错
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            # 往后挪
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = key

    print(nums)


"""
归并排序：
    一开始先把数组从中间划分为两个子数组，一直递归的把子数组划分为更小的数组，直到子数组里只有一个元素，才开始排序
    排序的方法就是按照大小顺序合并两个元素，接着依次按照递归的返回顺序，不断的合并排好序的子数组，直到最后把整个数组的顺序排好
"""


def merge(a, b):
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result += a[i:]
    result += b[j:]
    return result


def sort(data):
    length = len(data)
    if length <= 1:
        return data

    mid = length // 2
    a = sort(data[:mid])
    b = sort(data[mid:])
    return merge(a, b)

"""
https://blog.51cto.com/me2xp/1973414、
一般升序用大顶堆， 降序用小顶堆
堆排序， 堆排序对简单选择排序进行了改进， 堆是一个完全二叉树
大顶堆：每个非叶子节点都要大于或者等于其左右孩子节点的值称为大顶堆
小顶堆：每个非叶子节点都要小于或者等于其左右孩子节点的值称为小顶堆
堆排序的思路：
    构建完全二叉树， 将原始数据放入完全二叉树中，
    构建大顶堆，需要选择起点结点，选择下一个结点，以及如何调整堆
        核心算法：堆结点的调整
            度数为2的结点A，如果它的左右孩子结点的最大值比它大的，将这个最大值和该结点交换
            度数为1的结点A，如果它的左孩子的值大于它， 则交换
            如果结点A被交换到新的位置，还需要和其孩子结点重复上面的过程
    排序，将堆顶数据依次拿走，生成排序的树， 最后用层序遍历就可以拿到所有的排序元素
    
时间复杂度：O(nlogn)
空间复杂度：O(1), 只使用了一个交换用的空间
是不稳定的排序算法
"""


def heapify(arr, n, i):
    largest = i
    # print(i, arr[i])
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # 交换

        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n, -1, -1):
        print("i", i)
        # print(i, arr,arr[i])
        heapify(arr, n, i)

        # 一个个交换元素
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 交换
        heapify(arr, i, 0)


class Solution:
    def max_heapify(self, heap, root, heap_len):
        p = root
        while p * 2 + 1 < heap_len:
            l, r = p * 2 + 1, p * 2 + 2
            if heap_len <= r or heap[r] < heap[l]:
                nex = l
            else:
                nex = r
            if heap[p] < heap[nex]:
                heap[p], heap[nex] = heap[nex], heap[p]
                p = nex
            else:
                break

    def build_heap(self, heap):
        for i in range(len(heap) - 1, -1, -1):
            self.max_heapify(heap, i, len(heap))

    def heap_sort(self, nums):
        self.build_heap(nums)
        for i in range(len(nums) - 1, -1, -1):
            nums[i], nums[0] = nums[0], nums[i]
            self.max_heapify(nums, 0, i)

    def sortArray(self, nums):
        self.heap_sort(nums)
        return nums

    def link_node(self, headA, headB):
        ha = headA
        hb = headB
        while not ha == hb:
            ha = ha.next if ha else headB

            hb = hb.next if hb else headA
        return ha



# if __name__ == '__main__':
#     arr = [12, 11, 13, 5, 6, 7]
#     heapSort(arr)
#     n = len(arr)
#     print("排序后")
#     for i in range(n):
#         print("%d" % arr[i])


