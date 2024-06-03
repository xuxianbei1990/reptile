from MySqlUtil import MySqlUtil

myutil = MySqlUtil()
myresult = myutil.execute_query_sql("SELECT * FROM order_main")
for x in myresult:
    print(x)