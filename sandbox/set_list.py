key = "[37, 1, 15, 43, 23]"

key_1 = key.replace("[", "")
key_2 = key_1.replace("]", "")
key_s = key_2.split(", ")

print(type(key_s))