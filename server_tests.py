import unittest

import requests

class Testing(unittest.TestCase):

    URL = "127.0.0.1"
    PORT = "8000"
    address = "http://{}:{}".format(URL, PORT)

    def test_sum_valid(self):
        query = "sum?numbers=1,2,3"
        url = "{}/{}".format(self.address, query)
        r = requests.get(url)
        self.assertEqual(r.status_code, 200)

    def test_product_valid(self):
        query = "product?numbers=1,2,3"
        url = "{}/{}".format(self.address, query)
        r = requests.get(url)
        self.assertEqual(r.status_code, 200)

    def test_wrong_query(self):
        query = "sum?numbers=x,8"
        url = "{}/{}".format(self.address, query)
        r = requests.get(url)
        self.assertEqual(r.status_code, 400)

    def test_wrong_path(self):
        query = "not-only-sum"
        url = "{}/{}".format(self.address, query)
        r = requests.get(url)
        self.assertEqual(r.status_code, 400)


if __name__ == '__main__':
    unittest.main()

