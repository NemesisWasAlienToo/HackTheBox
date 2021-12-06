f = open("output.txt", "r")
content = f.read()
f.close()

values = content.split(" ")

cypher = []
key = []

for i in range(0, len(values)):
	val = int(values[i])
	if ((i % 2) == 0):
		cypher.append(val)
	else:
		key.append(val)

print(cypher)
print(key)