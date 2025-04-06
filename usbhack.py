# Now compatabile with Python3
import os
import time

while True:
    # time.sleep(2)
    os.system("wmic diskdrive get serialnumber > usblist.txt")
    
    with open("usblist.txt", "r", encoding="utf-16le") as readfile:
        content = readfile.read()

    word = "0416KK00000066840822"
    os.remove("usblist.txt")  # Cross-platform file delete

    if word in content:
        pass
    else:
        os.system("shutdown -l")  # -l (lowercase L) for logoff
