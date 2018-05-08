import pymysql
import datetime

class Shuttle:
	def get_now_seconds(self):
		now = datetime.datetime.now().time()
		total_second = 0
		total_second += now.hour * 3600
		total_second += now.minute * 60
		total_second += now.second
		return total_second

	def get_shuttle(self, departure, destination):
		conn = pymysql.connect(host='localhost', user='root', password='root', db='speaker', charset='utf8')
		curs = conn.cursor()

		sql = "select * from shuttle where departure='{}' and destination='{}'".format(departure, destination)
		curs.execute(sql)

		rows = curs.fetchall()

		conn.close()

		return_list = []

		for i in rows:
			total_second = self.get_now_seconds()
			gap_second = i[2].seconds - total_second

			if gap_second > 0:
				h = gap_second // 3600
				m = (gap_second % 3600) // 60
				return_list.append((i[0], i[1], str(i[2]), h, m))
				print('탑승가능')

			else:
				print('탑승불가')
		return return_list
