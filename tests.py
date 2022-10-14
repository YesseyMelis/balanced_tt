import datetime
import unittest

from mean import get_mean


class TestMean(unittest.TestCase):
    def test_mean(self):
        date = datetime.datetime(2022, 1, 1)
        date2 = datetime.datetime(2022, 12, 11)
        result = get_mean(date, date2)
        self.assertEqual(
            result,
            {'2022': {'JAN': {'DOLLAR': 548.3945966883, 'TENGE': 549.631411037},
                      'FEB': {'DOLLAR': 550.8984656575, 'TENGE': 549.612733464},
                      'MAR': {'DOLLAR': 549.1996508528, 'TENGE': 550.4982320571},
                      'APR': {'DOLLAR': 548.4524439527, 'TENGE': 548.7656207769},
                      'MAY': {'DOLLAR': 546.1830308744, 'TENGE': 548.7705457709},
                      'JUN': {'DOLLAR': 550.5832705534, 'TENGE': 549.7754954084},
                      'JUL': {'DOLLAR': 549.5830768146, 'TENGE': 549.7034343149},
                      'AUG': {'DOLLAR': 548.736746747, 'TENGE': 549.6238293688},
                      'SEP': {'DOLLAR': 550.5646210783, 'TENGE': 548.5608775668},
                      'OCT': {'DOLLAR': 546.9960484535, 'TENGE': 549.6623936659},
                      'NOV': {'DOLLAR': 551.1023803681, 'TENGE': 548.9580411154},
                      'DEC': {'DOLLAR': 548.7871258355, 'TENGE': 548.1467248908}}}
        )

    def test_mean_wrong_date(self):
        date = datetime.datetime(2022, 12, 1)
        date2 = datetime.datetime(2022, 1, 11)
        result = get_mean(date, date2)
        self.assertEqual(
            result,
            {}
        )


if __name__ == '__main__':
    unittest.main()
