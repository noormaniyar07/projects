import os
import platform

def shutdown():
    if platform.system() == "Windows":
        os.system('shutdown -s')
    elif platform.system() == "Linux" or platform.system() == "Darwin":
        os.system("shutdown -h now")
    else:
        print("Os not supported!")

def restart():
    system_type = platform.system()
    if system_type == "Windows":
        os.system("shutdown -t 0 -r -f")  
    elif system_type in ["Linux", "Darwin"]:
        os.system('sudo reboot now')  
    else:
        print("OS not supported!")


command = input("Use \'r\' for restart and \'s\' for shutdown: ").lower()

if command == "r":
    restart()
elif command == "s":
    shutdown()
else:
    print("Wrong letter")
