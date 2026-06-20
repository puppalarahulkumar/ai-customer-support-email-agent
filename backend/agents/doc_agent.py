from rag.retriever import Retriever
from agents.response_agent import ResponseAgent

class DocSearchAgent:
    def search_docs(self, query):
        # Implement your document search logic here
        # For example, you can use a vector database or a simple keyword search
        # Return the relevant documents based on the query
        return Retriever().search(query)
        

    