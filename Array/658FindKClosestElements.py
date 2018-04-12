//二分查找 和 二指针划窗
class Solution:
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        start, end = 0, len(arr)-1
        while(start <= end):
            mid = (start+end)//2
            if(arr[mid] == x):
                break
            if(arr[mid] > x):
                end = mid - 1
            if(arr[mid] < x):
                start = mid + 1
        cen = mid
        count = k - 1
        left = mid - k + 1
        right = mid + 1
        if left < 0:
            right = -left + right
            left = 0
        print(left, right)
        while(right < len(arr) and x - arr[left] > abs(arr[right] - x)):
            left += 1
            right += 1
        return arr[left:right]
