import pymysql

class dbConnection:
    def __init__(self):
        print("")
    def createConnection(self):

        return pymysql.connect(host = 'localhost',
                            user = 'disneytracker',
                            database = 'disneytracker',
                            charset = 'utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)


if __name__ == "__main__":
    connector = dbConnection()
    connection = connector.createConnection()
