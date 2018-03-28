import json
import urllib.request
import os
import sys
import pygame
import time


class TTS():
	def play_tts(self,get_str):

		client_id = "6vNW1jYKk6ETlhsx4QAB"           # <= 변경 
		client_secret = "80mPSyDfbA" # <= 변경
		encText = urllib.parse.quote(get_str)
		data = "speaker=yuri&speed=0&text=" + encText; # jinho,mijin, clara, matt, shinji, yuri
		url = "https://openapi.naver.com/v1/voice/tts.bin"
		request = urllib.request.Request(url)
		request.add_header("X-Naver-Client-Id",client_id)
		request.add_header("X-Naver-Client-Secret",client_secret)
		response = urllib.request.urlopen(request, data=data.encode('utf-8'))
		rescode = response.getcode()
		if(rescode==200):
		    print("TTS mp3 저장")
		    response_body = response.read()
		    with open("test.mp3", "wb") as f:
		        f.write(response_body)
		    #os.system("chmod 777 test.mp3")
		    os.system("omxplayer test.mp3") # for Debin omx player
		else:
		    print("Error Code:" + rescode)