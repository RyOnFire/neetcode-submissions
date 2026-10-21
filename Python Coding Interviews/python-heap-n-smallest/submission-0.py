import heapq
from typing import List


def get_min_element(arr: List[int]) -> int:
    heap = []
    for num in arr:
        heapq.heappush(heap, num)
    mi = heapq.nsmallest(1, heap)
    mio = int(mi[0])
    return mio


def get_min_4_elements(arr: List[int]) -> List[int]:
    # Return elements in *increasing* order
    heap = []
    for num in arr:
        heapq.heappush(heap, num)
    mi4 = heapq.nsmallest(4, heap)
    return mi4


def get_min_2_elements(arr: List[int]) -> List[int]:
    # Return elements in *decreasing* order
    mi2 = heapq.nsmallest(2, arr)
    return mi2[::-1]
    


# do not modify below this line
print(get_min_element([1, 2, 3]))
print(get_min_element([3, 2, 1, 4, 6, 2]))
print(get_min_element([1, 9, 7, 3, 2, 1, 4, 6, 2]))

print(get_min_4_elements([1, 9, 7, 3, 2, 1, 4, 6, 2]))
print(get_min_4_elements([1, 9, 7, 2, 1, 3, 2, 1, 4, 6, 2, 1]))
print(get_min_4_elements([1, 9, 7, 2, 3, 2, 4, 6, 2]))

print(get_min_2_elements([1, 9, 7, 3, 2, 1, 4, 6, 2]))
print(get_min_2_elements([1, 9, 7, 2, 1, 3, 2, 1, 4, 6, 2, 1]))
print(get_min_2_elements([1, 9, 7, 2, 3, 2, 4, 6, 2]))

