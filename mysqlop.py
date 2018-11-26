# -*- coding: utf-8 -*-

import pymysql.cursors
from logger import logger
from testdata.getpath import GetConfigFile
import configparser


class MySQLOP():
    def __init__(self):
        config = configparser.ConfigParser()
        config.read(GetConfigFile('db.conf'))
        mysqldb = config['Mysql']
        try:
            # Connect to the database
            self.connection = pymysql.connect(host=mysqldb['host'], user=mysqldb['user'], password=mysqldb['password'],
                                              db=mysqldb['dbname'], port=int(mysqldb['port']),
                                              charset=mysqldb['charset'], cursorclass=pymysql.cursors.DictCursor)
        except pymysql.err.OperationalError as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    def clear(self, table_name):
        real_sql = "DELETE FROM " + table_name + ";"
        logger.info(real_sql)
        with self.connection.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(real_sql)
        self.connection.commit()

    def insert(self, table_name, data):
        for key in data:
            data[key] = "'" + str(data[key]) + "'"
        key = ','.join(data.keys())
        value = ','.join(data.values())
        real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES (" + value + ")"
        logger.info(real_sql)
        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)
        self.connection.commit()

    def close(self):
        self.connection.close()

    def update(self, table_name, data, condition):
        value = ','.join([k + "='" + str(v) + "'" for k, v in data.items()])
        real_sql = "UPDATE " + table_name + " SET " + value + " WHERE " + condition
        logger.info(real_sql)
        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)
        self.connection.commit()

    def find(self, table_name, data='*', condition=None):
        if condition:
            real_sql = "SELECT " + data + " FROM " + table_name + " WHERE " + condition
        else:
            real_sql = "SELECT " + data + " FROM " + table_name
        logger.info(real_sql)
        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)
        return cursor.fetchall()


if __name__ == '__main__':
    import datetime

    db = MySQLOP()
    table_name = "polls_question"
    data = {'id': 1, 'question_text': '你喜欢的游戏是什么?', 'pub_date': datetime.datetime.now()}
    db.clear(table_name)
    db.insert(table_name, data)
    data2 = {'question_text': '你喜欢的电影是什么?', 'pub_date': datetime.datetime.now()}
    db.update(table_name, data2, "id=1")
    print(db.find(table_name, condition='id=1'))
    db.close()
