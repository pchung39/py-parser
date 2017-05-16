import unittest
from main import parse

class ParserTest(unittest.TestCase):
    def setUp(self):
        string_value = '''
        id
        first_name
        last_name
        email
        gender
        ip_address

        1
        Shirley
        Snyder
        ssnyder0@behance.net
        Female
        229.190.106.211
        '''

    def test_parser(self):
        response = parse('TEST_DATA.csv')
        self.assertEqual(parse('TEST_DATA.csv'), string_value)

if __name__ == '__main__':
    unittest.main()
