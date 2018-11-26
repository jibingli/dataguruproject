from django.test import TestCase
import requests


# Create your tests here.


class TestPolls(TestCase):
    def setUp(self):
        self.base_url = "http://127.0.0.1:8010"

    def test_detail_ok(self):
        resp = requests.get(self.base_url + "/polls/1/").json()
        self.assertEqual(resp['status'], "200")
        self.assertEqual(resp['message'], "success")
        self.assertEqual(resp['data']['1'], "生化危机")
        self.assertEqual(resp['data']['2'], "吃鸡")
        self.assertEqual(resp['data']['3'], "魔兽")

    def test_detail_fail(self):
        resp = requests.get(self.base_url + "/polls/3/").json()
        self.assertEqual(resp['status'], "10021")
        self.assertEqual(resp['message'], "null")
        self.assertEqual(resp['data'], {})

    def test_vote_ok(self):
        choice_id = 5
        resp = requests.post(self.base_url + "/polls/2/vote/", data={'choice': choice_id}).json()
        self.assertEqual(resp['status'], "200")
        self.assertEqual(resp['message'], "success")
        self.assertEqual(resp['data']['泰国'], 1)
        self.assertEqual(resp['data']['日本'], 5)
        self.assertEqual(resp['data']['新加坡'], 3)

    def test_vote_fail(self):
        resp = requests.post(self.base_url + "/polls/7/vote/", data={'choice': 5}).json()
        self.assertEqual(resp['status'], "10021")
        self.assertEqual(resp['message'], "fail")
        self.assertEqual(resp['data'], None)
