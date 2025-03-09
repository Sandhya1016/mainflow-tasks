import heapq
def find_k_largest(nums, k):
    return heapq.nlargest(k, nums)
input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
k = 3
print(find_k_largest(input_list, k))
