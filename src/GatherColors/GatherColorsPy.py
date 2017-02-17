from subprocess import Popen, PIPE
from PIL import ImageGrab
"""
apple_script_gather_colors = '''
    set {green, red, blue} to {-1, -1, -1}

    tell application "Digital Color Meter" to activate
    tell application "System Events"
	tell process "Digital Color Meter"
		click menu item "Copy Color as Text" of menu 1 of menu bar item "Color" of menu bar 1
	end tell
    end tell

    delay 0.1

    set grbColors to words of (the clipboard)
    if (count of grbColors) is 3 then
	set {green, red, blue} to {item 2 of grbColors, item 1 of grbColors, item 3 of grbColors}
    end if

    delay 0.1

    tell application "System Events"
	tell process "Digital Color Meter"
		click menu item "Quit Digital Color Meter" of menu 1 of menu bar item "Digital Color Meter" of menu bar 1
	end tell
    end tell

    return {green, red, blue}'''

process = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate(apple_script_gather_colors)
print ( process.returncode, stdout, stderr)
"""
screen_grab = ImageGrab.grab( bbox = (10, 10, 11, 11) )
print ( screen_grab.getpixel( (0, 0) ))
