import unittest

from algorithms.comparison.Bubble_Sort import bubble_sort


class TestBubbleSort(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(bubble_sort([]), [])

    def test_single_element(self):
        self.assertEqual(bubble_sort([5]), [5])

    def test_already_sorted(self):
        self.assertEqual(
            bubble_sort([1, 2, 3, 4, 5]),
            [1, 2, 3, 4, 5]
        )

    def test_reverse_sorted(self):
        self.assertEqual(
            bubble_sort([5, 4, 3, 2, 1]),
            [1, 2, 3, 4, 5]
        )

    def test_random_order(self):
        self.assertEqual(
            bubble_sort([64, 34, 25, 12, 22, 11, 90]),
            [11, 12, 22, 25, 34, 64, 90]
        )

    def test_duplicates(self):
        self.assertEqual(
            bubble_sort([4, 2, 5, 2, 1, 4]),
            [1, 2, 2, 4, 4, 5]
        )

    def test_negative_numbers(self):
        self.assertEqual(
            bubble_sort([3, -1, 0, -5, 8]),
            [-5, -1, 0, 3, 8]
        )


if __name__ == "__main__":
    unittest.main()