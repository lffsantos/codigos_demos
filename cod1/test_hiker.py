import hiker
import unittest

class TestHiker(unittest.TestCase):

    def test_min_value_seq(self):
        hiker_ = hiker.Hiker([6, 9, 15, -2, 92, 11])
        self.assertEqual(-2,hiker_.min_value_seq())
    
    def test_max_value_seq(self):
        hiker_ = hiker.Hiker([6, 9, 15, -2, 92, 11])
        self.assertEqual(92,hiker_.max_value_seq())    

    def test_number_of_elements(self):
        hiker_ = hiker.Hiker([6, 9, 15, -2, 92, 11])
        self.assertEqual(6,hiker_.number_elements())    
    
    def test_avg_seq(self):
        hiker_ = hiker.Hiker([6, 9, 15, -2, 92, 11])
        self.assertEqual(21.833333,hiker_.avg_seq())    

    def test_empty_seq(self):
        hiker_ = hiker.Hiker([])
        self.assertEqual(0,hiker_.number_elements())
        self.assertEqual(0,hiker_.max_value_seq())
        self.assertEqual(0,hiker_.min_value_seq())
        self.assertEqual(0,hiker_.number_elements())

if __name__ == '__main__':
    unittest.main()