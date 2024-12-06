# f= open("file io/text.txt")
# data = f.read()
# print(data)

# f.close()

with open("file io/text.txt", "a") as f:
    f.write("\nhello world!")