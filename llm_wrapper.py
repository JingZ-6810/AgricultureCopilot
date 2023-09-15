import openai
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI

OPENAI_API_KEY = ""

class LLMWrapper:
    """
    A Wrapper class for calling OpenAI GPT3.5 / GPT4 APIs
    """
    
    @staticmethod
    def init(api_key):
        openai.api_key = api_key
    TEMPLATE_QUESTION_GET_PAGE = ' Context: "{all_summaries}" Question: Which page may best answer the question? Please just give me the page number in digits. The question is: {question}'

    @staticmethod
    def ask(query, docs):
        prompt_template = """
Answer the question based on the context below. Keep the answer short and concise. Respond "Unsure about answer" if not sure about the answer, don't try to make up an answer.
# Context:
{context}

# Question: {question}
# Your Answer:
"""
        PROMPT = PromptTemplate(
            template=prompt_template, input_variables=["context", "question"]
        )
        llm = OpenAI(model_name="text-davinci-003",
                     temperature=0, # What sampling temperature to use.
                     top_p = 1, # Total probability mass of tokens to consider at each step.
                     max_tokens = 300,
                     openai_api_key=OPENAI_API_KEY)
        chain = load_qa_chain(llm=llm, chain_type="stuff", prompt=PROMPT)
        print('[API Call] DV3')
        response = chain({"input_documents": docs, "question": query}, return_only_outputs=True)
        return response['output_text']

