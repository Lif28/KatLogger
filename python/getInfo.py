import os 
import json
def GetIp():
    info = str(os.system("curl ipinfo.io > ciao.json"))
    

    with open("ciao.json", "r") as filew:
        file = json.load(filew)

        list = {"ip", "country", "region", "city", "org"}
        for a in list:
            b = file.get(a, "Not found")
            print(a,">", b)
