from random import randint
from typing import TypeVar

T = TypeVar("T")


def randomized_quick_sort(
    arr: list[T], low: int = 0, high: int | None = None
) -> list[T]:
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot_index = randomized_partition(arr, low, high)
        randomized_quick_sort(arr, low, pivot_index - 1)
        randomized_quick_sort(arr, pivot_index + 1, high)

    return arr


def randomized_partition(arr: list[T], low: int, high: int) -> int:
    random_index = randint(low, high)
    arr[random_index], arr[high] = arr[high], arr[random_index]

    return partition(arr, low, high)


def partition(arr: list[T], low: int, high: int) -> int:
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1