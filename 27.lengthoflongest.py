def longest_word(words):
	"""Return the longest word in a list."""
	longest = ""
	for word in words:
		if len(word) > len(longest):
			longest = word
	return longest


words = input("Enter words separated by spaces: ").split()
print("Longest word:", longest_word(words))
