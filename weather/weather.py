#-*- coding: utf-8 -*-

import json
import urllib.request
import requests
import mise
import pos

sky_dict = {'SKY_D01': "맑은 날씨", 'SKY_D02': '구름이 조금 있는 날씨', 'SKY_D03': '구름이 많은 날씨', 'SKY_D04': '흐린 날씨', 'SKY_D05': '비가 오는 날씨', 'SKY_D06': '눈이 오는 날씨', 'SKY_D07': '비 또는 눈이 오는 날씨'}
tomorrow_sky_dict = {'SKY_M01': "맑은 날씨", 'SKY_M02': '구름이 조금 있는 날씨', 'SKY_M03': '구름이 많은 날씨', 'SKY_M04': '흐린 날씨', 'SKY_M05': '비가 오는 날씨', 'SKY_M06': '눈이 오는 날씨', 'SKY_M07': '비 또는 눈이 오는 날씨'}

def get_weather_str(addr, temp, tmax, tmin, sky, dust, dust_str):
	weather_str = "{}의 현재 온도는 {} 도 이고, 오늘의 최고 기온은 {} 도, 최저 기온은 {} 도 이며, {}입니다. ".format(addr, temp, tmax, tmin, sky)
	weather_str = weather_str + "또한 미세먼지 농도는 {}마이크로그램 퍼 제곱미터 이고, 상태는 {}입니다.".format(dust, dust_str)
	return weather_str


def get_weather(lat, lon, time=0):

	current_weather = requests.get("https://api2.sktelecom.com/weather/current/hourly?version=1&lat={}&lon={}&appKey=fda2fe2c-3ad4-42fd-9162-4ad9ce9bf0e5".format(lat, lon))
	current_result = current_weather.json()
	
	temperature = current_result['weather']['hourly'][0]['temperature']['tc']

	summary_weather = requests.get("https://api2.sktelecom.com/weather/summary?version=1&lat={}&lon={}&appKey=fda2fe2c-3ad4-42fd-9162-4ad9ce9bf0e5".format(lat, lon))
	result = summary_weather.json()

	sky_code = result['weather']['summary'][0]['today']['sky']['code']
	tmax = result['weather']['summary'][0]['today']['temperature']['tmax']
	tmin = result['weather']['summary'][0]['today']['temperature']['tmin']

	tomorrow_sky_code = result['weather']['summary'][0]['tomorrow']['sky']['code']
	tomorrow_tmax = result['weather']['summary'][0]['tomorrow']['temperature']['tmax']
	tomorrow_tmin = result['weather']['summary'][0]['tomorrow']['temperature']['tmin']

	addr = pos.get_addr(lat, lon)
	dust, dust_str = mise.get_mise(addr[:2])

	if time == 0:
		return get_weather_str(addr, temperature, tmax, tmin, sky_dict[sky_code], dust, dust_str)
	else:
		return "내일의 최고 기온은 {tmax} 도, 최저 기온은 {tmin} 도 이며, {sky}가 예상됩니다. ".format(tmax=tomorrow_tmax, tmin=tomorrow_tmin, sky=tomorrow_sky_dict[tomorrow_sky_code])
		

print(get_weather(37.33,127))