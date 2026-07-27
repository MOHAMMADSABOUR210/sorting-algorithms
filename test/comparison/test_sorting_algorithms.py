import unittest

from algorithms.comparison.Bubble_Sort import bubble_sort
from algorithms.comparison.Selection_Sort import selection_sort
from algorithms.comparison.Insertion_Sort import insertion_sort
from algorithms.comparison.Shell_Sort import shell_sort
from algorithms.comparison.Marg_sort import merge_sort


SORTING_FUNCTIONS = [
    bubble_sort,
    selection_sort,
    insertion_sort,
    shell_sort,
    merge_sort,
]


class TestSortingAlgorithms(unittest.TestCase):

    def test_empty_list(self):
        for sort in SORTING_FUNCTIONS:
            with self.subTest(sort=sort.__name__):
                self.assertEqual(sort([]), [])

    def test_single_element(self):
        for sort in SORTING_FUNCTIONS:
            with self.subTest(sort=sort.__name__):
                self.assertEqual(sort([5]), [5])

    def test_sorted_integers(self):
        expected = [1, 2, 3, 4, 5]
        for sort in SORTING_FUNCTIONS:
            with self.subTest(sort=sort.__name__):
                self.assertEqual(sort([1, 2, 3, 4, 5]), expected)

    def test_reverse_sorted(self):
        expected = [1, 2, 3, 4, 5]
        for sort in SORTING_FUNCTIONS:
            with self.subTest(sort=sort.__name__):
                self.assertEqual(sort([5, 4, 3, 2, 1]), expected)

    def test_random_integers(self):
        expected = [11, 12, 22, 25, 34, 64, 90]
        data = [64, 34, 25, 12, 22, 11, 90]
        for sort in SORTING_FUNCTIONS:
            with self.subTest(sort=sort.__name__):
                self.assertEqual(sort(data.copy()), expected)

    def test_duplicates(self):
        expected = [1, 2, 2, 4, 4, 5]
        data = [4, 2, 5, 2, 1, 4]
        for sort in SORTING_FUNCTIONS:
            with self.subTest(sort=sort.__name__):
                self.assertEqual(sort(data.copy()), expected)

    def test_negative_numbers(self):
        expected = [-5, -1, 0, 3, 8]
        data = [3, -1, 0, -5, 8]
        for sort in SORTING_FUNCTIONS:
            with self.subTest(sort=sort.__name__):
                self.assertEqual(sort(data.copy()), expected)

    def test_floats(self):
        expected = [-1.5, 0.0, 2.71, 3.14, 8.9]
        data = [3.14, 2.71, -1.5, 0.0, 8.9]
        for sort in SORTING_FUNCTIONS:
            with self.subTest(sort=sort.__name__):
                self.assertEqual(sort(data.copy()), expected)

    def test_mixed_numbers(self):
        expected = [1, 2, 3.2, 4.7, 5]
        data = [5, 3.2, 1, 4.7, 2]
        for sort in SORTING_FUNCTIONS:
            with self.subTest(sort=sort.__name__):
                self.assertEqual(sort(data.copy()), expected)

    def test_strings(self):
        expected = ["apple", "banana", "grape", "orange"]
        data = ["banana", "apple", "orange", "grape"]
        for sort in SORTING_FUNCTIONS:
            with self.subTest(sort=sort.__name__):
                self.assertEqual(sort(data.copy()), expected)


if __name__ == "__main__":
    unittest.main()