# -*- coding: utf-8 -*-
from locust import TaskSet, task, HttpLocust


class WebsiteTasks(TaskSet):
    def on_start(self):
        self.client.get(
            '/login?key=00d91e8e0cca2b76f515926a36db68f5&phone=13594347817&passwd=123456')

    @task(10)
    def novelSearch(self):
        self.client.get('/novelSearchApi?name=盗墓笔记')

    @task(8)
    def weatherApi(self):
        self.client.get('/weatherApi?city=成都')

    @task(5)
    def searchMusic(self):
        self.client.get('/searchMusic?name=需要人陪')

    @task(4)
    def searchEmail(self):
        self.client.get('/EmailSearch?number=1012002')


class UserBehavior(HttpLocust):
    task_set = WebsiteTasks
    host = 'https://www.apiopen.top'
    min_wait = 1000
    max_wait = 5000