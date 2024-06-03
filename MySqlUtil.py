import mysql.connector


class MySqlUtil:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="127.0.0.1",  # 数据库主机地址
            port=3306,  # 数据库端口
            user="root",  # 数据库用户名
            password="1",  # 数据库密码
            database="pinyiche_pro"  # 要连接的数据库名
        )
    def execute_query_sql(self, sql):
        mycursor = self.mydb.cursor()
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        return myresult

