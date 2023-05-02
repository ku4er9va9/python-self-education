import unittest
import tempfile
import os
from main_2 import check_number_range, calculate_time_remaining,write_task_to_file


class TestCheckNumberRange(unittest.TestCase):

    def test_number_in_range_0_100(self):
        self.assertEqual(check_number_range('50'), 'Число попало в промежуток от 0-100')

    def test_number_in_range_200_300(self):
        self.assertEqual(check_number_range('250'), 'Число попало в промежуток от 200-300')

    def test_number_out_of_range(self):
        self.assertEqual(check_number_range('-10'), 'Не попало ни в один из промежутков')
        self.assertEqual(check_number_range('500'), 'Не попало ни в один из промежутков')

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            check_number_range('abc')


class TestCalculateTimeRemaining(unittest.TestCase):
    def test_time_remaining_for_0_minutes(self):
        result = calculate_time_remaining('0')
        self.assertEqual(result, '200 минут')

    def test_time_remaining_for_50_minutes(self):
        result = calculate_time_remaining('50')
        self.assertEqual(result, '100 минут')

    def test_time_remaining_for_100_minutes(self):
        result = calculate_time_remaining('100')
        self.assertEqual(result, '0 минут')

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            calculate_time_remaining('abc')


if __name__ == '__main__':
    unittest.main()


