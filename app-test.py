from app import app
import unittest

class BasicTestCase(unittest.TestCase):
    def test_idx(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, "Hello, world!")

if __name__ == '__main__':
    unittest.main()
