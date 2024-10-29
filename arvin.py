f = open("Translation/1393.tex", "r")
text = f.read()
text = text.replace("\\\\", "\\")

f.close()
f = open("Translation/1393-2.tex", "w")
print(text, file=f)
f.close()