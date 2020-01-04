class Solution:
    def removeElement(self, nums, val):
        if len(nums) == 0:
            return 0
        result = len(nums)
        for i in range(result):
            if val in nums:
                nums.remove(val)
        result = len(nums)
        print("Nums : {}".format(nums))
        print("Result : {}".format(result))
        return result


a = Solution()
num_list = [0, 1, 2, 2, 3, 0, 4, 2]
print(num_list)
a.removeElement(num_list, 2)
