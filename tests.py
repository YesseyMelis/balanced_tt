import datetime
import unittest

from mean import get_mean


class TestMean(unittest.TestCase):
    def test_mean(self):
        date = datetime.datetime(2022, 8, 1)
        date2 = datetime.datetime(2022, 10, 11)
        result = get_mean(date, date2)
        self.assertEqual(
            result,
            {
                "(Timestamp('2022-08-31 00:00:00'), 'TENGE')": 820.0,
                "(Timestamp('2022-09-30 00:00:00'), 'DOLLAR')": 600.0,
                "(Timestamp('2022-09-30 00:00:00'), 'TENGE')": 400.0,
                "(Timestamp('2022-10-31 00:00:00'), 'TENGE')": 400.0
            }
        )


if __name__ == '__main__':
    unittest.main()
