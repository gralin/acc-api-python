from tests.context import USER_KEY, USER_NONCE, USER_TIME, USER_TOKEN
from accapi.token import AccToken
from unittest import mock
import unittest


class TokenTest(unittest.TestCase):

    @mock.patch('time.time', mock.MagicMock(return_value=USER_TIME))
    def test_token(self):
        token = AccToken(USER_NONCE, USER_KEY).generate()
        self.assertEqual(token, USER_TOKEN)
