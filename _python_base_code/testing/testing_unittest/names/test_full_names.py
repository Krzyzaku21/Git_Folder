import unittest
from full_names import get_full_name

class NamesTestCase(unittest.TestCase):
    'test for names.py'

    def test_first_last(self):
        'test names like Janis Joplin'
        full_name = get_full_name('Janis', 'Joplin')
        self.assertEqual(full_name, 'Janis Joplin')

if __name__ == '__main__':
    unittest.main()