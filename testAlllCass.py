# -*- coding: utf-8 -*-

from apitest.testvote import *


def testVote():
    test_post_vote()
    test_login()
    test_get_polls_detail()
    test_get_polls_index()


def testSearch():
    test_search_music()
    test_search_poetry()
    test_search_novelinfo()

