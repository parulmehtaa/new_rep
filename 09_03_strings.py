message="My name is Parul Mehta"
print(message)
print(message[0])
print(message[0],message[1])
print(message[3:])

print(message.index(" "))
print(message.rindex(" "))
words=message.split(" ")
print(words)
message="_".join(words)
print(message)

position_of_2nd_space=(len(words[0])+len(words[1])+1)
print(position_of_2nd_space)
words.sort()
print(words)