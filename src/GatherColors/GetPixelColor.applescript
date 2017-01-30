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

return {green, red, blue}