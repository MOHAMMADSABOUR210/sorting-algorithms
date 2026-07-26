import unittest

from algorithms.comparison.Insertion_Sort import insertion_sort


class TestInsertionSort(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(insertion_sort([]), [])

    def test_single_element(self):
        self.assertEqual(insertion_sort([5]), [5])

    def test_already_sorted(self):
        self.assertEqual(
            insertion_sort([1, 2, 3, 4, 5]),
            [1, 2, 3, 4, 5]
        )

    def test_reverse_sorted(self):
        self.assertEqual(
            insertion_sort([5, 4, 3, 2, 1]),
            [1, 2, 3, 4, 5]
        )

    def test_random_order(self):
        self.assertEqual(
            insertion_sort([64, 34, 25, 12, 22, 11, 90]),
            [11, 12, 22, 25, 34, 64, 90]
        )

    def test_duplicates(self):
        self.assertEqual(
            insertion_sort([4, 2, 5, 2, 3, 4, 1]),
            [1, 2, 2, 3, 4, 4, 5]
        )

    def test_negative_numbers(self):
        self.assertEqual(
            insertion_sort([-3, -1, -7, 4, 2, 0]),
            [-7, -3, -1, 0, 2, 4]
        )

    def test_mixed_numbers(self):
        self.assertEqual(
            insertion_sort([3, -1, 0, -5, 8, 2]),
            [-5, -1, 0, 2, 3, 8]
        )

    def test_original_list_not_modified(self):
        arr = [3, 2, 1]
        insertion_sort(arr)
        self.assertEqual(arr, [3, 2, 1])


if __name__ == "__main__":
    unittest.main()