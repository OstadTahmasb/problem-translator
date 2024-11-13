f = open("Translation/1396.tex", "r")
text = f.read()
text = text.replace("\\\\", "\\")

f.close()
f = open("Translation/1396-2.tex", "w")
print(text, file=f)
f.close()