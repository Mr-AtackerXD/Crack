#!/usr/bin/python2
#-*-coding:utf-8-*-

import os,re,sys,itertools,time,requests,random,threading,json,random
import requests,bs4,sys,os,subprocess
import requests,sys,random,time,re,base64,json
reload(sys)
sys.setdefaultencoding("utf-8")
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
reload(sys)

if ("linux" in sys.platform.lower()):

        N = '\033[0m'
        G = '\033[0;92m'
        O = '\033[0;97m'
        R = '\033[0;91m'
else:

        N = ''
        G = ''
        O = ''
        R = ''

def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.05)
		
def clear():
	if " linux" in sys.platform.lower():
		os.system("clear")
	elif "win" in sys.platform.lower():
		os.system("cls")
	else:os.system("clear")
		
def banner():
	print("""
\033[0;96m         
\033[0;96m ███████████████████████████
███████▀▀▀░░░░░░░▀▀▀███████
████▀░░░░░░░░░░░░░░░░░▀████
███│░░░░░░░░░░░░░░░░░░░│███
██▌│░░░░░░░░░░░░░░░░░░░│▐██
██░└┐░░░░░░░░░░░░░░░░░┌┘░██ \033[0;96m| \033[0;97mCoded By \033[0;96mDimasXD \033[0;97m& \033[0;96mLukas Bintang
\033[0;96m ██░░└┐░░░░░░░░░░░░░░░┌┘░░██
██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
██▌░│██████▌░░░▐██████│░▐██
███░│▐███▀▀░░▄░░▀▀███▌│░███
██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄  \033[0;96m| \033[0;97m \033[0;96m: \033[0;97
\033[0;96m ░░░▄██
████▄─┘██▌░░░░░░░▐██└─▄████
█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████  
█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████   \  \033[0;96m| \033[0;97m \033[0;96m: \033[0;97m
\033[0;96m ███████▄░░░░░░░░░░░▄███████
██████████▄▄▄▄▄▄▄██████████
███████████████████████████ \  \033[0;96m| \033[0;97mGithub \033[0;96m: \033[0;97mGithub.com/Mr-AtackerXD/Crack
\033[0;96m─────────────────────────────────────────────────────────────""")
		
def salam():
    os.system('clear')
    banner()
    jalan ("\n\033[0;97mAssalamualaikum, User SC Mr-AtackerXD...");time.sleep(0.05)
    jalan("\n\x1b[0;33mTerima Kasih Telah Menggunakan Script Ini Dan Telah Mensupport Kami Dalam Pengembangannya. Kritik Dan Saran Yang Telah Kami Terima Selama Ini Akan Kami Tampung Dan Jadikan Bahan Pengembangan Untuk SC Berikutnya");time.sleep(0.05)
    jalan("\n\x1b[0;33mSeiring Berjalannya Waktu, Kami Menyadari Bahwa Script Ini Telah Melebihi Batas Penggunaannya, Hingga Kami Meriset Sendiri, Dan Memang Benar Adanya");time.sleep(0.05)
    jalan("\n\x1b[0;33mBeberapa Pengguna SC Ini, Kemungkinan Makin Hari Merasakan Bahwa SC Lebih Sering Error, Bug, Lebih Lemot, Dan Hasilnya Tidak Banyak Seperti Dahulu");time.sleep(0.05)
    jalan("\n\x1b[0;33mMaka Dari Itu, Dengan Berat Hati Kami Menutup SC Ini Untuk Waktu Yang Tidak Bisa Dipastikan");time.sleep(0.05)
    jalan("\n\x1b[0;33mJangan Lupa Support Kami Untuk Pengembangan SC Terbaru Lainnya :)");time.sleep(0.05)
    jalan("\n\033[0;97m Mr-AtackerXD, Lukas Bintang\nJay\n")
    exit()

if __name__=='__main__':
  salam()
