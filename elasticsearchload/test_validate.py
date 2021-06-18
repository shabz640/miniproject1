import unittest
import big_to_smallcounter



class ElasticSearch(unittest.TestCase):
    def test_validate(self):
        self.assertEqual(big_to_smallcounter.index, 288)

if __name__ == '__main__':
    unittest.main()


