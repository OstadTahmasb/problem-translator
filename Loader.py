from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from AI import AI


class Loader:
    def __init__(self, file_name):
        self.splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=0, length_function=len,
                                                       separators=["\\d\\.", "\\.\\d"],
                                                       is_separator_regex=True)
        self.all_texts = []
        self.ai = AI()
        self.file_path = "Data/Problems/{name}.pdf"
        self.file_name = file_name
        self.loader = PyPDFLoader(self.file_path.format(name=self.file_name))
        self.pages = self.loader.load()

    def do_translation(self):
        f = open("Translation/{name}.tex".format(name=self.file_name), "w")
        for i in range(0, len(self.all_texts)):
            text = self.ai.translate(self.all_texts[i]),
            print(text, file=f)
            print(text)
            print("\\\\", file=f)

    def load_and_split(self):
        pass


class Main_Loader(Loader):
    def load_and_split(self):
        i = 0
        for page in self.pages[1:]:
            content = page.page_content
            split_text = self.splitter.split_text(content)
            for s in split_text[1:]:
                self.all_texts.append(s)
                print(s)
                print("-----------------------------------------" + str(i))
                i += 1

for year in range(1390, 1403):
	loader = Main_Loader(str(year))
	loader.load_and_split()
	loader.do_translation()
