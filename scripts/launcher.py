#!/usr/bin/python
# Example using a character LCD connected to a Raspberry Pi
import time
import Adafruit_CharLCD as LCD
import datetime
import socket
import commands

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

while 1:
	lcd.clear()
	lcd.message(time.strftime("%d.%m.%y\n%H:%M:%S"))
	time.sleep(1.0)

lcd.clear()

