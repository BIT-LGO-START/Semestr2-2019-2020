"""
There was a list of length m * n, which had unique values and was sorted.
It was cut into n parts of same length, and then those parts were randomly
shuffled. Elements inside each part were then also shuffled.
Implement function fix_unsorted(arr, n) which will sort such array.
"""


def generate_data(m, n):
    # generate list of consecutive diminishing integers, since it suffices
    # to fulfill the task constraints
    return list(range(m*n, 0, -1))


def fix_unsorted(arr, n):
    """
    We use two pieces of information from the task:
    1) The parts were originally internally sorted
    2) All values are distinct
    Using the first piece of info, we sort each part (we can easily compute
    the m value, since len(arr) = m * n). We then have a list of "blocks",
    which we have to put in the right order. Since all values are distinct,
    we can base our sorting only on the first element of each part - for any
    part the first element will be larger than the last element of the
    previous part (previous i. e. after sorting). Therefore we can sort a
    list of tuples (first_value, index) based on first_value to get the right
    ordering and then use the indices to sort the parts. Note that for
    efficiency the implementation checks not to "swap" part with itself.
    Time complexity:
    First part - using the O(nlog(n)) sorting, the sorting of each of n parts
    internally is O(mlog(m)), givng O(mnlog(m)) in total.
    Second part - sorting the tuples array is O(nlog(n)) (there are as many
    tuples are there are parts, so n), swapping is O(n*m) (pessimistically,
    when we need to swap each of n parts, every one has length m), giving
    O(nlog(n) + m*n) in total.
    Overall time complexity - O(mnlog(m) + nlog(n) + mn) = O(mnlog(m))
    Space complexity:
    We need temporary array for swapping, which in Python happens "behind the
    mask", but is still there. O(m)
    :param arr: array given as in the task description
    :param n: number of parts in the array
    :return: sorted array
    """
    m = len(arr) // n

    # sort individual parts
    for i in range(0, len(arr), m):
        arr[i:i + m] = sorted(arr[i:i + m])

    # put parts in right places
    first_elems = [(arr[i], i) for i in range(0, len(arr), m)]
    first_elems.sort()
    curr_i = 0
    for val, i in first_elems:
        # check, guards from "swapping" part with itself
        if arr[curr_i] != val:
            arr[curr_i:curr_i + m], arr[i:i + m] = \
                arr[i:i + m], arr[curr_i:curr_i + m]
        curr_i += m

    return arr


if __name__ == "__main__":
    m = 4
    n = 5
    unsorted_list = generate_data(m, n)
    print("List after \"unsorting\":")
    print(unsorted_list)
    print("\nSorted list:")
    sorted_list = fix_unsorted(unsorted_list, n)
    print(sorted_list)
