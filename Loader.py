from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter_1 = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=0, length_function=len,
                                            separators=["\\.\\d", "\\d\\."], is_separator_regex=True)
splitter_2 = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=0, length_function=len,
                                            separators=[], is_separator_regex=True)


def english_nums(text):
    text = text.replace("١", "1")
    text = text.replace("۱", "1")
    text = text.replace("٢", "2")
    text = text.replace("۲", "2")
    text = text.replace("٣", "3")
    text = text.replace("۳", "3")
    text = text.replace("٤", "4")
    text = text.replace("۵", "5")
    text = text.replace("٥", "5")
    text = text.replace("٦", "6")
    text = text.replace("٧", "7")
    text = text.replace("٨", "8")
    text = text.replace("٩", "9")
    text = text.replace("۹", "9")
    text = text.replace("٠", "0")
    text = text.replace("۰", "0")
    text = text.replace(".", ".")
    return text


all_texts = []

loader = PyPDFLoader("Data/Problems/1390.pdf")
pages = loader.load()
for page in pages:
    content = page.page_content
    # content = english_nums(content)
    split_text = splitter_1.split_text(content)
    all_texts.append(split_text[1:])
    for s in split_text[1:]:
        print(s)
        print("-----------------------------------------")
        # for t in splitter_2.split_text(s):
        #     split_text.append(t)

# print(split_text[0])
