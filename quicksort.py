# [amotz]

# this is my attempt to make a quick sort algorithm, it seems to work now.

# it will have three functions,

# the first one swap, will take a list
# and two indecies as arguments and swap the values in those indecies.

# the second function will be called partition.
# this function is taking 3 arguments, one of them is a list another is the start index of the list and the last one is the end index of the list.
# the partition function will then choose the end element in a list and sort it in such a way that all the smaller elements will be in the left side of the value
# and all the greater elements will be in the right side of the value.
# it will do this by making the index of the end element as a pivot and the index of the first element as pindex,
# it will then loop the list and each element that is smaller than the pivot will be swapped with the element in pindex using the swap function,
# while each swap we also increment pindex by 1.
# in the end of this process  we will swap the pivot value with pindex value to sort the end index value and return pindex for our quicksort function use.

# the third function will be called quicksort, this function will get a list as an argument, a start index and an end index.
# it will use partition to sort the end index value of a list first and assign pindex to a variable.
# then it will call itself two times recurssively the first call will take the same list a start index and a pindex-1 index as arguments
# and the second call will take the same list pindex+1  and the end index,
# this procedure will create new pivot each reccursive call and will sort it until the whole list is sorted and then it will return the list


def swap(list, index1, index2):
    temp = list[index2]
    list[index2] = list[index1]
    list[index1] = temp
    return list


def testswap():
    testCases = [([1, 0], 0, 1), ([2, 3, 5], 0, 2), ([4, 8, 7, 9], 0, 3)]

    for testcase in testCases:
        print("in ", testcase[0], testcase[1], testcase[2])
        print("out ", swap(testcase[0], testcase[1], testcase[2]))


testswap()


def partition(list, start, end):
    pivot = end
    pindex = start
    for i in range(pindex, pivot):
        if list[i] < list[pivot]:
            swap(list, i, pindex)
            pindex = pindex + 1
    swap(list, pindex, pivot)
    return pindex


testcases = [([1, 1], 0, 1), ([1, 2, 3], 0, 2), ([3, 2, 1], 0, 2), ([4, 7, 8, 4], 0, 3), ([2, 15, 11, 9], 0, 3)]


def testpartition():
    for testcase in testcases:
        print(partition(testcase[0], testcase[1], testcase[2]))


testpartition()


# partition([2,6,8,3,9,7,5])

def quicksort(list, start, end):
    if start >= end:
        return list
    pindex = partition(list, start, end)
    quicksort(list, start, pindex - 1)
    quicksort(list, pindex + 1, end)
    return list


testcases = [([], 0, 0), ([1], 0, 0), ([1, 1], 0, 1), ([1, 2, 3], 0, 2), ([3, 2, 1], 0, 2), ([4, 7, 8, 4], 0, 3),
             ([7, 4, 6, 9, 6, 9, 7, 8], 0, 7), ([86, 56, 23, 46, 11, 3, 5, 8, 3321, 99, 567], 0, 10)]


def testquicksort():
    for testcase in testcases:
        print("in ", testcase[0])
        print("out ", quicksort(testcase[0], testcase[1], testcase[2]))


testquicksort()
