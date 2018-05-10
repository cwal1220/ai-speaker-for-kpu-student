#-*- coding: utf-8 -*-

import json
import requests
import mise

sky_dict = {'SKY_D01': "맑은 날씨", 'SKY_D02': '구름이 조금 있는 날씨', 'SKY_D03': '구름이 많은 날씨', 'SKY_D04': '흐린 날씨', 'SKY_D05': '비가 오는 날씨', 'SKY_D06': '눈이 오는 날씨', 'SKY_D07': '비 또는 눈이 오는 날씨'}
tomorrow_sky_dict = {'SKY_M01': "맑은 날씨", 'SKY_M02': '구름이 조금 있는 날씨', 'SKY_M03': '구름이 많은 날씨', 'SKY_M04': '흐린 날씨', 'SKY_M05': '비가 오는 날씨', 'SKY_M06': '눈이 오는 날씨', 'SKY_M07': '비 또는 눈이 오는 날씨'}

def get_weather(lat, lon, city, time=0):

    current_weather = requests.get("https://api2.sktelecom.com/weather/current/hourly?version=1&lat=37&lon=126&appKey=fda2fe2c-3ad4-42fd-9162-4ad9ce9bf0e5")
    current_result = current_weather.json()
    
    temperature = current_result['weather']['hourly'][0]['temperature']['tc']


    summary_weather = requests.get("https://api2.sktelecom.com/weather/summary?version=1&lat=37&lon=126&appKey=fda2fe2c-3ad4-42fd-9162-4ad9ce9bf0e5")
    result = summary_weather.json()

    sky_code = result['weather']['summary'][0]['today']['sky']['code']
    tmax = result['weather']['summary'][0]['today']['temperature']['tmax']
    tmin = result['weather']['summary'][0]['today']['temperature']['tmin']

    tomorrow_sky_code = result['weather']['summary'][0]['tomorrow']['sky']['code']
    tomorrow_tmax = result['weather']['summary'][0]['tomorrow']['temperature']['tmax']
    tomorrow_tmin = result['weather']['summary'][0]['tomorrow']['temperature']['tmin']

    if time == 0:
        text = "현재 온도는 {temp} 도 이고, 오늘의 최고 기온은 {tmax} 도, 최저 기온은 {tmin} 도 이며, {sky}입니다. ".format(temp=temperature, tmax=tmax, tmin=tmin, sky=sky_dict[sky_code])
    else:
        text = "내일의 최고 기온은 {tmax} 도, 최저 지온은 {tmin} 도 이며, {sky}가 예상됩니다. ".format(tmax=tomorrow_tmax, tmin=tomorrow_tmin, sky=tomorrow_sky_dict[tomorrow_sky_code])

    text = text + mise.get_mise(city)

    return text

print(get_weather(37, 126, 'Seoul'))