
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
load_dotenv()
## this is my google gemini api key
class LLMManager:
    def __init__(self) ->None:
        self.model = "gpt-3.5-turbo"
        self.api_key = os.getenv("OPENAI_API_KEY") 
    def get_llm(self):
        get_llm = ChatOpenAI(model=self.model,api_key = self.api_key )
        return get_llm
