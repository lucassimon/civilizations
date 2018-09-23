from vibora.tests import TestSuite

from apps import create_app

app = create_app('testing')


class HomeTestCase(TestSuite):
    def setUp(self):
        self.client = app.test_client()

    async def test_home(self):
        response = await self.client.get('/v1/home')
        self.assertEqual(response.content, b'{"hello":"world"}')
