import unittest

from algorithms.comparison.Shell_Sort import shell_sort


class TestShellSort(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(shell_sort([]), [])

    def test_single_element(self):
        self.assertEqual(shell_sort([1]), [1])

    def test_sorted_integers(self):
        self.assertEqual(
            shell_sort([1, 2, 3, 4, 5]),
            [1, 2, 3, 4, 5]
        )

    def test_reverse_sorted_integers(self):
        self.assertEqual(
            shell_sort([5, 4, 3, 2, 1]),
            [1, 2, 3, 4, 5]
        )

    def test_random_integers(self):
        self.assertEqual(
            shell_sort([64, 34, 25, 12, 22, 11, 90]),
            [11, 12, 22, 25, 34, 64, 90]
        )

    def test_duplicates(self):
        self.assertEqual(
            shell_sort([5, 3, 8, 3, 9, 1, 5]),
            [1, 3, 3, 5, 5, 8, 9]
        )

    def test_negative_numbers(self):
        self.assertEqual(
            shell_sort([0, -1, 5, -10, 8]),
            [-10, -1, 0, 5, 8]
        )

    def test_floats(self):
        self.assertEqual(
            shell_sort([3.14, 2.71, -1.5, 0.0, 8.9]),
            [-1.5, 0.0, 2.71, 3.14, 8.9]
        )

    def test_mixed_ints_and_floats(self):
        self.assertEqual(
            shell_sort([5, 3.2, 1, 4.7, 2]),
            [1, 2, 3.2, 4.7, 5]
        )

    def test_strings(self):
        self.assertEqual(
            shell_sort(["banana", "apple", "orange", "grape"]),
            ["apple", "banana", "grape", "orange"]
        )


if __name__ == "__main__":
    unittest.main()