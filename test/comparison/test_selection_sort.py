import unittest

from algorithms.comparison.Selection_Sort import selection_sort


class TestSelectionSort(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(selection_sort([]), [])

    def test_single_element(self):
        self.assertEqual(selection_sort([1]), [1])

    def test_already_sorted(self):
        self.assertEqual(selection_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted(self):
        self.assertEqual(selection_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_random_order(self):
        self.assertEqual(selection_sort([64, 25, 12, 22, 11]), [11, 12, 22, 25, 64])

    def test_duplicates(self):
        self.assertEqual(selection_sort([3, 1, 2, 3, 1]), [1, 1, 2, 3, 3])

    def test_negative_numbers(self):
        self.assertEqual(selection_sort([-3, -1, -7, 2, 0]), [-7, -3, -1, 0, 2])

    def test_mixed_numbers(self):
        self.assertEqual(selection_sort([0, -1, 5, -3, 2]), [-3, -1, 0, 2, 5])


if __name__ == "__main__":
    unittest.main()