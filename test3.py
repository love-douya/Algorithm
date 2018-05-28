
fo = open("C:/test.txt", "r+")
fo.write("Hello\nWorld!")
fo.close()
fo = open("C:/test.txt", "r+")
txt = fo.read()
print(txt)
fo.close()

