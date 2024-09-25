import unittest
from googlenews import GoogleNews

class TestGoogleNews(unittest.TestCase):
    def setUp(self):
        self.news = GoogleNews()

    def test_top_news(self):
        result = self.news.top_news()
        self.assertIn('entries', result)
        self.assertTrue(len(result['entries']) > 0)

    def test_topic_headlines(self):
        result = self.news.topic_headlines('TECHNOLOGY')
        self.assertIn('entries', result)
        self.assertTrue(len(result['entries']) > 0)

    def test_search(self):
        result = self.news.search('Python programming')
        self.assertIn('entries', result)
        self.assertTrue(len(result['entries']) > 0)

if __name__ == '__main__':
    unittest.main()