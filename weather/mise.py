#-*- coding: utf-8 -*-
import sys
import urllib.request
import json


def get_mise(city):
    convert_cityname = {'Seoul':u'서울','Busan':u'부산','Daegu':u'대구','Incheon':u'인천','Gwangju':u'광주','Daejeon':u'대전','Ulsan':u'울산','Gyeonggi':u'경기','Gangwon':u'강원','Chungbuk':u'충북','Chungnam':u'충남','Jeonbuk':u'전북','Jeonnam':u'전남','Gyeongbuk':u'경북','Gyeongnam':u'경남','Jeju':u'제주','Sejong':u'세종'}
    convert_dust_level = {u'1':u'좋음',u'2':u'보통',u'3':u'나쁨',u'4':u'매우나쁨'}
    url = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty"
    sidoName = convert_cityname[city]

    url = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=pbGF2mxEK2HNq6Xyl4qh3B9kq%2BSV%2FVq8LK3xetlrsNVTsQWhuTAtvxwPx6wc1pkWVHeZLuOF4nw5AYxnDyP2sQ%3D%3D&numOfRows=10&pageSize=10&pageNo=1&startPage=1&sidoName=%EC%84%9C%EC%9A%B8&ver=1.3&_returnType=json"
   
    jsonString = urllib.request.urlopen(url).read().decode('utf8')
    data = json.loads(jsonString)
    
    text = "또한 {city}의 미세먼지 농도는 {val} 이고, 상태는 {level}입니다.".format(city=sidoName, val=data["list"][1]["pm10Value"], level=convert_dust_level[data["list"][1]["pm10Grade"]])

    return text