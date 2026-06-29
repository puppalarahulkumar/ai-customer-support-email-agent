from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter


class Storing():

    def load_data(self, file_path):
        loader = TextLoader(file_path)
        docs = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,  # chunk size (characters)
            chunk_overlap=100,  # chunk overlap (characters)
            add_start_index=True,  # track index in original document
        )
        all_splits = text_splitter.split_documents(docs)

        embeddings = OpenAIEmbeddings(
            model="text-embedding-3-small"
        )
        try:
            vector_store = FAISS.from_documents(
                all_splits,
                embeddings
            )
            
            vector_store.save_local("vector_store")

            return vector_store
        except Exception as e:
            print(f"Error creating vector store: {e}")
