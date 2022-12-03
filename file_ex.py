text = "This is a test\nThis is new line 2\n"

# fp = open("myFile.txt", "w")
# fp = open("myFile.txt", "a") #append

fp = open("myFile.txt", "w")


# content = fp.read()

fp.write(text)

print(dir(fp))

fp.close()