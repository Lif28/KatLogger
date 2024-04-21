import json
import os
import subprocess
def GetIp():
    info = os.system(str("curl ipinfo.io > info.json"))

    with open("info.json", "r") as filew:
        file = json.load(filew)

        list = {"ip", "country", "region", "city", "org"}
        for a in list:
            b = file.get(a, "Not found")
            return a, b
