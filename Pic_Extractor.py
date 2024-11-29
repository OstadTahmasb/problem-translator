from pypdf import PdfReader

name = "Data/Problems/{year}.pdf"
dest = "Translation/{year}/"
for i in range(1390, 1403):
    reader = PdfReader(name.format(year=str(i)))
    for page in reader.pages:
        for image in page.images:
            with open(dest.format(year=str(i)) + image.name, "wb") as fp:
                fp.write(image.data)
    print("done: " + str(i))