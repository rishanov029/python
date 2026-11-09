text = input("Enter a string: ")

if len(text) > 1:
	text = text[-1] + text[1:-1] + text[0]

print(text)
