import math

def num_buses(n):
    """ (int) -> int

    Precondition: n >= 0

    Return the minimum number of buses required to transport n people.
    Each bus can hold 50 people.

    num_buses(75)
    2
    """
    return math.ceil(n/50)

def stock_price_summary(price_changes):
    """ (list of number) -> (number, number) tuple

    price_changes contains a list of stock price changes. Return a 2-item
    tuple where the first item is the sum of the gains in price_changes and
    the second is the sum of the losses in price_changes.

    stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
    (0.14, -0.17)
    """

    gains = 0
    losses = 0
    for item in price_changes:
        if item > 0:
            gains += item
        else:
            losses += item
    return gains, losses


def swap_k(L, k):
    """ (list, int) -> NoneType

    Precondtion: 0 <= k <= len(L) // 2

    Swap the first k items of L with the last k items of L.

    nums = [1, 2, 3, 4, 5, 6]
    swap_k(nums, 2)
    nums
    [5, 6, 3, 4, 1, 2]
    """

    length = len(L)

    for item in range(k):
        temp = L[length-item-1]
        L[length-item-1] = L[item]
        L[item] = temp

    return L


if __name__ == '__main__':
    nums = [12, 23, 15, 34, 67, 6, 7, 8, 45, 31]
    print(swap_k(nums, 2))