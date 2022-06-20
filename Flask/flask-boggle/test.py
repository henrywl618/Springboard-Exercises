from unittest import TestCase
from app import app
from boggle import Boggle
import json
import pdb


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
            with client.session_transaction() as change_session:
                change_session['gameboard'] = [['C','A','T','T','Y'],
                                               ['H','F','I','Y','C'],
                                               ['I','O','V','H','R'],
                                               ['I','O','V','H','R'],
                                               ['I','O','V','H','R']]

            response = client.post('/',
                                    data=json.dumps({'guess':'happy'}),content_type='application/json')
            result = response.get_data(as_text=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn('not-on-board',result)
        
            response = client.post('/',
                                    data=json.dumps({'guess':'cat'}),content_type='application/json')
            result = response.get_data(as_text=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn('ok',result)
    
    def test_endgame(self):
        with app.test_client() as client:
            client.get('/')
            response = client.post('/endgame',
                                    data=json.dumps({'score':20}),content_type='application/json')
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertEqual(session['highscore'],20)
            self.assertEqual(session['games_played'],1)


