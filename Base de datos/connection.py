import pymysql


class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(host='localhost',
                                          user='root',
                                          password='12345',
                                          db='just_in_time')

        self.cursor = self.connection.cursor()

    def close(self):
        self.connection.close()
