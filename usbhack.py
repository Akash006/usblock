import os, time, codecs

i = 1
while i > 0:
    #time.sleep(2)
    usblist = os.system("wmic diskdrive get serialnumber > usblist.txt")
    readfile = open("usblist.txt", "r")
    a = readfile.read()
    b = unicode(a,"utf_16le")
    closefile = readfile.close()
    word = "0416KK00000066840822"
    if word in b:
        os.system("del \f usblist.txt")
        pass
    else:
        os.system("del \f usblist.txt")
        os.system("shutdown -L")
