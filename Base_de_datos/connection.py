import pymysql


class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(host='localhost',
                                          user='root',
                                          password='42330102',
                                          db='just_in_time')

        self.close()

    def close(self):
        self.connection.close()

    def open(self):
        self.connection.connect()
        self.cursor = self.connection.cursor(pymysql.cursors.DictCursor)
