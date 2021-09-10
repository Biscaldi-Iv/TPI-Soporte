import pymysql


class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(host='localhost',
                                          user='root',
                                          password='4716650',
                                          db='just_in_time')

        self.cursor = self.connection.cursor(pymysql.cursors.DictCursor)

    def close(self):
        self.connection.close()
