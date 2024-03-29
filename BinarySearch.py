#binary search algorithm
# let us compair binary with naive search
import random
import time

def naive_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1
# binary search is kind of divide and coquuer, we have to make sure the list is sorted
def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1
    if high < low:
        return -1

    # assinging a mid point to start from
    midpoint = (low + high) // 2
    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint - 1)
    else:
        #target>l(midpoint)
        return binary_search(l, target, midpoint + 1, high)

if __name__ == '__main__':
    #li =[1,4,6,9,10,2,5,7,8].sort()
    #target = 10
    #print(naive_search(li, target))
    #print(binary_search(li, target))

    length = 10000
    #build a sorted list of length 10000
    sorted_list = []
    while len(sorted_list) < length:
        sorted_list.append(random.randint(-3 * length, 3 * length))
    sorted_list.sort()
    #lets ittrate though all the values and look for it in through naive and binary
    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    t_1 = (end - start) / len(sorted_list)
    print("Naive search time:", t_1, "seconds per iteration")

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    t_2 = (end - start) / len(sorted_list)
    print("Binary search time:", t_2, "seconds per iteration")

    print("Binary search is", t_1 / t_2, "times more efficient than naive search")
