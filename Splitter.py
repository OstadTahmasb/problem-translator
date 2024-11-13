from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import pandas as pd
import re

def is_short_answer(problem):
    if "a)" in problem and "b)" in problem and "c)" in problem and "d)" in problem:
        return True
    if "A)" in problem and "B)" in problem and "C)" in problem and "D)" in problem:
        return True
    if "1." in problem and "2." in problem and "3." in problem and "4." in problem:
        return True
    if "1)" in problem and "2)" in problem and "3)" in problem and "4)":
        return True
    if "a." in problem and "b." in problem and "c." in problem and "d.":
        return True
    if "A." in problem and "B." in problem and "C." in problem and "D.":
        return True
    return False

figures_regex = r"""\\begin{figure}\[.+\]
    \\centering
    \\includegraphics\[.+\]{(?P<path>.+)}
    \\caption{.+}
    \\label{.+}
\\end{figure}"""
def get_figure_paths(problem):
    return re.findall(figures_regex, problem)

def get_text(problem):
    trimmed_text = problem.strip()
    if problem[-2:] == "\\\\":
        trimmed_text = trimmed_text[:-2]
    if problems[1] == ".":
        trimmed_text = trimmed_text[2:]
    else:
        trimmed_text = trimmed_text[3:]
    return trimmed_text.strip()


splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=0, length_function=len, 
                                            separators=["\\n\\d{1,2}\\."], is_separator_regex=True)
all_problems = {
    "year": [],
    "number": [],
    "text": [],
    "is_short_answer": [],
    "figure_paths": [],
}
for year in range(1390, 1401):
    loader = TextLoader("final/{year}.txt".format(year=str(year)))
    docs = loader.load()
    problems = splitter.split_text(docs[0].page_content)

    for number, problem in enumerate(problems):
        all_problems["year"].append(year)
        all_problems["number"].append(number+1)
        all_problems["text"].append(get_text(problem))
        all_problems["is_short_answer"].append(is_short_answer(problem))
        all_problems["figure_paths"].append(get_figure_paths(problem))

df = pd.DataFrame(all_problems)
print(df.head())
df.to_csv("final.csv")