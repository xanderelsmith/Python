# DSA: TWO SUM
class TwoSum:
    def calculate_two_sum_brute_force(self, nums: list[int], total):
        # Brute force approach: O(n^2) time complexity
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == total:
                    return [i, j]
        return None   
    
    
    def calculate_two_sum(self, nums: list[int], total):
        # Hash map approach: O(n) time complexity
        map = {}
        for index in range(len(nums)):
            remainder = total - nums[index]
            if remainder in map:
                return [map[remainder], index]
            map[nums[index]] = index



# Difference:
# - Hash map approach is much faster (O(n)), only one pass through the list.
# - Brute force checks every pair (O(n^2)), much slower for large lists.

two_sum_object = TwoSum()
entities = two_sum_object.calculate_two_sum(nums=[1, 2, 4], total=6)
print("Hash map result:", entities)

entities_brute = two_sum_object.calculate_two_sum_brute_force(nums=[1, 2, 4], total=6)
print("Brute force result:", entities_brute)

