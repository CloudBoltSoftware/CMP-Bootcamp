from unittest import TestCase

from cmp.api import CloudBoltConnection
from settings import CB_UID, CB_PWD, CB_HOST


class TestCloudBoltConnection(TestCase):

    def test_login(self):
        with CloudBoltConnection(CB_UID, CB_PWD, CB_HOST) as conn:
            self.assertIsNotNone(conn.token)

    def test_get(self):
        with CloudBoltConnection(CB_UID, CB_PWD, CB_HOST) as conn:
            response = conn.get("/parameters/")
            self.assertTrue(response.json().get("count", 0) > 0)