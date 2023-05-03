import unittest
from main_2 import check_number_range, calculate_time_remaining, check_fits_in_door, generate_squares_below_N, can_buy_exactly_k_scoops, calculate_deposit, show_sum_of_digits


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


class TestCheckFitsInDoor(unittest.TestCase):

    def test_valid_input_true(self):
        A, B, C, M, K = 1, 2, 3, 3, 4
        self.assertEqual(check_fits_in_door(A, B, C, M, K), "Коробка войдет в дверь")

    def test_valid_input_false(self):
        A, B, C, M, K = 4, 5, 6, 3, 4
        self.assertEqual(check_fits_in_door(A, B, C, M, K), "Коробка не войдет в дверь")


class TestGenerateSquaresBelowN(unittest.TestCase):

    def test_positive(self):
        self.assertEqual(generate_squares_below_N(25), "1\n4\n9\n16")
        self.assertEqual(generate_squares_below_N(10), "1\n4\n9")
        self.assertEqual(generate_squares_below_N(5), "1\n4")
        self.assertEqual(generate_squares_below_N(1), "")

    def test_negative(self):
        self.assertNotEqual(generate_squares_below_N(10), "1\n4\n9\n16")
        self.assertNotEqual(generate_squares_below_N(25), "1\n4\n9")
        self.assertNotEqual(generate_squares_below_N(5), "4")
        self.assertNotEqual(generate_squares_below_N(1), "1")


class TestCanBuyExactlyKScoops(unittest.TestCase):

    def test_positive(self):
        self.assertTrue(can_buy_exactly_k_scoops(3))
        self.assertTrue(can_buy_exactly_k_scoops(5))
        self.assertTrue(can_buy_exactly_k_scoops(8))


    def test_negative(self):
        self.assertFalse(can_buy_exactly_k_scoops(1))
        self.assertFalse(can_buy_exactly_k_scoops(2))
        self.assertFalse(can_buy_exactly_k_scoops(4))
        self.assertFalse(can_buy_exactly_k_scoops(7))
        self.assertFalse(can_buy_exactly_k_scoops(11))
        self.assertFalse(can_buy_exactly_k_scoops(13))
        self.assertFalse(can_buy_exactly_k_scoops(14))
        self.assertFalse(can_buy_exactly_k_scoops(16))
        self.assertFalse(can_buy_exactly_k_scoops(17))
        self.assertFalse(can_buy_exactly_k_scoops(19))


class TestCalculateDeposit(unittest.TestCase):

    def test_positive(self):
        self.assertEqual(calculate_deposit(1000, 10, 2000), "Сумма вклада превысит 2000 тыс. грн через 8 лет")
        self.assertEqual(calculate_deposit(5000, 5, 10000), "Сумма вклада превысит 10000 тыс. грн через 15 лет")

    def test_negative(self):
        self.assertNotEqual(calculate_deposit(1000, 10, 2000), "Сумма вклада превысит 2000 тыс. грн через 5 лет")
        self.assertNotEqual(calculate_deposit(5000, 5, 10000), "Сумма вклада превысит 10000 тыс. грн через 10 лет")
        self.assertNotEqual(calculate_deposit(10000, 7, 15000), "Сумма вклада превысит 15000 тыс. грн через 14 лет")

    def test_input_validation(self):
        self.assertRaises(TypeError, calculate_deposit, "abc", 10, 2000)
        self.assertRaises(TypeError, calculate_deposit, 1000, "abc", 2000)
        self.assertRaises(TypeError, calculate_deposit, 1000, 10, "abc")



class TestShowSumOfDigits(unittest.TestCase):

    def test_negative(self):
        self.assertNotEqual(show_sum_of_digits(123), "Сумма цифр числа 123: 7")
        self.assertNotEqual(show_sum_of_digits(98765), "Сумма цифр числа 98765: 45")
        self.assertNotEqual(show_sum_of_digits(11111), "Сумма цифр числа 11111: 6")



if __name__ == '__main__':
    unittest.main()


