import os
import base64

def search(directory,key):
 for root, dirs, files in os.walk(directory):
    for file in files:
            path = root+"\\"+file
            if path.find(".xml") >= 1:
                file = open(path, "r", encoding="UTF-8", errors='')
                lines = file.readlines()
                data = []
                Hosts = [""]
                Port = [""]
                User = [""]
                Pass = [""]
                for line in lines:
                        if line.find("Host") >=1 or line.find("Port") >=1 or line.find("User") >=1 or line.find("Pass")>=1:
                            data.append(line.replace('	','').replace(' ','').replace("<Host>", "").replace('</Host>',' Host').replace("<Port>", "").replace('</Port>',' Port').replace("<User>", "").replace('</User>',' User').replace('<Passencoding="', " ").replace('<Pass>','').replace("</Pass>"," Pass").rstrip().replace('">','').replace('plaintextPassword','').replace(' crypt"pubkey="',''))
                for item in data:
                    if item.find("Host") >=1:
                        Hosts.append(item.replace(" Host", ""))
                    elif item.find("Port") >= 1:
                        Port.append(item.replace(" Port", ""))
                    elif item.find("User") >=1:
                        User.append(item.replace(" User", ""))
                    elif item.find("Pass") >=1:
                        Pass.append(item.replace(" Pass", ""))
                        if key == 1:
                           print(f"{Hosts[-1].rstrip()}:{Port[-1].rstrip()}:{User[-1].rstrip()}:{Pass[-1].replace(' base64','')}")
                        elif key == 2:
                            if item.find('base64') >=1:
                               print(f"{Hosts[-1]}:{Port[-1]}:{User[-1]}:{base64.b64decode(Pass[-1].replace(' base64','')).decode('UTF-8', errors='replace')}")
                            else:
                                print(f"{Hosts[-1]}:{Port[-1]}:{User[-1]}:{Pass[-1]}")
def menu():
    inpt = input("1 Собрать HOST:USER:PASS\n2 СОБРАТЬ HOST:USER:PASS + расшифровать пароли в base64\n")
    if inpt == "1":
       key = 1
       directory = input("путь: ").replace('"','')
       search(directory,key)
    elif inpt == "2":
        key = 2
        directory = input("путь: ").replace('"','')
        search(directory,key)
menu()
input()
