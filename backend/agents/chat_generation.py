from langchain.chat_models import init_chat_model
from langchain.messages import SystemMessage
from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")

os.environ["OPENAI_API_KEY"]=OPENAI_API_KEY


class ChatGenerationAgent:
    def __init__(self):
        
        self.model=init_chat_model("openai:gpt-4.1-nano",temperature=0)

    def generate_response(self, query, context):
        return self.model.invoke([SystemMessage(content=f"you need to generate the response for the query: {query}")] + 
                          [SystemMessage(content=f"here is some context to help you: {context}")])
    
