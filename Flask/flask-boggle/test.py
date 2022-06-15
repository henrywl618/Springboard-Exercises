from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     boggle_game = Boggle()
    #     gameboard = boggle_game.make_board()
    
    # def setUp(self):


    def test_home_page(self):
        with app.test_client() as client:
            response = client.get('/')
            html = response.get_data(as_text=True)
            
            self.assertEqual(response.status_code, 200)
            self.assertIn('<table>',html)

    def test_post_request(self):
        with app.test_client() as client:
            response = client.get('/')
            html = response.get_data(as_text=True)
            self.assertEqual(response.status_code, 200)

