#!/usr/bin/python
# Example using a character LCD connected to a Raspberry Pi

import time
import Adafruit_CharLCD as LCD
import datetime
import socket
import commands
import shutil
import os


usb0path = "/media/usb0"
usb1path = "/media/usb1"

#-------------------------------------------------------------
# Helper Functions
#-------------------------------------------------------------
def countFiles(directory):
    files = []
 
    if os.path.isdir(directory):
        for path, dirs, filenames in os.walk(directory):
            files.extend(filenames)
 
    return len(files)

def makedirs(dest):
    if not os.path.exists(dest):
        os.makedirs(dest)

def copyFilesWithProgress(src, dest, lcd):
	numFiles = countFiles(src)
 
	if numFiles > 0:
		makedirs(dest)
 
		numCopied = 0
 
		for path, dirs, filenames in os.walk(src):
			for directory in dirs:
				destDir = path.replace(src,dest)
				makedirs(os.path.join(destDir, directory))
            
			for sfile in filenames:
				srcFile = os.path.join(path, sfile)
 
				destFile = os.path.join(path.replace(src, dest), sfile)
                
				shutil.copy(srcFile, destFile)
                
				numCopied += 1
                
				progress = int(round( (done / float(total)) * 100))
				
				lcd.clear()
				msg = u'copy in progress\n{0}/{1}  {2}%'.format(done, total, progress)
				lcd.message(msg)


#-------------------------------------------------------------
# Main Task
#-------------------------------------------------------------

# raspbpberry Pi pin setup
lcd_rs = 25
lcd_en = 24
lcd_d4 = 23
lcd_d5 = 17
lcd_d6 = 18
lcd_d7 = 22
lcd_backlight = 2

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows = 2

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)
lcd.clear()

lcd.message('Hello!\n')

myIp = commands.getoutput("hostname -I")

lcd.message(myIp)
# Wait 5 seconds
time.sleep(2.0)
lcd.clear()

copied = 0
while 1:
	firstline = time.strftime("%d.%m.%y %H:%M")
	time.sleep(1.0)
	
	secondline = ""
	
	if os.path.ismount("/media/usb0"):
		secondline = secondline + " usb0"
	
	if os.path.ismount("/media/usb1"):
		secondline = secondline + " usb1"

	#print(secondline)
	lcd.clear()
	output = firstline +"\n" + secondline
	print(output)
	lcd.message(output)

	usb0=false
	usb1=false
	if os.path.ismount(usb0path):
		secondline += " usb0"
		usb0=true

	if os.path.ismount(usb1path):
		secondline += " usb1"
		usb1=true

	lcd.message(secondline)

	if usb0 & usb1 & (copied == 1):
		lcd.clear()
		lcd.message("copy starting")
		time.sleep(3.0)
		copyFilesWithProgress(usb1path, usb0path, lcd)

		lcd.clear()
		lcd.message("copy finished\remove the stick")
		time.sleep(3.0)
		copied = 1
	else:
		copied = 0
		 
lcd.clear()

