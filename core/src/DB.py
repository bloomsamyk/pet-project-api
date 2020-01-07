from Parser.Parser import Parser
import mysql.connector


class DB:
    my_db = mysql.connector.connect(
        host="remotemysql.com",
        user="3DNd13uNO1",
        passwd="6NoEZ5peTq",
        database = "3DNd13uNO1"
    )


    def __init__(self):

        print(self.my_db)

        print('DB weather')

    def get_data(self):
        print('DB getData')

        my_cursor = self.my_db.cursor()

        my_cursor.execute("SELECT * FROM data")

        my_result = my_cursor.fetchall()

        for x in my_result:
            print(x)


        return 'data from DB'
