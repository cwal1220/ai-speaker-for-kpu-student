import pymysql
import random
import time
import os
def get_food():
	conn = pymysql.connect(host='localhost', user='root', password='root', db='speaker', charset='utf8')
	curs = conn.cursor()
	sql = "select * from foodcourt"
	curs.execute(sql)
	rows = curs.fetchall()
	conn.close()
	rows = random.sample(rows, len(rows))
	return rows


if __name__ == "__main__":
	for i in get_food():
		os.system("clear")
		print(i)
		time.sleep(0.01)
