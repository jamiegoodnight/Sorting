# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # elements = len( arrA ) + len( arrB )
    # merged_arr = [0] * elements
    # TO-DO
    l = 0
    r = 0
    lenA = len(arrA)
    lenB = len(arrB)
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

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    lenA = len(arr)
    if lenA <= 1:
        return arr
    m = round(lenA/2)
    l = merge_sort(arr[:m])
    r = merge_sort(arr[m:])
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
