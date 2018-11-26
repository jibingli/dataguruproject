# -*- coding: utf-8 -*-

from testrequest import TestPostRequest, TestGetRequest
import xlrd
from testdata.getpath import GetTestDataPath

url = "http://127.0.0.1:8000"

testdata = xlrd.open_workbook(GetTestDataPath())


def test_post_vote():
    try:
        hdata = {
            'choice': "5"
        }
        testcaseid = "1-1"
        testname = "testvote" + testcaseid
        testhope = "200"
        fanhuitesthope = "success"
        header = {
            "content-type": "application/x-www-form-urlencoded"

        }
        r = TestPostRequest(url + "/polls/2/vote/", hdata, header, testcaseid, testname, testhope, fanhuitesthope)
    except Exception as e:
        print(e)


def test_get_polls_detail():
    try:
        hdata = ""
        testcaseid = "1-2"
        testname = "testvote" + testcaseid
        testhope = "200"
        fanhuitesthope = "success"
        header = {
            "content-type": "application/x-www-form-urlencoded"

        }
        r = TestGetRequest(url + "/polls/1", hdata, header, testcaseid, testname, testhope, fanhuitesthope)
    except Exception as e:
        print(e)


def test_get_polls_index():
    try:
        hdata = ""
        testcaseid = "1-3"
        testname = "testvote" + testcaseid
        testhope = "200"
        fanhuitesthope = "success"
        header = {
            "content-type": "application/x-www-form-urlencoded"

        }
        r = TestGetRequest(url + "/polls", hdata, header, testcaseid, testname, testhope, fanhuitesthope)
    except Exception as e:
        print(e)


def test_login():
    table = testdata.sheets()[2]
    for i in range(3, 5):
        username = table.cell(i, 0).value
        password = table.cell(i, 1).value
        qiwang = table.cell(i, 2).value
        hdata = {
            'username': username,
            'password': password
        }
        header = {
            'content-type': "application/x-www-form-urlencoded"
        }
        testcaseid = "1-1"
        testname = "testlogin" + testcaseid
        testhope = "200"
        fanhuitesthpe = qiwang
        r = TestPostRequest(url + '/polls/login/', hdata, header, testcaseid, testname, testhope, fanhuitesthpe)


def test_search_poetry():
    table = testdata.sheets()[3]
    for i in range(3, 5):
        name = table.cell(i, 0).value
        qiwang = table.cell(i, 1).value
        hdata = {
            "name":name
        }
        testcaseid = "1-1"
        testname = "test_search_poetry" + testcaseid
        testhope = "200"
        fanhuitesthope = qiwang
        header = {
            "content-type": "application/x-www-form-urlencoded"

        }
        r = TestGetRequest("http://api.apiopen.top/searchPoetry", hdata, header, testcaseid, testname, testhope, fanhuitesthope)

def test_search_music():
    table = testdata.sheets()[3]
    for i in range(13, 15):
        name = table.cell(i, 0).value
        qiwang = table.cell(i, 1).value
        hdata = {
            "name":name
        }
        testcaseid = "1-1"
        testname = "test_search_music" + testcaseid
        testhope = "200"
        fanhuitesthope = qiwang
        header = {
            "content-type": "application/x-www-form-urlencoded"

        }
        r = TestGetRequest("http://api.apiopen.top/searchMusic", hdata, header, testcaseid, testname, testhope, fanhuitesthope)

def test_search_novelinfo():
    table = testdata.sheets()[3]
    for i in range(21, 23):
        name = table.cell(i, 0).value
        qiwang = table.cell(i, 1).value
        hdata = {
            "name":name
        }
        testcaseid = "1-1"
        testname = "test_search_music" + testcaseid
        testhope = "200"
        fanhuitesthope = qiwang
        header = {
            "content-type": "application/x-www-form-urlencoded"

        }
        r = TestGetRequest("https://www.apiopen.top/novelInfoApi", hdata, header, testcaseid, testname, testhope, fanhuitesthope)
