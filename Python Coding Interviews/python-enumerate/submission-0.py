from typing import List


def get_index_of_seven(nums: List[int]) -> int:
    for i, sev in enumerate(nums):
        if sev == 7:
            return i
    return -1


def get_dist_between_sevens(nums: List[int]) -> int:
    first_sev_ind = 0
    second_sev_ind = 0
    num_of_sev = 0
    for i, sev in enumerate(nums):
        if num_of_sev == 0:
            if sev == 7:
                first_sev_ind = i
                num_of_sev += 1
        elif num_of_sev == 1:
            if sev == 7:
                second_sev_ind = i
                num_of_sev += 1
        elif num_of_sev == 2:
            pass
    dist = second_sev_ind - first_sev_ind
    return dist


# do not modify below this line
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 8, 9]))
print(get_index_of_seven([2, 4, 7, 5, 7, 8, 4, 2]))

print(get_dist_between_sevens([1, 2, 7, 4, 5, 6, 7, 8, 9]))
print(get_dist_between_sevens([2, 7, 7, 7, 8]))
print(get_dist_between_sevens([7, 4, 8, 4, 2, 7]))
