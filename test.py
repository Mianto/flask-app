from app import app
import unittest

class FlaskTestCase(unittest.TestCase):

    # Ensure that Flask app was set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type = 'html/text')
        self.assertEqual(response.status_code, 200)


    # Ensure that login page loads correctly
    def test_login_page(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type = 'html/text')
        self.assertTrue('Please Login' in response.data)


    # Ensure login behave correctly given correct credentials
    def test_correct_login(self):
        tester = app.test_client(self)
        response = tester.post('/login', # this is a post request
            data=dict(username='admin', password='admin'),
            follow_redirects=True
            )
        self.assertIn('You are now logged in', response.data)


    # Ensure login behave correctly given incorrect credentials
    def test_incorrect_login(self):
        tester = app.test_client(self)
        response = tester.post('/login', # this is a post request
            data=dict(username='wrong', password='wrong'),
            follow_redirects=True
            )
        self.assertIn('Invalid Credential.Please try again.', response.data)


    #Ensure that logout behaves correctly
    def test_logout(self):
        tester = app.test_client(self)
        tester.post('/login',
            data=dict(username='admin', password='admin'),
            follow_redirects=True)
        response = tester.posts('/logout', redirects=True)
        self.assertIn('You were just logged out', response.data)


    # Ensure that home page requires login
    def test_main_page_require_login(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type = 'html/text')
        self.assertTrue('You need to login first' in response.data)


    def test_post_shows_up(self):
        tester = app.test_client(self)
        response = tester.post(
                '/login',
                data=dict(username='admin', password='admin'),
                redirects=True
            )
        self.assertIn('Good', response.data)





if __name__=='__main__':
    unittest.main()

