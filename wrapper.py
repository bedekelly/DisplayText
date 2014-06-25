import textwrap


text = open("prose")

paragraphs = text.readlines()

lines = []
for para in paragraphs:
	lines.extend([line for line in textwrap.wrap(para, 70)])
	lines.append("")

for line in lines:
	print(line)