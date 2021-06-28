import unittest

import lfsr

class testLfsr(unittest.TestCase):
    def test_lfsr(self):
        self.assertEqual(lfsr.lfsr([1, 1, 0, 1, 0, 0, 0, 1],[1, 3]), [0, 1, 1, 0, 1, 0, 0, 0])

    def test_lfsr2(self):
        self.assertNotEqual(lfsr.lfsr([1,1,1,1,1,],[1,4]),[1,1,1,1,1,1,])
