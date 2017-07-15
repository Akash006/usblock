# usblock
USB key authentication .

The original code for this usb authentication is in usbhack.py. 

Run this command in windows shell and get your usb serial ID.
  wmic diskdrive get serialnumber
  
Now copy your serial ID of the usb and paste it in the python script(usbhack.py) by replacing the value of variable(word).

Your python script is ready now

To make it windows executable . Make a new folder and copy setup.py and usbhack.py.

Open the cmd and come to that folder.

run the command 
  python setup.py py2exe
  
Your windows executable file is ready to secure you account.


Thanking you
