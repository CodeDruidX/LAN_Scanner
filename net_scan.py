def scanner(mask):
	for i in range(int(mask[0]=="X")*255+1):
		if mask[0]!="X":i=mask[0]
	
		for ii in range(int(mask[1]=="X")*255+1):
			if mask[1]!="X":ii=mask[1]
	
			for iii in range(int(mask[2]=="X")*255+1):
				if mask[2]!="X":iii=mask[2]
	
				for iiii in range(int(mask[3]=="X")*255+1):
					if mask[3]!="X":iiii=mask[3]
					if not os.system(f"ping {str(i)}.{str(ii)}.{str(iii)}.{str(iiii)} -n 1 -w 10>>nul"):
						mac=subprocess.getoutput(f"arp -a {str(i)}.{str(ii)}.{str(iii)}.{str(iiii)}").split()[-3]
						vendor=requests.get("https://api.macvendors.com/"+mac).content.decode()
						if not "error" in vendor:print(f"{Fore.GREEN}Connected{Fore.RESET}:",i,ii,iii,iiii,f"with{Fore.GREEN}",vendor,"device",Fore.RESET)
						else:print(f"{Fore.GREEN}Connected{Fore.RESET}:",f"{str(i)}.{str(ii)}.{str(iii)}.{str(iiii)}",f"with {Fore.RED}unknown{Fore.RESET} device")
					else:
						pass
						print(f"# {Fore.YELLOW}Scanning{Fore.RESET}:",i,ii,iii,iiii,"    ",end="\r")



import os
import subprocess
import requests
from colorama import init,Fore
init()
mask=input(f"{Fore.YELLOW}Scanning{Fore.RESET} mask like (192.168.0.X) or (123.45.X.X):").split(".")
scanner(mask)
