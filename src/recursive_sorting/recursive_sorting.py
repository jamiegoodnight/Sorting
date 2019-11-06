# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # elements = len( arrA ) + len( arrB )
    # merged_arr = [0] * elements
    # TO-DO
    l = 0
    r = 0
    lenA = len(arrA)
    lenB = len(arrB)
    # STEP 3: We begin to loop through both arrays and compare them, ordering them as we go. Variables l and r are initialized at 0 meaning [0] postion.
    merged_arr = []
    while l < lenA and r < lenB:
        if arrA[l] < arrB[r]:
            merged_arr.append(arrA[l])
            l += 1
        else:
            merged_arr.append(arrB[r])
            r += 1
    if l == lenA:
        merged_arr.extend(arrB[r:])
    else:
        merged_arr.extend(arrA[l:])
    # STEP 4: We put the arrays together. In an example like merge([1,2],[3,4]) l == lenA and r == 0, therefore merged_arr.extend(arrB[r:] produces [1,2,3,4] because we're adding everything to the right of, and including, position 0)

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    lenA = len(arr)
    if lenA <= 1:
        return arr
    # STEP 1: We find the length of the array because if the length of the array is one then it's already sorted.
    m = round(lenA/2)
    l = merge_sort(arr[:m])
    r = merge_sort(arr[m:])
    # STEP 2: We split our array down the middle and we pass these two new arrays to merge().
    return merge(l, r)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
