import unittest
from city_functions import get_formatted_city

class CityTestCase(unittest.TestCase):
    """Tests for 'city_function.py'."""

    def test_city_function(self):
        formatted_city = get_formatted_city("santiago", "chile")
        self.assertEqual(formatted_city, "Santiago, Chile")
    
    def test_city_pop_function(self):
        formatted_city = get_formatted_city("santiago", "chile", 5000000)
        self.assertEqual(formatted_city, "Santiago, Chile: 5000000")
        

if __name__ == "__main__":
    unittest.main()