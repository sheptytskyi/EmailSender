from unittest import TestCase
from fastapi.testclient import TestClient

from producer.app import app
from producer.models import Emails
from producer.db import SessionLocal


class TestApiMethods(TestCase):

    def setUp(self) -> None:
        self.client = TestClient(app=app)

    def test_get(self) -> None:
        response = self.client.get('/')
        db = SessionLocal()

        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.text, str(db.query(Emails).all()))
