# count sort
# def counting_sort(arr):
#     max_val = max(arr)
#     count = [0] * (max_val + 1)
    
#     for num in arr:
#         count[num] += 1
        
#     sorted_arr = []
#     for i in range(len(count)): 
#         for _ in range(count[i] ):    
#             sorted_arr.append(i)
            
#     return sorted_arr

# arr = [4,6,3,6,2,7,3,7,4,6,1,7]
# print("Before Sort Array:" , arr)
# sorted_arr = counting_sort(arr)
# print("Sorted Array: ", sorted_arr)

#bin sort
# def bin_sort(arr):
#     if not arr: return arr
    
#     max_val = max(arr)
#     bins = [0] * (max_val + 1)
#     for num in arr:
#         bins[num] += 1
        
#     sorted_arr = []
#     for i,count in enumerate(bins):
#         sorted_arr.extend([i] * count)
        
#     return sorted_arr

# arr = [4,6,3,6,2,7,3,7,4,6,1,7]
# print("Before Sort Array:" , arr)
# print("After Sort Array: ", bin_sort(arr))
    
#radix sort