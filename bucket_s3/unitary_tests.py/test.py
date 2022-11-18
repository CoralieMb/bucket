from flask import Flask
import unittest
from moto import mock_s3
import boto3

class MyTest(unittest.TestCase):
    
    app = Flask(__name__)
    # we mock a bucket s3
    mock_s3 = mock_s3()

    bucket_name = 'bucket_test'
    key = '/path/to/obj'

    # setUp fonction will be executed before the test
    def setUp(self):
        self.mock_s3.start()
        s3 = boto3.resource('s3')

        bucket = s3.Bucket(self.bucket_name)
        bucket.create()
        
        # we give an item to the bucket
        object = s3.Object('bucket_test', 'file.txt')
        object.put(Body="hello")

    # tearDown fonction will be executed after the test
    def tearDown(self):
        self.mock_s3.stop()

    def test_get_item(self):
        body = "hello"
        client = self.app.test_client()
        rv = client.get('/get_item/bucket_test/file.txt')
        print(rv)
        self.assertEqual(rv.status_code, 200)
        self.assertEqual(rv.body, body)
        
if __name__ == '__main__':
    unittest.main()