my_dict = {"banana": 3, "apple": 5, "cherry": 2}

ascending = dict(sorted(my_dict.items()))
descending = dict(sorted(my_dict.items(), reverse=True))

print("Ascending order:", ascending)
print("Descending order:", descending)
