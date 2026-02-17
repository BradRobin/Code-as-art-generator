
import unittest
import os
import sys
from io import BytesIO

# Add project root to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from app import app

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Code-as-Art Generator', response.data)

    def test_file_upload_mock(self):
        # Mock file upload
        data = {
            'file': (BytesIO(b"def hello(): pass"), 'test_script.py')
        }
        response = self.app.post('/', data=data, content_type='multipart/form-data', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        # Check if result page elements are present
        self.assertIn(b'Visual Art', response.data)
        self.assertIn(b'ASCII Art', response.data)
        self.assertIn(b'Code Poetry', response.data)

if __name__ == '__main__':
    unittest.main()
