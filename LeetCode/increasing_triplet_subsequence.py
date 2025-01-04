array =[1,2,3,4,5]
def increasing_triplet_subsequence(array):
    first = second = float('inf')
    for num in array:
        if num <= first:
            first = num
        elif num <= second:
            second = num
        else:
            return True
    return False

print(increasing_triplet_subsequence(array))