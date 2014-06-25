from DisplayText import Display

with open("prose") as text:
	text_display = Display(text, ok_button="Accept")
	# ok_button is optional, C-c always closes the display without errors.
	text_display.show()
