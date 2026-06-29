# %%
import os
from langchain.chat_models import init_chat_model
from langchain_openai import OpenAIEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
import faiss
import numpy as np
from rag.load_data import Storing
# this is rag, please send the str of the docs to load.
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

class Retriever:

    def __init__(self):
        self.embeddings = OpenAIEmbeddings(
            model="text-embedding-3-small"
        )

        self.vector_store = FAISS.load_local(
            "vector_store",
            self.embeddings,
            allow_dangerous_deserialization=True
        )

    def search(self, query):
        return self.vector_store.similarity_search(
            query,
            k=2
        )


