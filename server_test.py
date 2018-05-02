import unittest
from server import *
from flask import Flask

app = Flask(__name__)


class ServerTest(unittest.TestCase):

    def test_status_code_200(self):
        pass

    def test_status_code_400(self):
        pass

    def test_response_is_json(self):
        pass


if __name__ == "__main__":
    unittest.main()        