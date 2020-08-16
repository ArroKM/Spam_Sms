class Main:
	def __init__(self):
		try:
			shutil.rmtree("lib/__pycache__")
			shutil.rmtree("war/__pycache__")
		except: pass
		os.system('cls' if os.name == 'nt' else 'clear')
		self.menu()

	def menu(self):
		print(f"""    {p}_____ ____  __  ___
   / ___// __ \/  |/  /
   \__ \/ /_/ / /|_/ /    {k}[{c}*{k}] {q}:: Coded By Asecx ::{s}
  ___/ / ____/ /  / /     {k}[{c}*{k}] {r}:: {k}Spam SMS
 /____/_/   /_/  /_/\n
{k}[{c}1{k}] {u} SPAM {c}Airbnb
{k}[{c}2{k}] {u} SPAM {c}Grab
{k}[{c}3{k}] {u} SPAM {c}Pizza Hut
{k}[{c}4{k}] {u} SPAM {c}Olx
{k}[{c}5{k}] {u} SPAM {c}Redbus
{k}[{c}6{k}] {u} SPAM {c}Dekoruma {r}[{k}WA{r}]
{k}[{c}7{k}] {u} SPAM {c}Danacita
{k}[{c}8{k}] {u} SPAM {c}Badgr    {r}[{k}Email{r}]
{k}[{c}9{k}] {u} SPAM {c}Catchplay
{k}[{c}10{k}] {u} SPAM {c}E-mas
{k}[{c}0{k}] {r} Exit
""")
		pil = int(input(f'{p}xSECx {c}>> {k}'))
		if pil == 1:
			nom = input(f'{r}\nEx : {o}6289510512xxx\n{k}[*] {c}Nomor  : {k}')
			jml = int(input(f'{k}[?] {c}Jumlah : {k}'))
			Thread(air(nom, jml)).start()
		elif pil == 2:
			nom = input(f'{r}\nEx : {o}6289510512xxx\n{k}[*] {c}Nomor  : {k}')
			Thread(grab(self, nom)).start()
		elif pil == 3:
			nom = input(f'{r}\nEx : {o}89510512xxx\n{k}[*] {c}Nomor  : {k}')
			jml = int(input(f'{k}[?] {c}Jumlah : {k}'))
			Thread(hut(nom, jml)).start()
		elif pil == 4:
			nom = input(f'{r}\nEx : {o}89510512xxx\n{k}[*] {c}Nomor  : {k}')
			Thread(olx(self, nom)).start()
		elif pil == 5:
			nom = input(f'{r}\nEx : {o}89510512xxx\n{k}[*] {c}Nomor  : {k}')
			Thread(red(self, nom)).start()
		elif pil == 6:
			nom = input(f'{r}\nEx : {o}89510512xxx\n{k}[*] {c}Nomor  : {k}')
			jml = int(input(f'{k}[?] {c}Jumlah : {k}'))
			Thread(ruma(nom, jml)).start()
		elif pil == 7:
			nom = input(f'{r}\nEx : {o}89510512xxx\n{k}[*] {c}Nomor  : {k}')
			jml = int(input(f'{k}[?] {c}Jumlah : {k}'))
			Thread(dana(nom, jml)).start()
		elif pil == 8:
			mail = input(f'{r}\nEx : {o}Asecx@gmail.com\n{k}[*] {c}Email  : {k}')
			jml = int(input(f'{k}[?] {c}Jumlah : {k}'))
			Thread(mai(mail, jml)).start()
		elif pil == 9:
			nom = input(f'{r}\nEx : {o}085218xxx\n{k}[*] {c}Nomor  : {k}')
			jml = int(input(f'{k}[?] {c}Jumlah : {k}'))
			Thread(play(nom, jml)).start()
		elif pil == 10:
			nom = input(f'{r}\nEx : {o}085218xxx\n{k}[*] {c}Nomor  : {k}')
			jml = int(input(f'{k}[?] {c}Jumlah : {k}'))
			Thread(emas(nom, jml)).start()
		elif pil == 0:
			sleep(1)
			exit("")
		else:
			print(f"{k}[!] Pilih Yang Bener Cok")
			self.menu()

if __name__ == '__main__':
	try:
			import os,sys,shutil
			from time import sleep
			from threading import *
			from war.war import *
			from lib.a import *
			from lib.b import *
			from lib.c import *
			from lib.d import *
			from lib.e import *
			from lib.f import *
			from lib.g import *
			from lib.h import *
			from lib.i import *
			from lib.j import *
			os.system('xdg-open https://www.youtube.com/channel/UCuPp2fYqlG7IvltINFMAOgQ')
			Thread(target=Main).start()
	except IOError: pass
