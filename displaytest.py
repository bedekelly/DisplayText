from DisplayText import Display

with open("prose") as text_file:
	text = text_file.read()
	text_display = Display(text, ok_button="Accept")
	text_display.show()