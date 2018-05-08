import json
import urllib.request

# 테스트용 Python Dictionary

api_url = "https://api2.sktelecom.com/weather/current/minutely?appKey=fda2fe2c-3ad4-42fd-9162-4ad9ce9bf0e5&version=1&lat=37&lon=126" #위도/경도
jsonString = urllib.request.urlopen(api_url).read().decode('utf8')

get_data = json.loads(jsonString)

type 	= get_data["weather"]["minutely"][0]["precipitation"]["type"] # 강수형태
sky 	= get_data["weather"]["minutely"][0]["sky"]["name"] # 하늘
tc 		= get_data["weather"]["minutely"][0]["temperature"]["tc"] # 현재 온도
tmax 	= get_data["weather"]["minutely"][0]["temperature"]["tmax"] #최고기온
tmin 	= get_data["weather"]["minutely"][0]["temperature"]["tmin"] # 최저기온
humi 	= get_data["weather"]["minutely"][0]["humidity"] # 상대습도
time 	= get_data["weather"]["minutely"][0]["timeObservation"] # 관측시간
wdir 	= get_data["weather"]["minutely"][0]["wind"]["wdir"] # 풍향
wspd 	= get_data["weather"]["minutely"][0]["wind"]["wspd"] # 풍속

str = "현재 날씨를 알려드리겠습니다. 현재 하늘은 " + sky + " 이고 현재온도는 " + str(float(tc)) + "도 입니다."


print(str)
