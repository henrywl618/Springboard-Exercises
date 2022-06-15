from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!
    def test_home_page(self):
        with app.test_client() as client:
            response = client.get('/')
            html = resp.get_data(as_text=True)

            self.assertIn('<table>',html)

