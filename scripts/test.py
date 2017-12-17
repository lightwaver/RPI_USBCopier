secondline = ""

if os.path.ismount("/media/usb0"):
	secondline = secondline + " usb0"

if os.path.ismount("/media/usb1"):
	secondline = secondline + " usb1"

print secondline;