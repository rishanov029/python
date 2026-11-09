str = input("Enter a string: ")
if str.endswith("ing"):
    print(str + "ly")
else:
    str += "ing"
print("Modified string:", str)