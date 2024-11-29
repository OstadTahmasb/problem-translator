import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')


class AI:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4o", temperature=0)
        self.__init_translation_chain()

    def __init_translation_chain(self):
        translation_prompt = ChatPromptTemplate([
            ("system", "You are a math teacher who specializes in mathematical olympiad. You are asked to translate the given questions to you by the user to polite english. Just translate the text and do not add anything to it. Print the output in LaTeX and put the equations between dollar signs. Only return the LaTeX code."),
            ("human", "Translate the question below from persian to english.\n\nquestion:\n>>>>>>>>>>\n{question}\n<<<<<<<<<")
        ])
        self.translation_chain = translation_prompt | self.llm | StrOutputParser()

    def translate(self, question):
        return self.translation_chain.invoke({'question': question})
