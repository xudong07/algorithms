from bit.add_bitwise_operator import add_bitwise_operator
from bit.count_ones import count_ones_iter, count_ones_recur
from bit.find_missing_number import find_missing_number, find_missing_number2
from bit.power_of_two import is_power_of_two
from bit.reverse_bits import reverse_bits
from bit.single_number import single_number
from bit.single_number2 import single_number2
from bit.single_number3 import single_number3
from bit.subsets import subsets
from bit.bit_operation import get_bit, set_bit, clear_bit, update_bit
from bit.swap_pair import swap_pair
from bit.find_difference import find_difference
from bit.has_alternative_bit import has_alternative_bit, has_alternative_bit_fast
from bit.insert_bit import insert_one_bit, insert_mult_bits
from bit.remove_bit import remove_bit

import unittest
import random

class TestSuite(unittest.TestCase):

    def test_add_bitwise_operator(self):
        self.assertEqual(5432 + 97823, add_bitwise_operator(5432, 97823))
        self.assertEqual(0, add_bitwise_operator(0, 0))
        self.assertEqual(10, add_bitwise_operator(10, 0))
        self.assertEqual(10, add_bitwise_operator(0, 10))

    def test_count_ones_recur(self):

        # 8 -> 1000
        self.assertEqual(1, count_ones_recur(8))

        # 109 -> 1101101
        self.assertEqual(5, count_ones_recur(109))

        # 63 -> 111111
        self.assertEqual(6, count_ones_recur(63))

        # 0 -> 0
        self.assertEqual(0, count_ones_recur(0))

    def test_count_ones_iter(self):

        # 8 -> 1000
        self.assertEqual(1, count_ones_iter(8))

        # 109 -> 1101101
        self.assertEqual(5, count_ones_iter(109))

        # 63 -> 111111
        self.assertEqual(6, count_ones_iter(63))

        # 0 -> 0
        self.assertEqual(0, count_ones_iter(0))

    def setUp(self):
        """Initialize seed."""
        random.seed("test")

    def test_find_missing_number(self):

        self.assertEqual(7, find_missing_number([4, 1, 3, 0, 6, 5, 2]))
        self.assertEqual(0, find_missing_number([1]))
        self.assertEqual(1, find_missing_number([0]))

        nums = [i for i in range(100000) if i != 12345]
        random.shuffle(nums)
        self.assertEqual(12345, find_missing_number(nums))

    def test_find_missing_number2(self):

        self.assertEqual(7, find_missing_number2([4, 1, 3, 0, 6, 5, 2]))
        self.assertEqual(0, find_missing_number2([1]))
        self.assertEqual(1, find_missing_number2([0]))

        nums = [i for i in range(100000) if i != 12345]
        random.shuffle(nums)
        self.assertEqual(12345, find_missing_number2(nums))

    def test_is_power_of_two(self):

        self.assertTrue(is_power_of_two(64))
        self.assertFalse(is_power_of_two(91))
        self.assertTrue(is_power_of_two(2**1001))
        self.assertTrue(is_power_of_two(1))
        self.assertFalse(is_power_of_two(0))

    def test_reverse_bits(self):

        self.assertEqual(43261596, reverse_bits(964176192))
        self.assertEqual(964176192, reverse_bits(43261596))
        self.assertEqual(1, reverse_bits(2147483648))

        # bin(0) => 00000000000000000000000000000000
        self.assertEqual(0, reverse_bits(0))

        # bin(2**32 - 1) => 11111111111111111111111111111111
        self.assertEqual(2**32 - 1, reverse_bits(2**32 - 1))

    def test_single_number(self):

        random.seed('test')

        self.assertEqual(0, single_number([1, 0, 2, 1, 2, 3, 3]))
        self.assertEqual(101, single_number([101]))

        single = random.randint(1, 100000)
        nums = [random.randint(1, 100000) for _ in range(1000)]
        nums *= 2  # nums contains pairs of random integers
        nums.append(single)
        random.shuffle(nums)

        self.assertEqual(single, single_number(nums))

    def test_single_number2(self):

        self.assertEqual(3, single_number2([4, 2, 3, 2, 1, 1, 4, 2, 4, 1]))
        single = random.randint(1, 100000)
        nums = [random.randint(1, 100000) for _ in range(1000)]
        nums *= 3  # nums contains triplets of random integers
        nums.append(single)
        random.shuffle(nums)
        self.assertEqual(single, single_number2(nums))

    def test_single_number3(self):
        self.assertEqual(sorted([2,5]),
                         sorted(single_number3([2, 1, 5, 6, 6, 1])))
        self.assertEqual(sorted([4,3]),
                         sorted(single_number3([9, 9, 4, 3])))

    def test_subsets(self):

        self.assertSetEqual(subsets([1, 2, 3]),
                            {(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)})

        self.assertSetEqual(subsets([10, 20, 30, 40]),
                            {(10, 40), (10, 20, 40), (10, 30), (10, 20, 30, 40), (40,),
                             (10, 30, 40), (30,), (20, 30), (30, 40), (10,), (),
                             (10, 20), (20, 40), (20, 30, 40), (10, 20, 30), (20,)})

    def test_get_bit(self):
        # 22 = 10110
        self.assertEqual(1, get_bit(22, 2))
        self.assertEqual(0, get_bit(22, 3))

    def test_set_bit(self):
        # 22 = 10110  --> after set bit at 3th position: 30 = 11110
        self.assertEqual(30, set_bit(22, 3))

    def test_clear_bit(self):
        # 22 = 10110 --> after clear bit at 2nd position: 20 = 10010
        self.assertEqual(18, clear_bit(22, 2))

    def test_update_bit(self):
        # 22 = 10110 --> after update bit at 3th position with value 1: 30 = 11110
        self.assertEqual(30, update_bit(22, 3, 1))
        # 22 = 10110 --> after update bit at 2nd position with value 0: 20 = 10010
        self.assertEqual(18, update_bit(22, 2, 0))

    def test_swap_pair(self):
        # 22: 10110  --> 41: 101001
        self.assertEqual(41, swap_pair(22))
        # 10: 1010   --> 5 : 0101
        self.assertEqual(5, swap_pair(10))

    def test_find_difference(self):
        self.assertEqual('e', find_difference("abcd", "abecd"))

    def test_has_alternative_bit(self):
        self.assertTrue(has_alternative_bit(5))
        self.assertFalse(has_alternative_bit(7))
        self.assertFalse(has_alternative_bit(11))
        self.assertTrue(has_alternative_bit(10))

    def test_has_alternative_bit_fast(self):
        self.assertTrue(has_alternative_bit_fast(5))
        self.assertFalse(has_alternative_bit_fast(7))
        self.assertFalse(has_alternative_bit_fast(11))
        self.assertTrue(has_alternative_bit_fast(10))

    def test_insert_one_bit(self):
        """
        Input: num = 10101 (21)
        insert_one_bit(num, 1, 2): 101101 (45)
        insert_one_bit(num, 0 ,2): 101001 (41)
        insert_one_bit(num, 1, 5): 110101 (53)
        insert_one_bit(num, 1, 0): 101010 (42)
        """
        self.assertEqual(45, insert_one_bit(21, 1, 2))
        self.assertEqual(41, insert_one_bit(21, 0, 2))
        self.assertEqual(53, insert_one_bit(21, 1, 5))
        self.assertEqual(43, insert_one_bit(21, 1, 0))

    def test_insert_mult_bits(self):
        """
        Input: num = 101 (5)
        insert_mult_bits(num, 7, 3, 1): 101111 (47)
        insert_mult_bits(num, 7, 3, 0): 101111 (47)
        insert_mult_bits(num, 7, 3, 3): 111101 (61)
        """
        self.assertEqual(47, insert_mult_bits(5, 7, 3, 1))
        self.assertEqual(47, insert_mult_bits(5, 7, 3, 0))
        self.assertEqual(61, insert_mult_bits(5, 7, 3, 3))

    def test_remove_bit(self):
        """
        Input: num = 10101 (21)
        remove_bit(num, 2): output = 1001 (9)
        remove_bit(num, 4): output = 101 (5)
        remove_bit(num, 0): output = 1010 (10)
        """
        self.assertEqual(9, remove_bit(21, 2))
        self.assertEqual(5, remove_bit(21, 4))
        self.assertEqual(10, remove_bit(21, 0))

if __name__ == '__main__':
    unittest.main()
