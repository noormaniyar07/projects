import os
import platform

def shutdown():
    """Shut down the system based on the operating system."""
    system_type = platform.system()
    if system_type == "Windows":
        os.system("shutdown /s /f /t 0")  
    elif system_type == "Linux" or system_type == "Darwin": 
        os.system("shutdown -h now")
    else:
        print("Operating system not supported!")

def restart():
    """Restart the system based on the operating system."""
    system_type = platform.system()
    if system_type == "Windows":
        os.system("shutdown /r /f /t 0")
    elif system_type in ["Linux", "Darwin"]:
        os.system("sudo reboot")
    else:
        print("Operating system not supported!")
command = input("Enter 'r' to restart or 's' to shutdown: ").lower()
if command == "s":
    shutdown()
elif command == "r":
    restart()
else:
    print("Invalid input. Please enter 'r' or 's'.")
