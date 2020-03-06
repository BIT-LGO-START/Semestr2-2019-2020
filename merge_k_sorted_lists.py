"""
There are given k sorted lists, which cumulatively have length n.
Design an algorithm that will merge them with time complexity O(nlog(k)).
"""
from collections import deque
import heapq
from random import randint

max_value = 100


def generate_data(n, k):
    lists = [[] for i in range(k)]
    while n >= 0:
        list_index = randint(0, k - 1)
        lists[list_index].append(randint(0, max_value))
        n -= 1

    # we use deque to have true lists and be able to pop from the beginning
    # in O(1) time
    lists = [deque(sorted(lists[i])) for i in range(k)]
    return lists


def print_lists(lists):
    for x in lists:
        print(list(x))


def merge_lists(lists, n):
    """
    We "look" at the first element of each list, creating a min heap with
    tuples (value, list_index) inside. This way we can pick the list with the
    smallest element in O(log(k)) time. Later we take that element, add to
    result and add new element from that list to the heap, "updating" our
    list "view" (heap).
    :param lists: list of deques, sum of their lengths is n
    :return: merged list
    """
    k = len(lists)
    # if exists, since list can be empty and popleft() would raise exception
    first_elems = []
    for k in range(0, len(lists)):
        # check if list is not empty
        if lists[k]:
            first_elem = lists[k][0]
            first_elems.append((first_elem, k))

    # turn first_elems into a min heap
    heapq.heapify(first_elems)

    result = []
    while len(result) < n:
        # take smallest element
        elem, index = heapq.heappop(first_elems)

        # pop element from the list that we got it from
        lists[index].popleft()

        # push new first element from that list to heap
        if lists[index]:
            new_elem = lists[index][0]
            heapq.heappush(first_elems, (new_elem, index))

        # add popped, smallest element to result
        result.append(elem)

    return result


if __name__ == "__main__":
    n = 20
    k = 4
    lists = generate_data(n, k)
    print("Lists before merging:")
    print_lists(lists)
    print()
    lists.append(deque())
    merged_list = merge_lists(lists, n)
    print("Merged lists:")
    print(merged_list)
