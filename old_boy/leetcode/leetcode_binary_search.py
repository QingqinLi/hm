
class Solution:
    """
    给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
    """
    def searchInsert(self, nums, target) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2  # 只拿整数部分
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return low
    """
    Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.
    Return the quotient after dividing dividend by divisor.
    The integer division should truncate toward zero.
    一般解法：转换为减法，知道被减数小于0为止， 但这种解法，时间复杂度高o(n)，无法AC
    二分法变种：
        二进制是可以用来表示所有数字的
        
        
    
    """

    def divide(self, dividend: int, divisor: int) -> int:
        count = 0
        # surplus = abs(dividend)
        if dividend == 0:
            return 0
        if dividend == divisor:
            return 1
        if divisor + dividend == 0:
            return -1
        if (divisor < 0 < dividend) or (divisor > 0 > dividend):
            flag = True
        else:
            flag = False
        # while surplus > 0:
        #     surplus -= abs(divisor)
        #     count += 1

        all = 0
        b = abs(dividend)
        while all != abs(dividend):

            sum = abs(divisor)
            ret = 0
            count = 0
            while sum+sum < b:
                sum += sum
                print(sum)
                count += 1
            ret += pow(2, count)
            all += sum
            b -= sum
            print(ret)

        if flag:
            return -(count - 1)
        else:
            return count - 1



s = Solution()
print(s.divide(0, 1))

