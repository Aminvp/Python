import unittest
from function import comb


class ScoreListTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_1(self):
        self.assertEqual(3, comb(3, 2), '\nخروجی تابع برای comb(3, 2) باید برابر ۳ باشد.')

    def test_2(self):
        self.assertEqual(1, comb(3, 0), '\nخروجی تابع برای comb(3, 0) باید برابر ۱ باشد.')

    def test_3(self):
        self.assertEqual(0, comb(3, 4)), '\nخروجی تابع برای comb(3, 4) باید برابر ۰ باشد.'
