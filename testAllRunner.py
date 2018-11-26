# -*- coding: utf-8 -*-

import threading
from testAlllCass import *


def threads():
    threads = []
    threads.append(threading.Thread(target=testVote))
    # threads.append(threading.Thread(target=testSearch))
    for th in threads:
        th.start()
    th.join()


threads()
