# -*- coding: utf-8 -*-

from mysqlop import MySQLOP
import datetime


def inster_data(table, datas):
    db = MySQLOP()
    db.clear(table)
    for data in datas:
        db.insert(table, data)
    db.close()


table_poll_question = "polls_question"
datas_poll_question = [{'id': 1, 'question_text': '请选择你喜欢的游戏?', 'pub_date': datetime.datetime.now()},
                       {'id': 2, 'question_text': '你喜欢去哪里旅游?', 'pub_date': datetime.datetime.now()}
                       ]
table_poll_choice = "polls_choice"
datas_poll_choice = [{'id': 1, 'choice_text': '生化危机', 'votes': 0, 'question_id': 1},
                     {'id': 2, 'choice_text': '吃鸡', 'votes': 0, 'question_id': 1},
                     {'id': 3, 'choice_text': '魔兽', 'votes': 0, 'question_id': 1},
                     {'id': 4, 'choice_text': '泰国', 'votes': 0, 'question_id': 2},
                     {'id': 5, 'choice_text': '日本', 'votes': 0, 'question_id': 2},
                     {'id': 6, 'choice_text': '新加坡', 'votes': 0, 'question_id': 2}]

table_poll_user = "polls_user"
datas_poll_user = [{'id': 1, 'username': 'test', 'password': 'test'}, ]


def init_data():
    inster_data(table_poll_question, datas_poll_question)
    inster_data(table_poll_choice, datas_poll_choice)
    inster_data(table_poll_user, datas_poll_user)


if __name__ == '__main__':
    init_data()
