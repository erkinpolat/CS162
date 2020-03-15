import unittest
import app
import os

class TestApp(unittest.TestCase):

	def setUp(self):
		self.db_fd, app.app.config['DATABASE'] = tempfile.mkstemp()
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()
        with app.app.app_context():
            app.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(app.app.config['DATABASE'])

    def test_index(self):
        request = self.app.get('/', follow_redirects=True)
        self.assertEqual(request.status_code, 200)

    def test_add(self):
        request = self.app.post('/add', data = dict(text='Testing Task'), follow_redirects=True)
        self.app.get('/delete/1', follow_redirects = True)
        self.assertEqual(request.status_code, 200)

    def test_delete(self):
        self.test_add()
        request = self.app.get('/delete/1', follow_redirects = True)
        self.assertEqual(request.status_code, 200)

    def test_move_right(self):
        self.test_add()
        request = self.app.get('/move_right/1', follow_redirects = True)
        self.app.get('/delete/1', follow_redirects = True)
        self.assertEqual(request.status_code, 200)

    def test_move_back(self):
        self.test_add()
        self.test_move_right
        request = self.app.get('/move_back/1', follow_redirects = True)
        self.app.get('/delete/1', follow_redirects = True)
        self.assertEqual(request.status_code, 200)





if __name__ == '__main__':
    unittest.main()