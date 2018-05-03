import unittest
from server import app
from flask import Flask


app.testing = True


class ServerTest(unittest.TestCase):

    def test_status_code_200(self):
        # imitates a browser
        with app.test_client() as c:
            resp = c.get('/calculate_price/3/4')
            self.assertEqual(200, resp.status_code)
            #data = json.loads(resp.data)

    def test_status_code_400(self):
        with app.test_client() as c:
            resp = c.get('/calculate_price/100/4')
            self.assertEqual(400, resp.status_code)

    def test_response_is_json(self):
        pass

if __name__ == "__main__":
    unittest.main()        