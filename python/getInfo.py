import json
import subprocess
def GetIp():
    info = str(subprocess.run(["curl", "ipinfo.io", ">", "info.json"]))

    with open("ciao.json", "r") as filew:
        file = json.load(filew)

        list = {"ip", "country", "region", "city", "org"}
        for a in list:
            b = file.get(a, "Not found")
            return a, b
