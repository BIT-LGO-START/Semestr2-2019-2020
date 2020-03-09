"""
There are 2n soldiers. Half of them are privates and half of them are marines.
They were instructed to get in line, but sergeant forgot to tell them to be
divided into two groups - privates first and marines later. As a result, they
are mixed, with 1 meter between each soldier. Soldiers are represented as a
"list" with Soldier class given below.
Implement distance_to_ideal(first_soldier) function, which calculates the
minimal number of meters that soldiers must cumulatively walk for privates
to be in line before marines (and the line must still be in the same place).
"""


class Soldier:
    def __init__(self, is_marine, next_soldier):
        """
        :param is_marine: boolean, False - private, True - marine
        :param next_soldier: next soldier in line, None for the last one
        """
        self.is_marine = is_marine
        self.next = next_soldier

    # method added for debugging
    def __str__(self):
        if self.is_marine:
            return "M"
        else:
            return "P"


def generate_soldiers(n):
    from random import choice
    """
    Utility function for generating example data
    :param n: number of type of soldiers, there will be 2n in total
    (n privates and n marines)
    :return: first Soldier in the "list" (with reference to next one)
    """
    if n <= 0:
        raise ValueError("Number of soldiers must be positive")

    # arbitrarily create private (there will have to be at least 1 anyway)
    first_soldier = Soldier(False, None)
    last_soldier = first_soldier
    privates_no = 1
    marines_no = 0
    while privates_no < n or marines_no < n:
        # more privates needed
        if privates_no < n:
            # more soldiers of both types needed
            if marines_no < n:
                is_marine = choice([False, True])
                if is_marine:
                    marines_no += 1
                else:
                    privates_no += 1
                new_soldier = Soldier(is_marine, None)
                last_soldier.next = new_soldier
                last_soldier = new_soldier

            # only more privates needed
            else:
                privates_no += 1
                new_soldier = Soldier(False, None)
                last_soldier.next = new_soldier
                last_soldier = new_soldier

        # only more marines needed
        else:
            marines_no += 1
            new_soldier = Soldier(True, None)
            last_soldier.next = new_soldier
            last_soldier = new_soldier

    return first_soldier


def print_soldiers(first_soldier):
    """
    Print "list" of soldiers (mostly for debugging purposes).
    :param first_soldier: Soldier, first in line
    :return: None
    """
    # copy reference, don't lose beginning of the "list"
    soldier = first_soldier
    while soldier:
        print(soldier, end=" ")
        soldier = soldier.next
    print()


def distance_to_ideal(first_soldier):
    """
    Algorithm idea: don't move any soldiers at all, only calculate "move" of
    privates. Privates have to move to the left through marines, so we
    count already "sorted" marines - the needed movement in meters will be
    that number times 2 (since "swap" of two soldiers requires a single step
    from both of them). Marines therefore only "add" move swaps needed for
    privates, while privates actually add meters to the required number.
    Time complexity: O(n), n - total number of soldiers
    Space complexity: O(1)
    :param first_soldier: Soldier, first in line
    :return: integer, minimal distance in meters for soldiers to walk to
    achieve right order
    """
    meters = 0
    marines_counter = 0
    soldier = first_soldier
    while soldier:
        if soldier.is_marine:
            marines_counter += 1
        else:
            meters += 2 * marines_counter
        soldier = soldier.next

    return meters


if __name__ == "__main__":
    first_soldier = generate_soldiers(3)
    print("Soldiers:")
    print_soldiers(first_soldier)
    meters = distance_to_ideal(first_soldier)
    print("\nRequired number of meters:", meters)
